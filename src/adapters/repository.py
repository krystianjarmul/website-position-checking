from __future__ import annotations

from abc import abstractmethod, ABC
from typing import List

from lib.driver import By
from src.domain.model import Result

GOOGLE_SEARCH_URL = "https://www.google.com/search?q="


class AbstractResultsRepository(ABC):
    """Abstract repository class for results."""

    @abstractmethod
    def list(self, query: str) -> List[Result]:
        ...


class GoogleResultsRepository(AbstractResultsRepository):
    """Repository class for results scraped from google searching."""

    def __init__(self, driver, search_url: str = GOOGLE_SEARCH_URL):
        self._driver = driver
        self._search_url = search_url

    def list(self, query):
        self._driver.get(f"{self._search_url}{query}")

        container = self._driver.find_element(By.ID, "rso")
        container_items = container.find_elements(By.CLASS_NAME, "g")

        results = []
        for item in container_items:
            title = item.find_element(By.TAG_NAME, "h3").get_attribute("text")
            url = item.find_element(By.TAG_NAME, "a").get_attribute("href")
            result = Result(title, url)
            results.append(result)
        return results


class FakeResultsRepository(AbstractResultsRepository):

    def __init__(self, results=None):
        if results is None:
            results = []
        self.results = results

    def list(self, query):
        return self.results
