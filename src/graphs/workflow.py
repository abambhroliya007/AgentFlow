from langgraph.graph import StateGraph, END

from utils.state import AgentState
from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.executor import executor_agent
from agents.validator import validator_agent


def should_continue(state: AgentState) -> str:
    validation = state["validation"].lower()

    if "needs improvement" in validation and state["retry_count"] < 1:
        return "retry"

    return "end"


def increment_retry(state: AgentState) -> AgentState:
    state["retry_count"] += 1
    return state


def build_workflow():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_agent)
    graph.add_node("researcher", researcher_agent)
    graph.add_node("executor", executor_agent)
    graph.add_node("validator", validator_agent)
    graph.add_node("increment_retry", increment_retry)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "executor")
    graph.add_edge("executor", "validator")

    graph.add_conditional_edges(
        "validator",
        should_continue,
        {
            "retry": "increment_retry",
            "end": END,
        },
    )

    graph.add_edge("increment_retry", "executor")

    return graph.compile()