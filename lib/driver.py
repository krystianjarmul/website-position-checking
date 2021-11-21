from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By as webdriver_By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement


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

    def __init__(self, chromedriver_path: str):
        self._service = Service(chromedriver_path)
        self._options = Options()
        self._options.add_argument("--disable-extensions")
        self._options.add_argument("--headless")

        self._driver = webdriver.Chrome(
            options=self._options,
            service=self._service
        )

    def get(self, url):
        self._driver.get(url)

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

    def find_element(self, by, value) -> Element:
        return Element(self._element.find_element(by, value))

    def find_elements(self, by, value) -> List[Element]:
        return [
            Element(element)
            for element in self._element.find_elements(by, value)
        ]

    def get_attribute(self, name):
        return self._element.get_attribute(name)
