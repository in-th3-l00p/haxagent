from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from agent.models import HackathonRequest


SYSTEM_PROMPT = "You should index hackathons in the database"


def build_indexer_agent():
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


def run_indexer(request: HackathonRequest):
    agent = build_indexer_agent()
    return agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": request.to_prompt(),
                }
            ]
        }
    )
