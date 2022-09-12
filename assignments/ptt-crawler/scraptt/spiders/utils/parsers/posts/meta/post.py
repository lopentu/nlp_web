import re
from typing import List
from .date import format_date
from scrapy.http.response.html import HtmlResponse

meta_tag_selector = '//*[@id="main-content"]/div/span[@class="article-meta-tag"]'


async def get_meta_data(response: HtmlResponse) -> List[str]:
    """The get_meta_data function gets the meta data from a ptt post.

    Args:
        response (HtmlResponse): the response to parse
    Returns:
        a list of strings
    """

    meta_tag = response.xpath(
        f"{meta_tag_selector}/following-sibling::*/text()"
    ).getall()

    author_info = meta_tag[0]
    author = re.search(r"([^(]*)", author_info).group(1).strip()
    alias_match = re.search(r"\((.*)\)", author_info)
    alias = alias_match.group(1) if alias_match else ""
    meta_tag[0] = author
    meta_tag[-1] = await format_date(meta_tag[-1])
    meta_tag.insert(1, alias)
    return meta_tag
