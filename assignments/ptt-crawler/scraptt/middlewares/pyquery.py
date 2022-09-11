from pyquery import PyQuery


class PyqueryMiddleware:
    """
    The PyqueryMiddleware object injects PyQuery object into Scrapy `response`.
    """

    def process_response(self, request, response, spider):
        response.dom = PyQuery(response.text).make_links_absolute(
            "https://www.ptt.cc/bbs/"
        )
        return response
