import os
import sys
from pathlib import Path

SYSTEM_PROMPT = "You should index hackathons in the database"
USER_PROMPT = (
    "index the hackathon 'Hack the Future' happening on 2024-07-15 in San Francisco."
)


def load_dotenv(dotenv_path: str = ".env") -> None:
    path = Path(dotenv_path)
    if not path.exists():
        return

    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        os.environ.setdefault(key, value)


def build_agent():
    from langchain.agents import create_agent
    from langchain.chat_models import init_chat_model

    model = init_chat_model(
        "gpt-5.4-mini",
        temperature=0.5,
        timeout=10,
        max_tokens=2048,
    )

    return create_agent(
        model=model,
        tools=[],
        system_prompt=SYSTEM_PROMPT,
    )


def main():
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        print(
            "OPENAI_API_KEY is not set. Add it to `.env` or export it before running `uv run main.py`.",
            file=sys.stderr,
        )
        return 1

    agent = build_agent()
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": USER_PROMPT,
                }
            ]
        }
    )
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
