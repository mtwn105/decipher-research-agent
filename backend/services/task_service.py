import asyncio
from typing import Dict, Optional, List, Any
from loguru import logger

from agents import topic_research_agent
from models.db import NotebookProcessingStatusValue
from .task_repository import task_repository
from .notebook_repository import notebook_repository

class TaskManager:

    async def _execute_task(self, task_id: str, topic: Optional[str], notebook_id: str, sources: Optional[List] = None):
        """Internal method to run the research task and update status."""
        max_retries = 1
        retry_count = 0

        await notebook_repository.update_notebook_status(
            notebook_id,
            NotebookProcessingStatusValue.IN_PROGRESS,
            "Research task started"
        )

        while retry_count < max_retries:
            try:

                await task_repository.update_task_status(task_id, "running")

                logger.info(f"Task {task_id} started for notebook: {notebook_id}" +
                           (f" on topic: {topic}" if topic else "") +
                           (f" (retry {retry_count}/{max_retries-1})" if retry_count > 0 else ""))

                with logger.contextualize(task_id=task_id):
                    if topic and topic != "" and (sources and len(sources) > 0):
                        logger.warning("Topic and sources research not implemented yet")
                        return
                    elif topic and topic != "" and (not sources or len(sources) == 0):
                        # Run topic research agent
                        result = await topic_research_agent.run_research_crew(topic)
                        # Save notebook output
                        await notebook_repository.save_notebook_output(notebook_id, result["blog_post"])

                        # # Save sources
                        # await notebook_repository.save_notebook_sources(notebook_id, result["scraped_data"])

                        # Update notebook title and topic
                        title = result["title"]
                        await notebook_repository.update_notebook(
                            notebook_id,
                            title=title,
                            topic=topic
                        )
                    elif  sources and len(sources) > 0:
                        logger.error("Sources research not implemented yet")
                        return
                    else:
                        logger.error("No topic or sources provided")
                        return


                await task_repository.update_task_result(task_id, result, "completed")

                await notebook_repository.update_notebook_status(
                    notebook_id,
                    NotebookProcessingStatusValue.PROCESSED,
                    "Research completed successfully"
                )

                logger.success(f"Task {task_id} completed successfully")
                return

            except Exception as e:
                retry_count += 1
                # Log the error but keep retrying if we haven't hit the limit
                if retry_count < max_retries:
                    logger.warning(f"Task {task_id} failed (attempt {retry_count}/{max_retries-1}): {e}")
                    continue

                logger.opt(exception=True).error(f"Task {task_id} failed after {retry_count} attempts: {e}")

                await task_repository.update_task_error(task_id, str(e))

                await notebook_repository.update_notebook_status(
                    notebook_id,
                    NotebookProcessingStatusValue.ERROR,
                    f"Research failed. Please try again."
                )

                return

    async def submit_task_async(self, notebook_id: str, topic: Optional[str] = None, sources: Optional[List] = None) -> str:
        """Async implementation for submitting a new research task."""

        task_id = await task_repository.create_task(notebook_id, topic, sources)

        asyncio.create_task(self._execute_task(task_id, topic, notebook_id, sources))

        logger.info(f"Task {task_id} submitted for notebook: {notebook_id}" + (f" on topic: {topic}" if topic else ""))
        return task_id

# Singleton instance
task_manager = TaskManager()