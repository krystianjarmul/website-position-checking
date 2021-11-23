from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from typing import List

import bs4
from retry import retry
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By as webdriver_By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement

CHROMEDRIVER_PATH = "bin/chromedriver"


class By(str, Enum):
    ID = webdriver_By.ID
    CLASS_NAME = webdriver_By.CLASS_NAME
    TAG_NAME = webdriver_By.TAG_NAME


class AbstractElement(ABC):
    """Abstract Wrapper class for a web element."""

    @abstractmethod
    def find_element(self, by: By, value: str) -> AbstractElement:
        ...

    @abstractmethod
    def find_elements(self, by: By, value: str) -> List[AbstractElement]:
        ...

    @abstractmethod
    def get_attribute(self, name: str) -> str:
        ...


class AbstractDriver(ABC):
    """Abstract wrapper class for a driver."""

    @abstractmethod
    def get(self, url: str):
        ...

    @abstractmethod
    def find_element(self, by: By, value: str) -> Element:
        ...

    @abstractmethod
    def find_elements(self, by: By, value: str) -> List[Element]:
        ...


class Driver(AbstractDriver):
    """Wrapper class for selenium driver."""

    def __init__(self, chromedriver_path: str = CHROMEDRIVER_PATH):
        self._service = Service(chromedriver_path)
        self._options = Options()
        self._options.add_argument("--disable-extensions")
        self._options.add_argument("--headless")

        self._driver = webdriver.Chrome(
            options=self._options,
            service=self._service
        )
        self.page_source = None

    @retry(ConnectionError, tries=2, delay=2)
    def get(self, url):
        try:
            self._driver.get(url)
            self.page_source = self._driver.page_source
        except WebDriverException:
            raise ConnectionError(
                "Driver can't connect to given search engine server."
            )

    def find_element(self, by, value):
        try:
            return Element(self._driver.find_element(by, value))
        except AttributeError:
            return

    def find_elements(self, by, value):
        try:
            return [
                Element(element)
                for element in self._driver.find_elements(by, value)
            ]
        except AttributeError:
            return []


class Element(AbstractElement):
    """Wrapper class for selenium WebElement."""

    def __init__(self, element: WebElement):
        self._element = element
        self.text = self._element.text

    def find_element(self, by, value) -> Element:
        return Element(self._element.find_element(by, value))

    def find_elements(self, by, value) -> List[Element]:
        return [
            Element(element)
            for element in self._element.find_elements(by, value)
        ]

    def get_attribute(self, name):
        return self._element.get_attribute(name)


class FakeDriver(AbstractDriver):
    """Fake driver class for testing purpose."""

    def __init__(self, html):
        self.soup = bs4.BeautifulSoup(html, "html.parser")

    def get(self, url: str):
        pass

    def find_element(self, by, value):
        if by == By.ID:
            return FakeElement(self.soup.find(id=value))
        elif by == By.TAG_NAME:
            return FakeElement(self.soup.find_all(value)[0])

    def find_elements(self, by, value):
        return [
            FakeElement(element)
            for element in self.soup.find_all(class_=value)
        ]


class FakeElement(AbstractElement):
    """Fake element class for testing purpose."""

    def __init__(self, element):
        self._element = element

    def find_element(self, by, value):
        if by == By.ID:
            return FakeElement(self._element.find(id=value))
        elif by == By.TAG_NAME:
            return FakeElement(self._element.find_all(value)[0])

    def find_elements(self, by, value):
        return [
            FakeElement(element)
            for element in self._element.find_all(class_=value)
        ]

    def get_attribute(self, name):
        if name == "text":
            return getattr(self._element, name)
        return self._element[name]
