from __future__ import annotations
from abc import ABC, abstractmethod

from selenium.webdriver.common.by import By
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService


class AbstractDriverSetup(ABC):

    def get_options(self) -> ArgOptions:
        """Returns a webdriver options instance."""

    def get_service(self) -> Service:
        """Returns a webdriver service instance."""

    def get_configs(self) -> dict:
        return {"options": self.get_options(), "service": self.get_service()}


class AbstractScraper(ABC):

    @abstractmethod
    def get(self, url):
        """Load a page content based on url"""

    @abstractmethod
    def find_element_by_id(self, id_: str) -> AbstractElement:
        """Returns an web element based on given id."""

    @abstractmethod
    def find_element_by_class(self, class_: str) -> AbstractElement:
        """Returns an web element based on given class name."""

    @abstractmethod
    def find_elements_by_class(self, class_: str) -> AbstractElement:
        """Returns an web elements based on given class name."""

    @abstractmethod
    def find_element_by_tag(self, tag: str) -> AbstractElement:
        """Returns an web element based on given tag name."""

    @abstractmethod
    def find_elements_by_tag(self, tag: str) -> AbstractElement:
        """Returns an web elements based on given tag name."""


class AbstractElement(ABC):

    @abstractmethod
    def __iter__(self):
        """Iterates over all elements."""

    @abstractmethod
    def get_attribute(self, name: str) -> str:
        """Load a page content based on url"""

    @abstractmethod
    def find_element_by_id(self, id_: str) -> AbstractElement:
        """Returns an web element based on given id."""

    @abstractmethod
    def find_element_by_class(self, class_: str) -> AbstractElement:
        """Returns an web element based on given class name."""

    @abstractmethod
    def find_elements_by_class(self, class_: str) -> AbstractElement:
        """Returns an web elements based on given class name."""

    @abstractmethod
    def find_element_by_tag(self, tag: str) -> AbstractElement:
        """Returns an web element based on given tag name."""

    @abstractmethod
    def find_elements_by_tag(self, tag: str) -> AbstractElement:
        """Returns an web elements based on given tag name."""


class ChromeDriverSetup(AbstractDriverSetup):

    def __init__(self, driver_path: str):
        self.options = ChromeOptions()
        self.service = ChromeService(driver_path)

    def get_options(self):
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--headless")
        return self.options

    def get_service(self):
        return self.service


class SeleniumScraper(AbstractScraper):

    def __init__(self, browser):
        self.browser = browser

    def get(self, url):
        self.browser.get(url)

    def find_element_by_id(self, id_) -> SeleniumElement:
        return SeleniumElement(self.browser.find_element(By.ID, id_))

    def find_element_by_class(self, class_) -> SeleniumElement:
        return SeleniumElement(
            self.browser.find_element(By.CLASS_NAME, class_)
        )

    def find_elements_by_class(self, class_) -> SeleniumElement:
        return SeleniumElement(
            self.browser.find_elements(By.CLASS_NAME, class_)
        )

    def find_element_by_tag(self, tag) -> SeleniumElement:
        return SeleniumElement(self.browser.find_element(By.TAG_NAME, tag))

    def find_elements_by_tag(self, tag) -> SeleniumElement:
        return SeleniumElement(self.browser.find_elements(By.TAG_NAME, tag))


class SeleniumElement(AbstractElement):

    def __init__(self, element):
        self.element = element

    def __iter__(self):
        return iter(SeleniumElement(element) for element in self.element)

    def get_attribute(self, name):
        return self.element.get_attribute(name)

    def find_element_by_id(self, id_):
        return SeleniumElement(self.element.find_element(By.ID, id_))

    def find_element_by_class(self, class_):
        return SeleniumElement(
            self.element.find_element(By.CLASS_NAME, class_)
        )

    def find_elements_by_class(self, class_):
        return SeleniumElement(
            self.element.find_elements(By.CLASS_NAME, class_)
        )

    def find_element_by_tag(self, tag):
        return SeleniumElement(self.element.find_element(By.TAG_NAME, tag))

    def find_elements_by_tag(self, tag):
        return SeleniumElement(self.element.find_elements(By.TAG_NAME, tag))
