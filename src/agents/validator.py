from utils.llm import call_llm
from utils.state import AgentState


def validator_agent(state: AgentState) -> AgentState:
    prompt = f"""
You are the Validator Agent.

Review whether the final output satisfies the user's task.

User task:
{state["user_task"]}

Final output:
{state["result"]}

Return your response in this exact format:

Validation result: PASS or NEEDS IMPROVEMENT
Explanation: short explanation
Suggested improvements: short suggestions
"""

    state["validation"] = call_llm(prompt)
    return state