from src.adapters.driver import FakeDriver
from src.service_layer.usecase import get_website_position


def test_get_website_position_success(html):
    driver = FakeDriver(html)

    position = get_website_position(
        website="https://travatar.ai/",
        query="travatar",
        driver=driver
    )

    assert position == 1


def test_get_website_position_failed_if_website_not_in_results(html):
    driver = FakeDriver(html)

    position = get_website_position(
        website="https://ratavart.ai/",
        query="ratavart",
        driver=driver
    )

    assert position == -1
