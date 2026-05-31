from utils.llm import call_llm
from utils.state import AgentState


def executor_agent(state: AgentState) -> AgentState:
    prompt = f"""
You are the Executor Agent.

Complete the task using the plan and research notes.

User task:
{state["user_task"]}

Plan:
{state["plan"]}

Research:
{state["research"]}
"""

    state["result"] = call_llm(prompt)
    return state