import re
import requests
from typing import Tuple
from ......models import redis_cli
from requests.adapters import HTTPAdapter, Retry
from scrapy.http.response.html import HtmlResponse


def fetch_ip(ip: str) -> Tuple[str, str]:
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount("http://", HTTPAdapter(max_retries=retries))

    response = requests.get(f"http://www.geoplugin.net/json.gp?ip={ip}")
    result = response.json()
    city = result["geoplugin_city"]
    country = result["geoplugin_countryName"]
    return city, country


def fetch_ip_with_cache(ip) -> Tuple[str, str]:
    ip_result = redis_cli.hgetall(ip)

    if ip_result:
        city = ip_result["city"]
        country = ip_result["country"]
        return city, country

    city, country = fetch_ip(ip)

    ttl = 10 * 60
    redis_cli.hset(ip, mapping={"city": city, "country": country})
    redis_cli.expire(name=ip, time=ttl)

    return city, country


def get_ip_loc(ip: str, ip_cache: bool) -> Tuple[str, str]:
    """The get_ip_loc function get info from an ip.

    Args:
        ip (str): the ip from a ptt post.
        ip_cache (bool): a boolean that is used to determine whether
                         to enable redis service to cache ip.
    Returns:
        a tuple, containing city and country
    """
    if ip_cache:
        return fetch_ip_with_cache(ip)

    return fetch_ip(ip)
