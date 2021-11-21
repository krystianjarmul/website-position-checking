from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.common.by import By as webdriver_By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement


class AbstractDriver(ABC):

    @abstractmethod
    def get(self, url: str):
        ...

    @abstractmethod
    def find_element(self, by: str, value: str) -> WebElement:
        ...

    @abstractmethod
    def find_elements(self, by: str, value: str):
        ...


class Driver(AbstractDriver):
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
        return self._driver.get(url)

    def find_element(self, by: str, value: str):
        try:
            return self._driver.find_element(By(by), value)
        except AttributeError:
            return

    def find_elements(self, by: str, value: str):
        try:
            return self._driver.find_elements(By(by), value)
        except AttributeError:
            return


def By(value: str) -> webdriver_By:
    if value == "id":
        return webdriver_By.ID
    elif value == "class":
        return webdriver_By.CLASS_NAME
    elif value == "tag":
        return webdriver_By.TAG_NAME
    else:
        raise AttributeError
