from pyquery import PyQuery
from scrapy.http.response.html import HtmlResponse


class PyqueryMiddleware:
    """
    The PyqueryMiddleware object injects PyQuery object into Scrapy `response`.
    """

    def process_response(self, request, response, spider) -> HtmlResponse:
        response.dom = PyQuery(response.text).make_links_absolute(
            "https://www.ptt.cc/bbs/"
        )
        return response
