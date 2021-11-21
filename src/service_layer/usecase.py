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
    driver.get(f"{server}{query}")
    container = driver.find_element("id", "rso")
    container_items = container.find_elements(By("class"), "g")

    page = Page()
    for item in container_items:
        title = item.find_element(By("tag"), "h3")
        hyperlink = item.find_element(By("tag"), "a")
        url = hyperlink.get_attribute("href")

        result = Result(title=title.text, url=url)
        page.add_result(result)

    position = page.get_website_position(website)

    return position
