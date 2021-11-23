import pytest

from src.adapters.driver import Driver, By, Element

driver = Driver()


def test_driver_find_element_by_id(test_url, mock_server):
    driver.get(test_url)

    element = driver.find_element(By.ID, "rso")

    assert isinstance(element, Element)
    assert element.get_attribute("id") == "rso"


def test_driver_find_element_by_tag_name(test_url, mock_server):
    driver.get(test_url)

    element = driver.find_element(By.TAG_NAME, "span")

    assert isinstance(element, Element)
    assert element.text == "unnecessarytag"


def test_driver_find_elements_by_class_name(test_url, mock_server):
    driver.get(test_url)

    elements = driver.find_elements(By.CLASS_NAME, "g")

    assert all(el.get_attribute("class") == "g" for el in elements)


def test_driver_find_elements_by_tag_name(test_url, mock_server):
    driver.get(test_url)

    elements = driver.find_elements(By.TAG_NAME, "h3")

    assert [el.text for el in elements] == ["Other", "Travatar"]


def test_driver_handle_connection_if_server_is_down(unavailable_server_url):
    with pytest.raises(
            ConnectionError,
            match="Driver can't connect to given search engine server."
    ):
        driver.get(unavailable_server_url)

# website is on another page
