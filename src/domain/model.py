from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Result:
    """Class representing a single search result."""
    title: str
    url: str


@dataclass
class Page:
    """Class representing a single page of search results."""
    number: int = field(default=1)
    results: List[Result] = field(default_factory=list)

    def get_website_position(self, website: str) -> int:
        try:
            result = next(res for res in self.results if res.url == website)
        except StopIteration:
            return -1
        return self.results.index(result)

    def add_result(self, result: Result):
        if result in self.results:
            return
        self.results.append(result)
