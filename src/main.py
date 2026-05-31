from graphs.workflow import build_workflow

DEBUG = True


def main():
    app = build_workflow()

    initial_state = {
        "user_task": input("Enter your task: "),
        "plan": "",
        "research": "",
        "result": "",
        "validation": "",
        "retry_count": 0,
    }

    final_state = app.invoke(initial_state)

    if DEBUG:
        print("\n--- Planner Agent Output ---")
        print(final_state["plan"])

        print("\n--- Researcher Agent Output ---")
        print(final_state["research"])

        print("\n--- Executor Agent Output ---")
        print(final_state["result"])

        print("\n--- Validator Agent Output ---")
        print(final_state["validation"])

    else:
        print("\n=== Final Answer ===")
        print(final_state["result"])


if __name__ == "__main__":
    main()