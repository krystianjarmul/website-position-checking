from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Result:
    title: str
    url: str


@dataclass
class Page:
    number: int = field(default=1)
    results: List[Result] = field(default_factory=list)

    def get_website_position(self, website: str) -> int:
        try:
            result = next(r for r in self.results if r.url == website)
        except StopIteration:
            return -1
        return self.results.index(result)

    def add_result(self, result: Result):
        if result in self.results:
            return
        self.results.append(result)

