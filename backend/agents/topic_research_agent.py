from crewai import Agent, Crew, Task, Process, LLM
from mcp import StdioServerParameters
from crewai_tools import MCPServerAdapter
import os
import logging
from datetime import datetime
from models import BlogTaskResult
from config import llm, TOPIC_RESEARCH_AGENT_CONFIGS, TOPIC_RESEARCH_TASK_CONFIGS
from typing import List
server_params = StdioServerParameters(
    command="pnpm",
    args=["dlx", "@brightdata/mcp"],
    env={"API_TOKEN": os.environ["BRIGHT_DATA_API_TOKEN"]},
)

# Initialize MCPAdapt with CrewAI adapter
async def run_research_crew(topic):
    with MCPServerAdapter(server_params) as tools:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create agents
        web_scraper = Agent(
            role=TOPIC_RESEARCH_AGENT_CONFIGS["web_scraper"]["role"],
            goal=TOPIC_RESEARCH_AGENT_CONFIGS["web_scraper"]["goal"],
            backstory=TOPIC_RESEARCH_AGENT_CONFIGS["web_scraper"]["backstory"],
            verbose=True,
            tools=tools,
            llm=llm,
            max_iter=50,
        )

        researcher = Agent(
            role=TOPIC_RESEARCH_AGENT_CONFIGS["researcher"]["role"],
            goal=TOPIC_RESEARCH_AGENT_CONFIGS["researcher"]["goal"],
            backstory=TOPIC_RESEARCH_AGENT_CONFIGS["researcher"]["backstory"],
            verbose=True,
            llm=llm,
        )

        content_writer = Agent(
            role=TOPIC_RESEARCH_AGENT_CONFIGS["content_writer"]["role"],
            goal=TOPIC_RESEARCH_AGENT_CONFIGS["content_writer"]["goal"],
            backstory=TOPIC_RESEARCH_AGENT_CONFIGS["content_writer"]["backstory"],
            verbose=True,
            llm=llm,
        )

        # Create tasks
        web_scraping_task = Task(
            description=TOPIC_RESEARCH_TASK_CONFIGS["web_scraping"]["description"],
            expected_output=TOPIC_RESEARCH_TASK_CONFIGS["web_scraping"]["expected_output"],
            agent=web_scraper,
            max_retries=5,
            # output_pydantic=WebScrapingTaskResult
        )

        research_task = Task(
            description=TOPIC_RESEARCH_TASK_CONFIGS["research_analysis"]["description"],
            expected_output=TOPIC_RESEARCH_TASK_CONFIGS["research_analysis"]["expected_output"],
            agent=researcher,
            context=[web_scraping_task],
            max_retries=5,
            # output_pydantic=ResearchTaskResult
        )

        content_task = Task(
            description=TOPIC_RESEARCH_TASK_CONFIGS["content_creation"]["description"],
            expected_output=TOPIC_RESEARCH_TASK_CONFIGS["content_creation"]["expected_output"],
            agent=content_writer,
            context=[research_task],
            max_retries=5,
            output_pydantic=BlogTaskResult
        )

        # Create and run the crew
        crew = Crew(
            agents=[web_scraper, researcher, content_writer],
            tasks=[web_scraping_task, research_task, content_task],
            verbose=True,
            process=Process.sequential,
        )

        result = crew.kickoff(inputs={
            "topic": topic,
            "current_time": current_time
        })

        # Tasks results
        # web_scraping_result = web_scraping_task.output
        # research_result = research_task.output
        # content_result = content_task.output

        # Log the results
        logging.info(f"Crew result: {result['content']}")
        # logging.info(f"Web scraping result: {web_scraping_result}")
        # logging.info(f"Research result: {research_result}")
        # logging.info(f"Content result: {content_result}")

        return result