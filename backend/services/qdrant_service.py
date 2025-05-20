from typing import List, Dict, Any, Optional
import uuid
from loguru import logger
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.http import models as rest
from qdrant_client.http.models import Distance, VectorParams
import os

class QdrantSourceStore:
    """Service for storing and retrieving source documents using Qdrant and OpenAI embeddings."""

    def __init__(
        self,
        qdrant_url: str = "localhost",
        qdrant_api_key: Optional[str] = None,
        collection_name: str = "sources",
        embedding_model: str = "text-embedding-3-small",
        openai_api_key: Optional[str] = None,
        chunk_size: int = 512,
        chunk_overlap: int = 50,
    ):
        """Initialize Qdrant source store.

        Args:
            qdrant_url: URL of Qdrant server
            qdrant_api_key: API key for Qdrant
            collection_name: Name of the collection to store sources
            embedding_model: OpenAI embedding model name
            openai_api_key: OpenAI API key
            chunk_size: Size of chunks for text splitting
            chunk_overlap: Overlap between chunks
        """
        logger.info(f"Initializing QdrantSourceStore with collection: {collection_name}")

        self.collection_name = collection_name
        self.embedding_model = embedding_model
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        # Initialize Qdrant client
        logger.info(f"Connecting to Qdrant at {qdrant_url}")
        self.qdrant_client = QdrantClient(
            url=qdrant_url,
            api_key=qdrant_api_key,
            prefer_grpc=True,
        )

        # Initialize OpenAI client
        logger.info("Initializing OpenAI client")
        self.openai_client = OpenAI(api_key=openai_api_key)

        # Create collection if it doesn't exist
        self._create_collection_if_not_exists()

    def _create_collection_if_not_exists(self) -> None:
        """Create collection if it doesn't exist."""
        logger.info("Checking if collection exists")
        collections = self.qdrant_client.get_collections().collections
        collection_names = [collection.name for collection in collections]

        if self.collection_name not in collection_names:
            logger.info(f"Collection {self.collection_name} does not exist, creating...")
            # Get vector size from embedding model
            vector_size = self._get_embedding_size()

            # Create collection
            self.qdrant_client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE,
                ),
            )

            # Create payload index for notebook_id for faster filtering
            logger.info("Creating payload index for notebook_id")
            self.qdrant_client.create_payload_index(
                collection_name=self.collection_name,
                field_name="notebook_id",
                field_schema=rest.PayloadSchemaType.KEYWORD,
            )

            logger.info(f"Created collection: {self.collection_name}")

    def _get_embedding(self, text: str) -> List[float]:
        """Get embedding for text using OpenAI."""
        logger.info(f"Getting embedding using model {self.embedding_model}")
        response = self.openai_client.embeddings.create(
            input=text,
            model=self.embedding_model,
        )
        return response.data[0].embedding

    def _get_embedding_size(self) -> int:
        """Get embedding size for the model."""
        # Simple text to get embedding size
        test_text = "Test"
        embedding = self.openai_client.embeddings.create(
            input=test_text,
            model=self.embedding_model,
        )
        return len(embedding.data[0].embedding)


    def _chunk_text(self, text: str) -> List[str]:
        """Split text into chunks based on chunk size and overlap.

        Args:
            text: The text to split into chunks

        Returns:
            List of text chunks with specified size and overlap
        """
        if not text:
            logger.warning("Empty text provided for chunking")
            return []

        logger.info(f"Chunking text with size {self.chunk_size} and overlap {self.chunk_overlap}")
        # Use list comprehension for cleaner chunk creation
        tokens = text.split()
        chunk_starts = range(0, len(tokens), self.chunk_size - self.chunk_overlap)
        chunks = [
            " ".join(tokens[i:i + self.chunk_size])
            for i in chunk_starts
            if i + self.chunk_size <= len(tokens)
        ]

        # Handle remaining tokens if any
        if tokens[chunk_starts[-1]:]:
            chunks.append(" ".join(tokens[chunk_starts[-1]:]))

        logger.info(f"Created {len(chunks)} chunks")
        return chunks

    def add_source(
        self,
        url: str,
        page_title: str,
        content: str,
        summary: str,
        notebook_id: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> List[str]:
        """Add source document to Qdrant.

        Args:
            url: Source URL
            page_title: Page title
            content: Source content
            summary: Source summary
            notebook_id: Notebook ID for filtering
            metadata: Additional metadata

        Returns:
            List of IDs for the stored chunks
        """
        logger.info(f"Adding source document: {url} for notebook {notebook_id}")

        if metadata is None:
            metadata = {}

        # Chunk content for better retrieval
        chunks = self._chunk_text(content)

        # Store IDs of added chunks
        chunk_ids = []

        # Process each chunk
        logger.info(f"Processing {len(chunks)} chunks")
        for i, chunk in enumerate(chunks):
            # Generate unique ID
            chunk_id = str(uuid.uuid4())
            chunk_ids.append(chunk_id)

            # Create payload
            payload = {
                "url": url,
                "page_title": page_title,
                "content_chunk": chunk,
                "chunk_index": i,
                "total_chunks": len(chunks),
                "summary": summary,
                "notebook_id": notebook_id,
                **metadata,
            }

            # Get embedding
            embedding = self._get_embedding(chunk)

            # Store in Qdrant
            logger.info(f"Storing chunk {i+1}/{len(chunks)} in Qdrant")
            self.qdrant_client.upsert(
                collection_name=self.collection_name,
                points=[
                    rest.PointStruct(
                        id=chunk_id,
                        vector=embedding,
                        payload=payload,
                    )
                ],
            )

        logger.info(f"Added source with {len(chunks)} chunks: {url}")
        return chunk_ids

    def search(
        self,
        query: str,
        notebook_id: Optional[str] = None,
        limit: int = 5,
    ) -> List[Dict[str, Any]]:
        """Search for sources based on query and notebook ID.

        Args:
            query: Search query
            notebook_id: Optional notebook ID to filter results
            limit: Maximum number of results

        Returns:
            List of matching sources with scores
        """
        logger.info(f"Searching for: '{query}' in notebook: {notebook_id}")

        # Get query embedding
        query_embedding = self._get_embedding(query)

        # Set up filter if notebook_id is provided
        filter_param = None
        if notebook_id:
            logger.info(f"Applying notebook filter: {notebook_id}")
            filter_param = rest.Filter(
                must=[
                    rest.FieldCondition(
                        key="notebook_id",
                        match=rest.MatchValue(value=notebook_id),
                    )
                ]
            )

        # Search in Qdrant
        logger.info(f"Executing search with limit: {limit}")
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=limit,
            filter=filter_param,
        )

        # Format results
        results = []
        for scored_point in search_result:
            results.append({
                "id": scored_point.id,
                "score": scored_point.score,
                "url": scored_point.payload.get("url"),
                "page_title": scored_point.payload.get("page_title"),
                "content_chunk": scored_point.payload.get("content_chunk"),
                "summary": scored_point.payload.get("summary"),
                "notebook_id": scored_point.payload.get("notebook_id"),
            })

        logger.info(f"Found {len(results)} matching results")
        return results

    def delete_by_notebook_id(self, notebook_id: str) -> int:
        """Delete all sources for a specific notebook ID.

        Args:
            notebook_id: Notebook ID to delete

        Returns:
            Number of deleted points
        """
        logger.info(f"Deleting all sources for notebook: {notebook_id}")

        filter_param = rest.Filter(
            must=[
                rest.FieldCondition(
                    key="notebook_id",
                    match=rest.MatchValue(value=notebook_id),
                )
            ]
        )

        result = self.qdrant_client.delete(
            collection_name=self.collection_name,
            points_selector=rest.FilterSelector(filter=filter_param),
        )

        logger.info(f"Deleted {result.status.deleted} points for notebook {notebook_id}")
        return result.status.deleted

qdrant_service = QdrantSourceStore(
    qdrant_url=os.getenv("QDRANT_API_URL"),
    qdrant_api_key=os.getenv("QDRANT_API_KEY"),
    collection_name="notebook_sources",
    embedding_model="text-embedding-3-small",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
)
