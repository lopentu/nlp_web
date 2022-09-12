import re
from datetime import datetime


async def format_date(str_date: str) -> str:
    """The format_date function formats dates and times of a ptt post.

    Args:
        str_date (str): a string date from a ptt post
    Returns:
        a str
    """
    str_format = "%Y-%m-%d %H:%M:%S"

    try:
        return datetime.strptime(str_date, "%a %b %d %H:%M:%S %Y").strftime(str_format)
    except:
        # handle incomplete date
        str_date = re.match(r"(.*\d{2}:\d{2}:\d{2}).*", str_date).group(1)
        date = datetime.strptime(str_date, "%a %b %d %H:%M:%S")
        date = date.replace(year=datetime.now().year)
        return date.strftime(str_format)
