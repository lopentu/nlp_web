import re
from .base import Parser
from scrapy import Request
from typing import Callable
from .....configs import COOKIES
from logging import LoggerAdapter
from dataclasses import dataclass
from scrapy.http.response.html import HtmlResponse


@dataclass
class LatestIndexParser(Parser):
    """
    The LatestIndexParser objects parses the latest index.html file.
    """

    logger: LoggerAdapter

    def get_latest_index(self, prev_url: str):
        return int(re.search(r"index(\d{1,6})\.html", prev_url).group(1))

    def get_board(self, url: str):
        return re.search(r"www\.ptt\.cc\/bbs\/([\w\d\-_]{1,30})\/", url).group(1)

    def parse(self, response: HtmlResponse, callback: Callable):
        prev_url = response.css('.btn.wide:contains("上頁")::attr(href)').get()
        self.logger.info(f"index link: {prev_url}")

        latest_index = self.get_latest_index(prev_url)
        board = self.get_board(response.url)

        for index in range(1, latest_index + 1):
            url = f"https://www.ptt.cc/bbs/{board}/index{index}.html"
            self.logger.info(f"index link: {url}")

            yield Request(url, cookies=COOKIES, callback=callback)