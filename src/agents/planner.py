from utils.llm import call_llm
from utils.state import AgentState


def planner_agent(state: AgentState) -> AgentState:
    prompt = f"""
You are the Planner Agent.

Break the user's task into clear numbered steps.

User task:
{state["user_task"]}
"""

    state["plan"] = call_llm(prompt)
    return state