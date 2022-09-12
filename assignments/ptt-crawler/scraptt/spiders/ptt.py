import asyncio
from .base import BaseSpider
from ..items import ScrapttItem
from scrapy.http.response.html import HtmlResponse
from .utils.parsers.posts.meta import get_meta_data
from .utils.parsers.posts.ip import get_ip, get_ip_loc
from .utils.parsers.posts.comments import count_comments


async def get_post_data(response: HtmlResponse):
    return await asyncio.gather(
        *[get_meta_data(response), count_comments(response), get_ip(response)]
    )


class PttSpider(BaseSpider):
    name = "ptt"

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def parse(self, response: HtmlResponse):
        post_url = response.url
        meta_data, comment_counter, ip = asyncio.run(get_post_data(response))
        author, alias, board, title, date = meta_data
        ups = comment_counter["推"]
        downs = comment_counter["噓"]
        comments = comment_counter["→"]
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
            "ups": ups,
            "downs": downs,
            "comments": comments,
            "url": post_url,
        }

        yield ScrapttItem(**data).dict()
