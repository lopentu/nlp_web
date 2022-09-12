import re
from .base import Parser
from datetime import datetime
from .....configs import COOKIES
from logging import LoggerAdapter
from typing import Callable, List
from dataclasses import dataclass
from scrapy import Request, Selector
from scrapy.http.response.html import HtmlResponse


@dataclass
class YearBackwardIndexParser(Parser):
    """
    The YearBackwardIndexParser object parses the index.html files from a year in the
    past to the current one.
    """

    since: str
    title_tags: List[Selector]
    logger: LoggerAdapter

    def parse(
        self, response: HtmlResponse, callback: Callable, self_callback: Callable
    ):
        for title_tag in reversed(list(self.title_tags.items())):
            title = title_tag.text()
            post_url = title_tag.attr("href")
            timestamp = re.search(r"(\d{10})", post_url).group(1)

            if int(timestamp) < int(self.since):
                return None

            self.logger.info(
                f"+ {title}, {post_url}, {datetime.fromtimestamp(int(timestamp))}"
            )

            yield Request(post_url, cookies=COOKIES, callback=callback)

        prev_url = response.dom('.btn.wide:contains("上頁")').attr("href")
        self.logger.info(f"index link: {prev_url}")

        if prev_url:
            yield Request(prev_url, cookies=COOKIES, callback=self_callback)
