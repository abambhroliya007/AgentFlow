# AgentFlow

A lightweight multi-agent AI task runner built with Python, LangGraph, and the OpenAI API.

AgentFlow demonstrates how specialized AI agents can collaborate through an orchestrated workflow to solve complex tasks more reliably than a single prompt-based approach.

---

## Overview

Traditional AI applications often rely on a single prompt to perform planning, reasoning, execution, and validation simultaneously. This can lead to inconsistent results and missed requirements.

AgentFlow addresses this by separating responsibilities across specialized AI agents:

* Planner Agent
* Researcher Agent
* Executor Agent
* Validator Agent

Each agent performs a focused task and passes structured information to the next stage through a shared state managed by LangGraph.

---

## Features

* Multi-agent AI architecture
* Planner Agent for task decomposition
* Researcher Agent for gathering context and assumptions
* Executor Agent for generating final solutions
* Validator Agent for quality assurance
* Shared state management using TypedDict
* LangGraph workflow orchestration
* Conditional retry loop for self-correction
* OpenAI API integration
* Modular and extensible design

---

## Architecture

```text
User Task
    │
    ▼
Planner Agent
    │
    ▼
Researcher Agent
    │
    ▼
Executor Agent
    │
    ▼
Validator Agent
    │
 ┌──┴─────────────┐
 │                │
 ▼                ▼
PASS         NEEDS IMPROVEMENT
 │                │
 ▼                │
END               │
 ▲                │
 └──── Retry ─────┘
```

---

## Workflow

### Step 1: Planner Agent

Analyzes the user task and creates a structured execution plan.

### Step 2: Researcher Agent

Identifies relevant context, assumptions, resources, and supporting information.

### Step 3: Executor Agent

Uses the plan and research notes to generate the final output.

### Step 4: Validator Agent

Evaluates the result for:

* Completeness
* Clarity
* Accuracy
* Requirement coverage

If improvements are needed, the workflow can route execution back through the Executor Agent.

---

## Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Core development language       |
| OpenAI API    | LLM-powered agents              |
| LangGraph     | Workflow orchestration          |
| python-dotenv | Environment variable management |
| Git & GitHub  | Version control                 |

---

## Project Structure

```text
AgentFlow/
│
├── README.md
├── requirements.txt
├── .gitignore
│
└── src/
    │
    ├── main.py
    │
    ├── agents/
    │   ├── planner.py
    │   ├── researcher.py
    │   ├── executor.py
    │   └── validator.py
    │
    ├── graphs/
    │   └── workflow.py
    │
    └── utils/
        ├── llm.py
        └── state.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AgentFlow.git
cd AgentFlow
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Run the Application

```bash
python src/main.py
```

Example:

```text
Enter your task:
Create a study plan for learning Python basics in one week
```

The workflow will automatically:

1. Create a plan
2. Research supporting information
3. Generate the final response
4. Validate the result

---

## Example Use Cases

* Study plan generation
* Research assistance
* Task decomposition
* Content generation
* Workflow automation
* AI orchestration experiments

---

## Future Improvements

* Streamlit web interface
* Real-time response streaming
* External search tools
* Memory-enabled agents
* Multi-model support
* LangSmith observability
* Agent performance metrics
* Docker deployment

---

## What I Learned

This project helped me understand:

* Multi-agent AI system design
* Agent orchestration with LangGraph
* Shared state management
* Prompt engineering
* Validation and retry workflows
* OpenAI API integration
* Building modular AI applications

---

## Author

**Ayush Bambhroliya**

Graduate Student – Computer Science
California State University, Sacramento

GitHub: https://github.com/abambhroliya007
