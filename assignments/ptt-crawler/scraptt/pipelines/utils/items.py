from operator import itemgetter
from typing import Any, Dict, List


def get_items(scrapy_item, item_list: List[str]) -> Dict[str, Any]:
    """
    The get_items function gets the selected items from `scrapy_item`
    and forms a dict.
    """
    items = itemgetter(*item_list)(scrapy_item)
    return dict(zip(item_list, items))
