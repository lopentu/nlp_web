from pydantic import BaseModel
from typing import Union, Dict, List


class ScrapttItem(BaseModel):
    """
    The ScrapttItem object keeps track of an item in inventory.
    """

    board: str
    post_id: str
    author: str
    alias: str
    title: str
    date: str
    ip: str
    city: Union[str, None]
    country: Union[str, None]
    url: str
    body: str
    post_vote: Dict[str, int]
    comments: List[Dict[str, str]]
