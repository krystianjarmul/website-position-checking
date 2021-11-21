from src.adapters.driver import AbstractDriver, By
from src.domain.model import Result, Page

GOOGLE_SEARCH_URL = "https://www.google.com/search?q="
CHROMEDRIVER_PATH = "bin/chromedriver"


def get_website_position(
        query: str,
        website: str,
        driver: AbstractDriver,
        server: str = GOOGLE_SEARCH_URL,
) -> int:
    page = Page()

    driver.get(f"{server}{query}")
    container = driver.find_element(By.ID, "rso")
    container_items = container.find_elements(By.CLASS_NAME, "g")

    for item in container_items:
        result = Result(
            title=item.find_element(By.TAG_NAME, "h3").get_attribute("text"),
            url=item.find_element(By.TAG_NAME, "a").get_attribute("href")
        )
        page.add_result(result)

    position = page.get_website_position(website)

    return position
