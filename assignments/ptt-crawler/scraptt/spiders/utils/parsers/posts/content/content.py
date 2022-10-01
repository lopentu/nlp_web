import re
from pyquery import PyQuery
from dataclasses import dataclass
from .html_stripper import HTMLStripper


@dataclass
class ContentCleaner:
    """
    The ContentCleaner object cleans the post content.
    """

    content: PyQuery

    def __post_init__(self) -> None:
        self.content_clone = (
            self.content.clone()
            .children()
            .remove('span[class^="article-meta-"]')
            .remove("div.push")
            .end()
            .html()
        )

    def strip_content(self, content: PyQuery) -> str:
        stripped_content = HTMLStripper.strip_tags(content)
        return re.sub(r"※ 發信站.*|※ 文章網址.*|※ 編輯.*", "", stripped_content).strip("\r\n-")

    def remove_quotes(self, stripped_content: str):
        quotes = re.findall("※ 引述.*|\n: .*", stripped_content)

        for quote in quotes:
            stripped_content = stripped_content.replace(quote, "")

        return stripped_content.strip("\n ")

    def clean(self):
        stripped_content = self.strip_content(self.content_clone)

        if stripped_content == "" or stripped_content is None:
            return None

        return self.remove_quotes(stripped_content)
