from src.adapters.driver import By, AbstractDriver
from src.domain.model import Page, Result

GOOGLE_SEARCH_URL = "https://www.google.com/search?q="


def get_website_position(
        website: str,
        query: str,
        driver: AbstractDriver,
        search_url: str = GOOGLE_SEARCH_URL
) -> int:
    """
    Scrapes a google's search results page for given query
    and returns a position of given website.
    """
    driver.get(f"{search_url}{query}")

    container = driver.find_element(By.ID, "rso")
    container_items = container.find_elements(By.CLASS_NAME, "g")

    results = []
    for item in container_items:
        title = item.find_element(By.TAG_NAME, "h3").get_attribute("text")
        url = item.find_element(By.TAG_NAME, "a").get_attribute("href")
        result = Result(title, url)
        results.append(result)

    page = Page(results)
    position = page.get_website_position(website)

    return position
