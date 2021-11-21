from src.adapters.repository import AbstractResultsRepository
from src.domain.model import Page

GOOGLE_SEARCH_URL = "https://www.google.com/search?q="
CHROMEDRIVER_PATH = "bin/chromedriver"


def get_website_position(
        website: str, query: str, repo: AbstractResultsRepository,
) -> int:
    """
    Scrapes a google's search results page for given query
    and returns a position of given website.
    """
    page = Page([result for result in repo.list(query)])

    position = page.get_website_position(website)

    return position
