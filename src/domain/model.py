from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Result:
    """Value Object Class representing a single search result."""
    title: str
    url: str


class Page:
    """Entity Class representing a single page of search results."""

    def __init__(self, results: Optional[List[Result]] = None, num: int = 1):
        if results is None:
            results = []
        self.results = results
        self.number = num

    def get_website_position(self, website: str) -> int:
        try:
            result = next(res for res in self.results if res.url == website)
        except StopIteration:
            return -1
        return self.results.index(result)

    def __repr__(self):
        return f"Page {self.number}"

    def __hash__(self):
        return hash(self.number)

    def __eq__(self, other):
        if not isinstance(Page, other):
            return False
        return self.number == other.number
