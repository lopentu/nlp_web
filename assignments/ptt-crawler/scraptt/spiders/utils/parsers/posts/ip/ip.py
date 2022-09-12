import re
from scrapy.http.response.html import HtmlResponse


async def get_ip(response: HtmlResponse) -> str:
    """The get_ip function gets the ip address from a ptt post.

    Args:
        response (HtmlResponse): the response to parse
    Returns:
        a str
    """
    f2_spans = response.dom(".f2")
    old_ip_format = "([0-9.]*)$"
    old_ip = re.search(old_ip_format, f"{f2_spans}").group(1)

    if old_ip:
        return old_ip

    f2_spans_list = [f2_span.text() for f2_span in f2_spans.items()]

    try:
        text = [
            f2_span
            for f2_span in f2_spans_list
            if re.match(r"※ 發信站: 批踢踢實業坊\(ptt\.cc\), 來自:", f2_span)
        ][0]
        return re.search(r"來自: ([0-9.]*)", text).group(1)

    except:
        ip_match = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        text = [span for span in f2_spans_list if re.findall(ip_match, span)][-1]
        return re.findall(ip_match, text)[-1]
