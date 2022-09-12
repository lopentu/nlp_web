from scrapy import Spider
from typing import Optional
from ..utils.parsers.html import (
    IndexParser,
    LatestIndexParser,
    YearBackwardIndexParser,
    get_title_tags,
)
from abc import ABC, abstractmethod
from ..utils.requests import fetch_ptt_boards
from scrapy.http.response.html import HtmlResponse


class BaseSpider(Spider, ABC):
    """
    The BasePostSpider object defines the behaviour for crawling and parsing ptt posts.
    """

    allowed_domains = ["ptt.cc"]

    def __init__(
        self,
        boards: str,
        data_dir: str = "./data",
        ip_cache: bool = False,
        scrap_all: Optional[bool] = None,
        index_from: Optional[int] = None,
        index_to: Optional[int] = None,
        since: Optional[int] = None,
        *args,
        **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.boards = boards.split(",")
        self.data_dir = data_dir
        self.ip_cache = ip_cache
        self.scrap_all = scrap_all
        self.index_from = index_from
        self.index_to = index_to
        self.since = since

    def start_requests(self):
        return fetch_ptt_boards(
            self.boards, self.parse_index, self.index_from, self.index_to
        )

    def parse_index(self, response: HtmlResponse):
        title_tags = get_title_tags(response)

        if self.scrap_all:
            return LatestIndexParser(self.logger).parse(response, self.parse_index)
        elif self.since:
            return YearBackwardIndexParser(
                self.since,
                title_tags,
                self.logger,
            ).parse(response, callback=self.parse, self_callback=self.parse_index)
        else:
            return IndexParser(title_tags).parse(self.parse)

    @abstractmethod
    def parse(self, response: HtmlResponse, **kwargs):
        pass
