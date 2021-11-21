from src.domain.model import Result
from src.adapters.repository import FakeResultsRepository
from src.service_layer.usecase import get_website_position

TEST_URL = "http://127.0.0.1:1938/"


def test_get_website_position_success():
    repo = FakeResultsRepository([
        Result(title="Other", url="https://other.ai/"),
        Result(title="Travatar", url="https://travatar.ai/"),
        Result(title="Another", url="https://another.ai/"),
    ])

    position = get_website_position(
        website="https://travatar.ai/",
        query="travatar",
        repo=repo
    )

    assert position == 1


def test_get_website_position_failed_if_website_not_in_results():
    repo = FakeResultsRepository([
        Result(title="Other", url="https://other.ai/"),
        Result(title="No-travatar", url="https://notravatar.ai/"),
        Result(title="Another", url="https://another.ai/"),
    ])

    position = get_website_position(
        website="https://travatar.ai/",
        query="travatar",
        repo=repo
    )

    assert position == -1

# cannot connect to server, server is down


# website is on another page
