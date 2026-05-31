from utils.llm import call_llm
from utils.state import AgentState


def researcher_agent(state: AgentState) -> AgentState:
    prompt = f"""
You are the Researcher Agent.

Identify useful background information and assumptions.

User task:
{state["user_task"]}

Plan:
{state["plan"]}
"""

    state["research"] = call_llm(prompt)
    return state