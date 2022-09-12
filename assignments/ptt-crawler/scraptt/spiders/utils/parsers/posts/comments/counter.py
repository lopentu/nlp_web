from typing import List
from collections import Counter
from scrapy.http.response.html import HtmlResponse


async def count_comments(response: HtmlResponse) -> Counter:
    """The count_comments function counts the total number of comments in a ptt post.

    Args:
        response (HtmlResponse): the response to parse
    Returns:
        a Counter object.
    """

    push_tags: List[str] = response.css('span[class*="push-tag"]::text').getall()
    total_comments = [push_tag.strip() for push_tag in push_tags]
    return Counter(total_comments)
