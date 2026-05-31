import streamlit as st
from graphs.workflow import build_workflow


st.set_page_config(
    page_title="AgentFlow",
    page_icon="🤖",
    layout="wide",
)

st.title("AgentFlow")
st.subheader("Multi-Agent AI Task Runner")

st.write(
    "AgentFlow uses specialized AI agents for planning, research, execution, and validation."
)

user_task = st.text_area(
    "Enter a task",
    placeholder="Example: Create a study plan for learning Python basics in one week",
    height=120,
)

show_debug = st.checkbox("Show agent reasoning steps", value=True)

if st.button("Run AgentFlow"):
    if not user_task.strip():
        st.warning("Please enter a task first.")
    else:
        with st.spinner("Agents are working..."):
            app = build_workflow()

            initial_state = {
                "user_task": user_task,
                "plan": "",
                "research": "",
                "result": "",
                "validation": "",
                "retry_count": 0,
            }

            final_state = app.invoke(initial_state)

        st.success("Workflow completed!")

        st.header("Final Answer")
        st.write(final_state["result"])

        st.header("Validation")
        st.write(final_state["validation"])

        st.info(f"Retry Count: {final_state['retry_count']}")

        if show_debug:
            st.divider()

            st.header("Agent Workflow Details")

            with st.expander("Planner Agent Output"):
                st.write(final_state["plan"])

            with st.expander("Researcher Agent Output"):
                st.write(final_state["research"])

            with st.expander("Executor Agent Output"):
                st.write(final_state["result"])

            with st.expander("Validator Agent Output"):
                st.write(final_state["validation"])