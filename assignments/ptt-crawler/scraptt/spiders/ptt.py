import asyncio
from .base import BaseSpider
from ..items import ScrapttItem
from scrapy.http.response.html import HtmlResponse
from .utils.parsers.posts.meta import get_meta_data
from .utils.parsers.posts.ip import get_ip, get_ip_loc
from .utils.parsers.posts.content import ContentCleaner
from .utils.parsers.posts.comment import count_comments, CommentsParser


async def create_post_data(response: HtmlResponse):
    return await asyncio.gather(
        *[
            get_meta_data(response),
            count_comments(response),
            get_ip(response),
            CommentsParser(response).parse(),
            ContentCleaner(response.dom("#main-content")).clean(),
        ]
    )


class PttSpider(BaseSpider):
    name = "ptt"

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def parse(self, response: HtmlResponse):
        post_url = response.url
        post_id = post_url.split("/")[-1].split(".html")[0]
        meta_data, comment_counter, ip, comments, body = asyncio.run(
            create_post_data(response)
        )
        author, alias, board, title, date = meta_data
        city, country = get_ip_loc(ip, self.ip_cache)

        data = {
            "board": board,
            "author": author,
            "alias": alias,
            "title": title,
            "date": date,
            "ip": ip,
            "city": city,
            "country": country,
            "body": body,
            "post_vote": comment_counter,
            "post_id": post_id,
            "url": post_url,
            "comments": comments,
        }

        yield ScrapttItem(**data).dict()
