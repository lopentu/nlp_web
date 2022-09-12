import re
import requests
from typing import Tuple
from requests.adapters import HTTPAdapter, Retry
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
        text = [f2_span for f2_span in f2_spans_list if re.match(r"※ 編輯:", f2_span)][0]
        return re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", text)[-1]


def get_ip_loc(ip: str) -> Tuple[str, str]:
    """The get_ip_loc function locates an ip address.

    Args:
        ip (str): the ip from a ptt post
    Returns:
        a tuple, containing city and counttry.
    """

    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount("http://", HTTPAdapter(max_retries=retries))

    response = requests.get(f"http://www.geoplugin.net/json.gp?ip={ip}")
    result = response.json()
    city = result["geoplugin_city"]
    country = result["geoplugin_countryName"]
    return city, country
