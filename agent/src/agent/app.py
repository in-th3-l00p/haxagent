import sys

from agent.agents.indexer import run_indexer
from agent.models import HackathonRequest
from agent.utils import ensure_openai_api_key, load_dotenv


def build_default_request() -> HackathonRequest:
    return HackathonRequest(
        name="Hack the Future",
        date="2024-07-15",
        location="San Francisco",
    )


def main() -> int:
    load_dotenv()

    try:
        ensure_openai_api_key()
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    request = build_default_request()
    result = run_indexer(request)
    print(result)
    return 0
