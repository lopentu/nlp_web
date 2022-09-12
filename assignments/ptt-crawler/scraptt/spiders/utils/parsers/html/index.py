from .base import Parser
from .....configs import COOKIES
from typing import Callable, List
from dataclasses import dataclass
from scrapy import Request, Selector


@dataclass
class IndexParser(Parser):
    """
    The IndexParser object parses one of the index.html files.
    """

    title_tags: List[Selector]

    def parse(self, callback: Callable):
        tag_lists = list(self.title_tags.items())

        for title_tag in tag_lists:
            url = title_tag.attr("href")
            yield Request(url, cookies=COOKIES, callback=callback)
