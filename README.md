# 🔍 DecipherIt - AI-Powered Research Assistant

<div align="center">

![DecipherIt Logo](https://img.shields.io/badge/DecipherIt-AI%20Research%20Assistant-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJMMTMuMDkgOC4yNkwyMCA5TDEzLjA5IDE1Ljc0TDEyIDIyTDEwLjkxIDE1Ljc0TDQgOUwxMC45MSA4LjI2TDEyIDJaIiBmaWxsPSJjdXJyZW50Q29sb3IiLz4KPC9zdmc+)

**Transform your research process with AI-powered intelligence**

[![Next.js](https://img.shields.io/badge/Next.js-15.3.2-black?style=flat-square&logo=next.js)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-19.0.0-blue?style=flat-square&logo=react)](https://reactjs.org/)
[![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)](https://python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue?style=flat-square&logo=typescript)](https://typescriptlang.org/)

[🚀 Live Demo](https://decipherit.xyz) • [🛠️ Installation](#installation) • [🤝 Contributing](#contributing)

</div>

---
## ⭐ Star on GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=mtwn105/decipher-research-agent&type=Date)](https://www.star-history.com/#mtwn105/decipher-research-agent&Date)
---

## ✨ Overview

DecipherIt is a cutting-edge AI-powered research assistant inspired by **Google NotebookLM** that revolutionizes how researchers, students, and professionals explore, analyze, and synthesize information from the web. The platform transforms any combination of documents, URLs, or topics into comprehensive research notebooks complete with AI-generated summaries, interactive Q&A capabilities, audio overviews, visual mindmaps, and automatically generated FAQs.

### The Problem DecipherIt Solves

Traditional research is time-consuming and fragmented. Researchers often struggle with:

- **Information Overload**: Sifting through countless sources manually
- **Geo-restrictions**: Unable to access content from different regions
- **Bot Detection**: Getting blocked when trying to scrape valuable data
- **Synthesis Challenges**: Difficulty connecting insights across multiple sources
- **Accessibility**: Converting research into different formats for various audiences

DecipherIt addresses these challenges by leveraging **Bright Data's MCP Server** to provide unrestricted, intelligent web access combined with advanced AI agents that can understand, synthesize, and present information in multiple formats.

### 🎯 Key Features

- **🔬 Deep Research** - Conduct thorough research on any topic with AI-assisted analysis and synthesis
- **🔍 Multi-Source Research** - Seamlessly integrate documents, URLs, and manual text into unified research spaces
- **🤖 AI-Powered Summaries** - Generate comprehensive, well-structured research analyses using advanced AI agents
- **💬 Interactive Q&A** - Chat with your research materials using natural language queries
- **🎧 Audio Overviews** - AI-generated podcast-style audio summaries with multiple voices
- **❓ Smart FAQ Generation** - Automatically create relevant FAQs from your research content
- **🧠 Visual Mindmaps** - Generate interactive, hierarchical mindmaps to visualize research structure and connections
- **🌐 Global Web Access** - Bypass geo-restrictions and bot detection using Bright Data's infrastructure

### 🔍 Detailed Feature Overview

**🔬 Deep Research**
DecipherIt's AI agents conduct comprehensive research by strategically planning data collection, discovering diverse sources through Bright Data's global search capabilities, and synthesizing information from multiple perspectives. The system can research any topic from current events to academic subjects, providing thorough analysis that rivals human researchers.

**🔍 Multi-Source Research**
Users can combine various input types in a single research project: upload documents (PDF, DOCX, PPTX, XLSX), add custom URLs for specific web content, input manual text for direct analysis, or simply enter topics for AI-driven discovery. All sources are processed and integrated into a unified research space.

**🤖 AI-Powered Summaries**
Specialized CrewAI agents work together to create comprehensive research summaries. The Research Analyst synthesizes information from all sources, while the Content Writer crafts engaging, well-structured analyses that highlight key insights, trends, and connections across the research material.

**💬 Interactive Q&A**
Using vector embeddings and semantic search through Qdrant database, users can ask natural language questions about their research content. The system provides contextual answers by retrieving relevant information from all processed sources, enabling deep exploration of the research material.

**🎧 Audio Overviews**
On-demand feature that transforms research into engaging podcast-style audio content. The Podcast Script Generator agent creates conversational scripts, which are then converted to high-quality audio using LemonFox TTS with multiple AI voices, making research accessible in audio format.

**❓ Smart FAQ Generation**
AI agents automatically analyze research content to generate relevant, insightful questions and comprehensive answers. This feature helps users understand key aspects of their research topic and provides quick access to important information.

**🧠 Visual Mindmaps**
The Mindmap Creator agent analyzes research structure to generate interactive, hierarchical visualizations with up to 5 levels of depth. Built with react-mindmap-visualiser, these mindmaps help users understand complex topics at a glance and navigate research relationships visually.

**🌐 Global Web Access**
Powered by Bright Data's MCP Server, DecipherIt bypasses geo-restrictions and bot detection to access content from anywhere in the world. This ensures comprehensive research coverage and access to diverse, authoritative sources that traditional scraping methods cannot reach.

---

## 🏗️ Architecture

![DecipherIt drawio](https://github.com/user-attachments/assets/085c41aa-4cdc-400f-b6e0-af8cbce4c5a3)

---

## 🛠️ Tech Stack

### Frontend

- **[Next.js 15](https://nextjs.org/)** - React framework with App Router
- **[React 19](https://reactjs.org/)** - Latest React with concurrent features
- **[TypeScript 5](https://typescriptlang.org/)** - Type-safe development
- **[Tailwind CSS 4](https://tailwindcss.com/)** - Utility-first CSS framework
- **[Shadcn/ui](https://ui.shadcn.com/)** - Beautiful, accessible component library
- **[Radix UI](https://radix-ui.com/)** - Unstyled, accessible UI primitives
- **[Better Auth](https://better-auth.com/)** - Modern authentication solution
- **[Prisma](https://prisma.io/)** - Type-safe database ORM
- **[react-mindmap-visualiser](https://www.npmjs.com/package/react-mindmap-visualiser)** - Interactive mindmap visualization component
- **[pnpm](https://pnpm.io/)** - Fast, disk space efficient package manager

### Backend

- **[Python 3.12](https://python.org/)** - Latest Python with performance improvements
- **[FastAPI](https://fastapi.tiangolo.com/)** - High-performance async API framework
- **[CrewAI](https://crewai.com/)** - Multi-agent AI framework for complex tasks
- **[Qdrant](https://qdrant.tech/)** - Vector database for semantic search
- **[SQLAlchemy](https://sqlalchemy.org/)** - Python SQL toolkit and ORM
- **[Pydantic](https://pydantic.dev/)** - Data validation using Python type hints
- **[Loguru](https://loguru.readthedocs.io/)** - Simplified logging for Python
- **[uv](https://docs.astral.sh/uv/getting-started/installation/)** - Fast, disk space efficient package manager

### AI & ML Services

- **[Bright Data MCP Server](https://github.com/brightdata-com/brightdata-mcp)** - Official Model Context Protocol server for real-time web access, bypassing geo-restrictions and bot detection
- **[Google Gemini using OpenRouter](https://openrouter.ai/models/google/gemini-1.5-flash)** - Large language models for content generation
- **[OpenAI Embeddings](https://openai.com/)** - Text embeddings for semantic search
- **[LemonFox TTS](https://lemonfox.ai/)** - High-quality text-to-speech synthesis
- **[MarkItDown](https://github.com/microsoft/markitdown)** - Document conversion to Markdown

### Infrastructure & Storage

- **[Cloudflare R2](https://cloudflare.com/products/r2/)** - Object storage for files and audio
- **[PostgreSQL](https://postgresql.org/)** - Robust relational database
- **[Docker](https://docker.com/)** - Containerization for deployment

---

## 🚀 Installation

### Prerequisites

- **Node.js 20+** and **pnpm**
- **Python 3.12+** and **uv**
- **PostgreSQL 14+**
- **Docker** (optional, for containerized deployment)

### Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/mtwn105/decipher-research-agent.git
   cd decipher-research-agent
   ```

2. **Set up the frontend**

   ```bash
   cd client
   pnpm install
   cp .env.example .env.local
   # Configure your environment variables
   pnpm prisma generate
   pnpm prisma migrate dev
   ```

3. **Set up the backend**

   ```bash
   cd ../backend
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv sync
   cp .env.example .env
   # Configure your environment variables
   ```

4. **Start the development servers**

   ```bash
   # Terminal 1 - Frontend
   cd client && pnpm dev

   # Terminal 2 - Backend
   cd backend &&  uv run uvicorn server:app --host 0.0.0.0 --port 8001
   ```

### 🌐 Bright Data MCP Server Setup

DecipherIt uses the official **[Bright Data MCP Server](https://github.com/brightdata-com/brightdata-mcp)** for advanced web scraping capabilities. Follow these steps to set it up:

#### 1. Get Your Bright Data Account

- Sign up at [brightdata.com](https://brightdata.com) (new users get free credits)
- Navigate to your user settings page to get your API token

#### 2. Configure Web Unlocker (Automatic)

- By default, DecipherIt creates a Web Unlocker zone automatically using your API token
- For custom control, create your own Web Unlocker zone in the Bright Data control panel

#### 3. Web Unlocker Zone (Optional)

- For advanced use cases, you can create a custom Web Unlocker zone in your Bright Data control panel
- This provides more control over proxy settings and usage limits

#### 4. Integration Implementation

**Official MCP Server Integration**:

```python
from mcp import StdioServerParameters
from crewai_tools import MCPServerAdapter

server_params = StdioServerParameters(
    command="pnpm",
    args=["dlx", "@brightdata/mcp"],
    env={
        "API_TOKEN": os.environ["BRIGHT_DATA_API_TOKEN"],
        "BROWSER_AUTH": os.environ["BRIGHT_DATA_BROWSER_AUTH"]
    },
)
```

**Multi-Agent Workflow**:

```python
# Execute multiple scraping tasks in parallel
web_scraping_tasks = []
for link in links:
    web_scraping_tasks.append(
        web_scraping_crew.kickoff_async(inputs={
            "url": link.url,
            "current_time": current_time,
        })
    )

web_scraping_results = await asyncio.gather(*web_scraping_tasks)
```

#### 5. Security Best Practices

⚠️ **Important**: Always treat scraped web content as untrusted data. DecipherIt automatically:

- Filters and validates all web data before processing
- Uses structured data extraction rather than raw text
- Implements rate limiting and error handling

### Environment Variables

#### Frontend (.env.local)

```env
DATABASE_URL="postgresql://username:password@localhost:5432/decipher"
BETTER_AUTH_SECRET="your-auth-secret"
BETTER_AUTH_URL="http://localhost:3000"
R2_ENDPOINT="https://your-account-id.r2.cloudflarestorage.com"
R2_ACCESS_KEY_ID="your-r2-access-key"
R2_SECRET_ACCESS_KEY="your-r2-secret-key"
R2_BUCKET_NAME="decipher-files"
R2_PUBLIC_URL="https://files.decipherit.xyz"
NEXT_PUBLIC_BASE_URL="http://localhost:3000"
```

#### Backend (.env)

```env
# Database
DATABASE_URL="postgresql://username:password@localhost:5432/decipher"

# AI Services
OPENAI_API_KEY="your-openai-api-key"
OPENROUTER_API_KEY="your-openrouter-api-key"
LEMONFOX_API_KEY="your-lemonfox-api-key"

# Bright Data MCP Server
BRIGHT_DATA_API_TOKEN="your-bright-data-token"
BRIGHT_DATA_WEB_UNLOCKER_ZONE="your-web-unlocker-zone"  # Optional: custom zone name

# Vector Database
QDRANT_API_URL="http://localhost:6333"
QDRANT_API_KEY="your-qdrant-api-key"

# Cloud Storage
CLOUDFLARE_ACCOUNT_ID="your-cloudflare-account-id"
CLOUDFLARE_R2_ACCESS_KEY_ID="your-r2-access-key"
CLOUDFLARE_R2_SECRET_ACCESS_KEY="your-r2-secret-key"
```

---

## 🎯 Core Features

### 🔍 Intelligent Research Agents

DecipherIt employs specialized AI agents powered by **CrewAI** to handle different aspects of research:

#### CrewAI Crews Overview

DecipherIt employs a sophisticated multi-crew architecture powered by **CrewAI**:

- **Web Scraping Crew** - A crew of agents focused on data collection strategy and execution
- **Research Crew** - A crew dedicated to discovering and analyzing relevant sources using Bright Data
- **Content Processing Crew** - A crew that extracts and structures web content data
- **Analysis Crew** - A crew that synthesizes information from multiple research sources
- **Content Creation Crew** - A crew producing engaging, well-structured research summaries
- **FAQ Generation Crew** - A specialized crew generating relevant questions and answers
- **Visualization Crew** - A crew analyzing research to create hierarchical visual mindmaps

#### Individual Agent Roles

- **Web Scraping Planner** - Strategizes optimal data collection approaches
- **Link Collector Agent** - Uses `search_engine` to find relevant sources based on research topics
- **Web Scraper Agent** - Uses `scrape_as_markdown` to extract clean, structured content from discovered URLs
- **Research Analyst** - Synthesizes information from multiple sources
- **Content Writer** - Creates engaging, well-structured research summaries
- **FAQ Generator** - Automatically generates relevant questions and answers
- **Mindmap Creator** - Analyzes research content to create hierarchical visual mindmaps with up to 5 levels of depth

### 🌐 Advanced Web Scraping with Bright Data MCP

DecipherIt leverages the **[official Bright Data MCP Server](https://github.com/brightdata-com/brightdata-mcp)** - a powerful Model Context Protocol server that provides an all-in-one solution for public web access. This integration enables:

#### 🚀 Core Capabilities

- **Real-time Web Access** - Access up-to-date information directly from the web
- **Bypass Geo-restrictions** - Access content regardless of location constraints
- **Web Unlocker Technology** - Navigate websites with advanced bot detection protection
- **Browser Control** - Optional remote browser automation capabilities
- **Seamless Integration** - Works with all MCP-compatible AI assistants

#### 🛠️ Tools Used by DecipherIt

DecipherIt leverages two key tools from the Bright Data MCP server:

- `search_engine` - Search the web for relevant information and discover sources
- `scrape_as_markdown` - Extract and convert web content to clean, structured Markdown format

#### 🔒 Security & Reliability

- **Anti-Bot Detection** - Advanced techniques to avoid getting blocked
- **Residential Proxies** - Access content through real residential IP addresses
- **Rate Limiting** - Built-in protection against overuse
- **Data Validation** - Automatic filtering and validation of scraped content

This powerful integration allows DecipherIt's AI agents to conduct comprehensive research across the entire web without the typical limitations of traditional scraping methods.

### 🧠 Vector-Powered Search

Using **Qdrant vector database** and **OpenAI embeddings**:

- Semantic search through research content
- Intelligent content chunking for optimal retrieval
- Cross-reference information across multiple sources
- Context-aware question answering

### 🎧 AI-Generated Audio Overviews

Transform your research into engaging audio content:

- **LemonFox TTS** for high-quality voice synthesis
- Multiple AI voices for podcast-style conversations
- Automatic script generation from research content using **Podcast Script Generator** CrewAI agent
- Seamless audio file management with Cloudflare R2

#### How It Works

1. **Input Your Research Sources**: Enter any topic, upload documents, add custom URLs, or input manual text
2. **AI Planning**: The system creates a strategic research plan using specialized AI agents
3. **Web Discovery**: Bright Data's search engine finds relevant sources globally
4. **Intelligent Scraping**: Bright Data extracts content and converts it to clean markdown format
5. **AI Analysis**: Multiple AI agents analyze, synthesize, and create comprehensive summaries
6. **Multi-Format Output**: Get research summaries, FAQs, visual mindmaps, and podcast-style audio overviews

### 🧠 Interactive Visual Mindmaps

Transform complex research into visual hierarchical structures:

- **Intelligent Content Analysis** - AI agents analyze research to identify main themes and relationships
- **Hierarchical Structure Generation** - Creates up to 5 levels of depth based on content complexity
- **Interactive Visualization** - Built with react-mindmap-visualiser for smooth user experience
- **Adaptive Depth** - Automatically adjusts mindmap complexity based on research content richness
- **Real-time Generation** - Background processing with live status updates

#### AI Processing Pipeline

**Immediate Processing:**

- **Vector embeddings** created using OpenAI embeddings and stored in Qdrant for semantic search capabilities
- **Contextual analysis** by Research Analyst agents to synthesize information from multiple sources
- **Automatic FAQ generation** by analyzing content patterns and extracting key insights

**On-Demand Generation:**

- **Audio script creation** when users request podcast-style overviews, processed by specialized TTS agents
- **Mindmap structure analysis** for hierarchical visualization when users want visual representations
- **Interactive Q&A responses** powered by vector similarity search through processed content

### 📄 Document Processing

Comprehensive document support using **MarkItDown**:

- PDF, DOCX, PPTX, XLSX file processing
- Automatic text extraction and formatting
- Secure file storage with Cloudflare R2
- Metadata preservation and indexing

---

## 🐳 Docker Deployment

### Using Docker Compose

```yaml
version: "3.8"
services:
  frontend:
    build: ./client
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/decipher
    depends_on:
      - db
      - backend

  backend:
    build: ./backend
    ports:
      - "8001:8001"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/decipher
    depends_on:
      - db
      - qdrant

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=decipher
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "6333:6333"
    volumes:
      - qdrant_data:/qdrant/storage

volumes:
  postgres_data:
  qdrant_data:
```

### Build and Run

```bash
docker-compose up -d
```

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Created By

**Amit Wani**

- GitHub: [@mtwn105](https://github.com/mtwn105)
- LinkedIn: [Amit Wani](https://linkedin.com/in/mtwn105)
- Website: [linktr.ee/mtwn105](https://linktr.ee/mtwn105)

---

## 🙏 Acknowledgments

- **[Bright Data](https://brightdata.com/)** for their powerful [MCP Server](https://github.com/brightdata-com/brightdata-mcp) enabling real-time web access and advanced scraping capabilities
- **[CrewAI](https://crewai.com/)** for the multi-agent AI framework
- **[Qdrant](https://qdrant.tech/)** for vector database technology
- **[LemonFox](https://lemonfox.ai/)** for high-quality TTS services
- **[Cloudflare](https://cloudflare.com/)** for R2 storage and CDN
- **[Vercel](https://vercel.com/)** for seamless deployment
- **[OpenAI](https://openai.com/)** for GPT and embedding models
- **[OpenRouter](https://openrouter.ai/)** for OpenRouter API for Gemini

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by [Amit Wani](https://github.com/mtwn105)

</div>
