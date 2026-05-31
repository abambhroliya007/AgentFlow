import time

import streamlit as st

from graphs.workflow import build_workflow


st.set_page_config(
    page_title="AgentFlow",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
<style>
header {
    visibility: hidden;
}

.block-container {
    padding-top: 1rem;
    max-width: 1200px;
}

.stApp {
    background: #0f172a;
}

[data-testid="stSidebar"] {
    background: #020617;
}

h1, h2, h3, h4, h5, h6, p, div, span, label {
    color: #f8fafc !important;
}

.hero {
    background: linear-gradient(135deg, #2563eb, #7c3aed, #ec4899);
    padding: 32px;
    border-radius: 24px;
    margin-bottom: 24px;
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.25);
}

.hero-title {
    font-size: 52px;
    font-weight: 900;
    margin-bottom: 14px;
}

.hero-subtitle {
    font-size: 18px;
    line-height: 1.5;
    max-width: 850px;
}

.badge {
    display: inline-block;
    background: rgba(255,255,255,0.2);
    padding: 9px 16px;
    border-radius: 999px;
    margin-right: 10px;
    margin-top: 18px;
    font-weight: 800;
    font-size: 14px;
}

.metric-card {
    padding: 22px;
    border-radius: 18px;
    background: rgba(17, 24, 39, 0.95);
    border: 1px solid rgba(148, 163, 184, 0.2);
    transition: all 0.3s ease;
    min-height: 145px;
    margin-bottom: 18px;
}

.metric-card:hover {
    transform: translateY(-4px);
    border-color: rgba(139, 92, 246, 0.55);
    box-shadow: 0 16px 35px rgba(139, 92, 246, 0.18);
}

.metric-icon {
    font-size: 32px;
    margin-bottom: 10px;
}

.metric-title {
    color: #94a3b8 !important;
    font-size: 14px;
    font-weight: 700;
}

.metric-value {
    font-size: 27px;
    font-weight: 900;
    color: white !important;
    margin-top: 6px;
    white-space: nowrap;
}

.metric-sub {
    color: #22c55e !important;
    font-size: 13px;
    margin-top: 8px;
    font-weight: 600;
}

.step {
    background: #1e293b;
    border-left: 4px solid #8b5cf6;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
}

.result-box {
    background: #111827;
    border: 1px solid #334155;
    padding: 18px;
    border-radius: 16px;
    margin-top: 16px;
}

textarea {
    background: #020617 !important;
    color: #f8fafc !important;
    border: 1px solid #475569 !important;
    border-radius: 12px !important;
}

div.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #ec4899);
    color: white !important;
    border: none;
    border-radius: 10px;
    font-weight: 800;
    height: 46px;
}

div.stButton > button:hover {
    border: none;
    color: white !important;
}

[data-testid="stExpander"] {
    background: #111827;
    border: 1px solid #334155;
    border-radius: 12px;
}
</style>
""",
    unsafe_allow_html=True,
)


with st.sidebar:
    st.title("🤖 AgentFlow")
    st.write("Multi-Agent AI Task Runner powered by LangGraph and OpenAI.")

    st.divider()

    st.subheader("Agents")
    st.write("🧠 Planner")
    st.write("🔎 Researcher")
    st.write("⚙️ Executor")
    st.write("✅ Validator")

    st.divider()

    st.subheader("Examples")
    example_1 = st.button("📘 Python study plan", use_container_width=True)
    example_2 = st.button("🚀 AI project roadmap", use_container_width=True)
    example_3 = st.button("📝 Resume improvement", use_container_width=True)

    st.divider()

    show_debug = st.toggle("Show agent details", value=False)


default_task = ""

if example_1:
    default_task = "Create a study plan for learning Python basics in one week"
elif example_2:
    default_task = "Create a roadmap for building an AI chatbot project"
elif example_3:
    default_task = "Create a resume improvement plan for a junior AI engineer role"


st.markdown(
    """
<div class="hero">
    <div class="hero-title">🤖 AgentFlow</div>
    <div class="hero-subtitle">
        AI-powered multi-agent workflow orchestration with planning,
        research, execution, and validation agents.
    </div>
    <span class="badge">LangGraph</span>
    <span class="badge">OpenAI API</span>
    <span class="badge">Multi-Agent AI</span>
    <span class="badge">Streamlit</span>
</div>
""",
    unsafe_allow_html=True,
)


c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-icon">👥</div>
            <div class="metric-title">Agents</div>
            <div class="metric-value">4</div>
            <div class="metric-sub">Active agents</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-icon">🔀</div>
            <div class="metric-title">Workflow</div>
            <div class="metric-value">LangGraph</div>
            <div class="metric-sub">Orchestration</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-icon">🔁</div>
            <div class="metric-title">Retry Loop</div>
            <div class="metric-value">Enabled</div>
            <div class="metric-sub">Self-correcting</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c4:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-icon">⚡</div>
            <div class="metric-title">Platform</div>
            <div class="metric-value">Streamlit</div>
            <div class="metric-sub">Interactive UI</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


left, right = st.columns([2, 1], gap="large")

with left:
    st.subheader("Enter Your Task")

    user_task = st.text_area(
        "Task",
        value=default_task,
        placeholder="Example: Create a study plan for learning Python basics in one week",
        height=150,
        label_visibility="collapsed",
    )

    run_button = st.button("🚀 Run AgentFlow", use_container_width=True)

with right:
    st.subheader("How It Works")

    st.markdown(
        """
<div class="step">1. Planner breaks down the task</div>
<div class="step">2. Researcher gathers context</div>
<div class="step">3. Executor creates the answer</div>
<div class="step">4. Validator checks quality</div>
""",
        unsafe_allow_html=True,
    )


if run_button:
    if not user_task.strip():
        st.warning("Please enter a task first.")
    else:
        progress = st.progress(0)
        status_text = st.empty()

        steps = [
            "🧠 Planner Agent is creating a plan...",
            "🔎 Researcher Agent is gathering context...",
            "⚙️ Executor Agent is generating the answer...",
            "✅ Validator Agent is checking the output...",
        ]

        for index, step in enumerate(steps, start=1):
            status_text.info(step)
            progress.progress(index * 20)
            time.sleep(0.25)

        with st.spinner("Running workflow..."):
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

        progress.progress(100)
        status_text.success("Workflow completed.")

        st.divider()

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("🎯 Final Answer")
        st.markdown(final_state["result"])
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("✅ Validation")
        st.info(final_state["validation"])
        st.caption(f"Retry count: {final_state['retry_count']}")
        st.markdown("</div>", unsafe_allow_html=True)

        if show_debug:
            st.divider()
            st.subheader("Agent Details")

            with st.expander("🧠 Planner Agent"):
                st.write(final_state["plan"])

            with st.expander("🔎 Researcher Agent"):
                st.write(final_state["research"])

            with st.expander("⚙️ Executor Agent"):
                st.write(final_state["result"])

            with st.expander("✅ Validator Agent"):
                st.write(final_state["validation"])