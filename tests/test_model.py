from src.domain.model import Page, Result


def test_page_get_position_of_a_website_success():
    page = Page()
    page.add_result(Result(title="Travatar", url="https://travatar.ai/"))
    page.add_result(Result(title="Other", url="https://other.com/"))

    position = page.get_position(website="https://travatar.ai/")

    assert position == 0


def test_page_get_position_returns_minus_one_if_website_not_in_results():
    page = Page()
    page.add_result(Result(title="Travatar", url="https://travatar.ai/"))
    page.add_result(Result(title="Other", url="https://other.com/"))

    position = page.get_position(website="https://different.ai/")

    assert position == -1
