import streamlit as st
from graphs.workflow import build_workflow


st.set_page_config(
    page_title="AgentFlow",
    page_icon="🤖",
    layout="wide",
)


st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
    }
    .card {
        padding: 20px;
        border-radius: 14px;
        background-color: #f8f9fa;
        border: 1px solid #e5e7eb;
        margin-bottom: 18px;
    }
    .card-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


with st.sidebar:
    st.title("🤖 AgentFlow")
    st.write("A multi-agent AI task runner using LangGraph and OpenAI.")

    st.divider()

    st.subheader("Workflow")
    st.write("1. Planner Agent")
    st.write("2. Researcher Agent")
    st.write("3. Executor Agent")
    st.write("4. Validator Agent")

    st.divider()

    st.subheader("Example Tasks")
    st.caption("Create a study plan for learning Python basics in one week")
    st.caption("Draft a project roadmap for an AI chatbot")
    st.caption("Break down a resume improvement plan")

    st.divider()

    show_debug = st.toggle("Show agent details", value=True)


st.markdown("<div class='main-title'>AgentFlow</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>A polished multi-agent AI workflow powered by LangGraph and OpenAI.</div>",
    unsafe_allow_html=True,
)


col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>Enter Your Task</div>", unsafe_allow_html=True)

    user_task = st.text_area(
        label="Task input",
        label_visibility="collapsed",
        placeholder="Example: Create a study plan for learning Python basics in one week",
        height=160,
    )

    run_button = st.button("Run AgentFlow", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown(
        """
        <div class='card'>
            <div class='card-title'>What This App Does</div>
            <p>AgentFlow separates a complex task into multiple AI agent responsibilities.</p>
            <p>Each agent contributes to the final answer using shared workflow state.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='card'>
            <div class='card-title'>Tech Stack</div>
            <p>Python</p>
            <p>LangGraph</p>
            <p>OpenAI API</p>
            <p>Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


if run_button:
    if not user_task.strip():
        st.warning("Please enter a task first.")
    else:
        with st.spinner("Running multi-agent workflow..."):
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

        st.success("Workflow completed successfully.")

        st.divider()

        st.markdown("## Final Answer")
        st.markdown(final_state["result"])

        st.markdown("## Validation")
        st.info(final_state["validation"])

        st.metric("Retry Count", final_state["retry_count"])

        if show_debug:
            st.divider()
            st.markdown("## Agent Details")

            with st.expander("Planner Agent"):
                st.markdown(final_state["plan"])

            with st.expander("Researcher Agent"):
                st.markdown(final_state["research"])

            with st.expander("Executor Agent"):
                st.markdown(final_state["result"])

            with st.expander("Validator Agent"):
                st.markdown(final_state["validation"])