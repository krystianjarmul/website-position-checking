from src.domain.model import Page, Result


def test_page_disallows_result_duplicates():
    page = Page()
    page.add_result(Result(title="Travatar", url="https://travatar.ai/"))
    page.add_result(Result(title="Travatar", url="https://travatar.ai/"))

    assert len(page.results) == 1


def test_page_gets_website_rank_successfully():
    page = Page()
    page.add_result(Result(title="Travatar", url="https://travatar.ai/"))
    page.add_result(Result(title="Other", url="https://other.com/"))

    position = page.get_website_position(website="https://travatar.ai/")

    assert position == 0


def test_page_get_position_returns_minus_one_if_website_not_in_results():
    page = Page()
    page.add_result(Result(title="Travatar", url="https://travatar.ai/"))
    page.add_result(Result(title="Other", url="https://other.com/"))

    position = page.get_website_position(website="https://different.ai/")

    assert position == -1
