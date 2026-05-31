from typing import TypedDict


class AgentState(TypedDict):
    user_task: str
    plan: str
    research: str
    result: str
    validation: str
    retry_count: int