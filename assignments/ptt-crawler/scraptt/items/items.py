from typing import Union
from pydantic import BaseModel


class ScrapttItem(BaseModel):
    """
    The ScrapttItem object keeps track of an item in inventory.
    """

    board: str
    author: str
    alias: str
    title: str
    date: str
    ip: str
    city: Union[str, None]
    country: Union[str, None]
    ups: int
    downs: int
    comments: int
    url: str
