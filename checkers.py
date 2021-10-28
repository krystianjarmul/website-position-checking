from abc import ABC, abstractmethod

from selenium import webdriver

from scrapers import AbstractScraper, SeleniumScraper, ChromeDriverSetup

DRIVER_PATH = "./chromedriver"


class AbstractPositionChecker(ABC):
    def __init__(self, scraper: AbstractScraper):
        self.scraper = scraper

    @abstractmethod
    def search(self, query: str):
        """Open browser and search for a query."""

    @abstractmethod
    def get_position(self, url: str) -> int:
        """Gets position of website based on passed url."""


class GooglePositionChecker(AbstractPositionChecker):

    def __init__(self, scraper):
        super().__init__(scraper)
        self.search_url = "https://www.google.com/search?q="

    def search(self, query: str):
        self.scraper.get(self.search_url + query)

    def get_position(self, url):
        rso = self.scraper.find_element_by_id("rso")
        urls = [
            g.find_element_by_tag("a").get_attribute("href")
            for g in rso.find_elements_by_class("g")
        ]
        return urls.index(url)


def get_site_position_from_google(query: str, website_url: str) -> int:
    driver_settings = ChromeDriverSetup(DRIVER_PATH)
    driver = webdriver.Chrome(**driver_settings.get_configs())
    scraper = SeleniumScraper(driver)

    position_checker = GooglePositionChecker(scraper)
    position_checker.search(query)
    return position_checker.get_position(website_url)


if __name__ == '__main__':
    position = get_site_position_from_google(
        query="travatar",
        website_url="https://travatar.ai/"
    )
