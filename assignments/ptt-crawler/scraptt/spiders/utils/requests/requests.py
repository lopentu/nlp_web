from scrapy import Request
from ....configs import PTT_BOARD, COOKIES
from typing import Callable, List, Optional


def fetch_ptt_boards(
    boards_list: List[str],
    callback: Callable,
    index_from: Optional[str] = None,
    index_to: Optional[str] = None,
):
    """The fetch_ptt_boards function fetches the ptt boards htm indexes.

    Args:
        boards_list (list): a list of boards
        callback (Callable): a scrapy parse function
        index_from (str | None): the starting html index
        index_to (str | None): the ending html index
    Returns:
        a scrapy Request.
    """

    for board in boards_list:
        if index_from is not None and index_to is not None:
            if int(index_from) > int(index_to):
                raise ValueError(
                    "the value of `index_from` cannot be greater than `index_to`."
                )

            for index in range(int(index_from), int(index_to) + 1):
                url = PTT_BOARD.format(board, index)
                yield Request(url, cookies=COOKIES, callback=callback)
        else:
            url = PTT_BOARD.format(board, "")
            yield Request(url, cookies=COOKIES, callback=callback)
