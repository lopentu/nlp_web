import asyncio
from typing import List
from context import use_WSG, WSGKind
from utils.ckip.wsg import WordSegmentation
from utils.text import add_multiple_textsubscripts


def handle_create_wsg(nlp_model: str, sentence_list: List[str]) -> List[str]:
    """The handle_create_wsg function handles the request that deals with word
    segmentation.
    Args:
        sentence_list (list): a list of sentences
    Returns:
        a list of strings
    """

    ws_result = WordSegmentation(nlp_model, sentence_list).segment()
    dispatch = use_WSG()[1]
    dispatch({"kind": WSGKind.ADD_WSG, "payload": ws_result})
    return asyncio.run(add_multiple_textsubscripts("ws", ws_result))