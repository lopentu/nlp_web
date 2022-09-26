import asyncio
from typing import List
from context import use_WSG
from utils.ckip.pos import PosTagging
from utils.text import add_multiple_textsubscripts


def handle_create_pos(nlp_model: str, sentence_list: List[str]):
    """The handle_create_pos function handles the request that deals with pos-tagging.
    Args:
        sentence_list (list): a list of sentences
    Returns:
        a list of strings
    """

    ws_result = use_WSG()[0]
    segmented_result = PosTagging(nlp_model, ws_result).tag()
    return asyncio.run(add_multiple_textsubscripts("pos", segmented_result))
