from pydantic import BaseModel, Field
from typing import Optional, List, Any, Literal
from datetime import datetime

class ResearchSource(BaseModel):
    source_type: Literal["URL", "MANUAL", "FILE"]
    source_url: Optional[str]
    source_content: Optional[str]


class ResearchRequest(BaseModel):
    notebook_id: str = Field(..., description="The notebook ID to use for the research. If not provided, the agent will create a new notebook.")
    topic: Optional[str] = Field(None, min_length=3, description="The research topic for the agent.")
    sources: Optional[List[ResearchSource]] = Field(None, description="The sources to use for the research. If not provided, the agent will use the default sources.")

class TaskResponse(BaseModel):
    task_id: str
    notebook_id: str
    status: str
    message: str

class TaskStatusResponse(BaseModel):
    task_id: str
    notebook_id: str
    topic: Optional[str]
    sources: Optional[List[ResearchSource]]
    status: str
    created_at: datetime
    result: Optional[Any] = None
    error: Optional[str] = None
    completed_at: Optional[datetime] = None
    failed_at: Optional[datetime] = None

class TaskListItem(BaseModel):
    task_id: str
    notebook_id: str
    topic: Optional[str]
    sources: Optional[List[ResearchSource]]
    status: str
    created_at: datetime
    completed_at: Optional[datetime] = None

class TaskList(BaseModel):
    tasks: List[TaskListItem]
    total: int