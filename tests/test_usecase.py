from lib.driver import Driver
from src.adapters.repository import GoogleResultsRepository
from src.service_layer.usecase import get_website_position

TEST_URL = "http://127.0.0.1:1938/"
CHROMEDRIVER_PATH = "bin/chromedriver"

driver = Driver(CHROMEDRIVER_PATH)


def test_get_website_position_success(google_mock):
    repo = GoogleResultsRepository(driver=driver, search_url=TEST_URL)
    position = get_website_position(
        website="https://travatar.ai/", query="travatar", repo=repo
    )

    assert position == 1


def test_get_website_position_failed_if_website_not_in_results(google_mock):
    repo = GoogleResultsRepository(driver=driver, search_url=TEST_URL)
    position = get_website_position(
        website="https://another.ai/", query="travatar", repo=repo
    )

    assert position == -1

# cannot connect to server, server is down


# website is on another page
