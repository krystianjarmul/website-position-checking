from src.service_layer.usecase import get_website_position

TEST_URL = "http://127.0.0.1:1938/"
CHROMEDRIVER_PATH = "bin/chromedriver"


def test_get_website_position_success(google_mock):
    position = get_website_position(
        query="travatar",
        website="https://travatar.ai/",
        server=TEST_URL,
        chromedriver_path=CHROMEDRIVER_PATH
    )

    assert position == 1


def test_get_website_position_failed_if_website_not_in_results(google_mock):
    position = get_website_position(
        query="travatar",
        website="https://another.ai/",
        server=TEST_URL,
        chromedriver_path=CHROMEDRIVER_PATH
    )

    assert position == -1

# cannot connect to server, server is down


# website is on another page
