import asyncio
from typing import List, Union
from models import connect_ckip_drivers
from ckip_transformers.nlp.util import NerToken
from utils.ckip.ner import chunk_multiple_entities


def is_list_of_empty_list(ner_token_list: List[Union[NerToken, None]]) -> bool:
    """The is_list_of_empty_list function checks whether a list is full of empty lists.
    Args:
        ner_token_list (list): the result of the ner driver
    Returns:
        a bool
    """
    return all(map(lambda value: not value, ner_token_list))


def handle_create_ner(nlp_model: str, sentence_list: List[str]) -> List[str]:
    """The handle_create_ner function handles the request that deals with NER.
    Args:
        nlp_model (str): the nlp model name
        sentence_list (list): a list of sentences
    Returns:
        a list of strings
    """
    ner_driver = connect_ckip_drivers(nlp_model)[2]
    ner_token_list = ner_driver(sentence_list)

    if is_list_of_empty_list(ner_token_list):
        return sentence_list

    return asyncio.run(chunk_multiple_entities(zip(sentence_list, ner_token_list)))
