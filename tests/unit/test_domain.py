from src.domain.model import Page, Result


def test_page_gets_website_rank_successfully():
    result1 = Result(title="Travatar", url="https://travatar.ai/")
    result2 = Result(title="Other", url="https://other.com/")
    page = Page([result1, result2])

    position = page.get_website_position(website="https://travatar.ai/")

    assert position == 0


def test_page_get_position_returns_minus_one_if_website_not_in_results():
    result1 = Result(title="Travatar", url="https://travatar.ai/")
    result2 = Result(title="Other", url="https://other.com/")
    page = Page([result1, result2])

    position = page.get_website_position(website="https://different.ai/")

    assert position == -1
