from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from src.domain.model import Result, Page

GOOGLE_SEARCH_URL = "https://www.google.com/search?q="
CHROMEDRIVER_PATH = "bin/chromedriver"


def get_website_position(
        query: str,
        website: str,
        chromedriver_path: str,
        server: str = GOOGLE_SEARCH_URL,
) -> int:
    # move to infrastructure layer
    service = Service(chromedriver_path)

    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        options=options,
        service=service
    )

    driver.get(f"{server}{query}")
    container = driver.find_element(By.ID, "rso")
    container_items = container.find_elements(By.CLASS_NAME, "g")

    page = Page()

    for item in container_items:
        title = item.find_element(By.TAG_NAME, "h3")
        hyperlink = item.find_element(By.TAG_NAME, "a")
        url = hyperlink.get_attribute("href")

        result = Result(title=title.text, url=url)
        page.add_result(result)

    position = page.get_position(website)

    return position
