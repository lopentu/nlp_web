from functools import lru_cache
from ...text import create_entity_color
from typing import List, Tuple, Optional
from ckip_transformers.nlp.util import NerToken


def add_textsubscript(ner_token_list: List[NerToken]) -> Tuple[Tuple[str]]:
    """The add_textsubscript function combines the token word and the
    NER-tag, and specifies the NER-tag to be displayed as subscript.
    Args:
        ner_token_list (NerToken): a list of NerToken
    Returns:
        a tuple: (
            ("<span>傅達仁<sub style='margin-right: 0.1rem'>PERSON</sub></span>", (0, 3))
            ...
        )
    """

    combine = lambda value: (
        f"<span style='color: {create_entity_color(value.ner)};'>{value.word}<sub style='margin-right: 0.6rem'>{value.ner}</sub></span>",
        value.idx,
    )
    return tuple(map(combine, ner_token_list))


@lru_cache(maxsize=None)
def modify_sentence(
    span_tuple: Tuple[Tuple[str]], sentence: str, increased_len: Optional[int] = 0
) -> str:
    if len(list(span_tuple)) == 1:
        span_list = list(span_tuple)
        modified_word, index = span_list[0]
        start_index, end_index = index
        start_index += increased_len
        end_index += increased_len
        return "".join((sentence[:start_index], modified_word, sentence[end_index:]))

    span_list = list(span_tuple)
    modified_word, index = span_list.pop(0)
    span_tuple = tuple(span_list)

    start_index, end_index = index

    if increased_len:
        start_index += increased_len
        end_index += increased_len

    original_word = sentence[start_index:end_index]
    modified_sentence = "".join(
        (sentence[:start_index], modified_word, sentence[end_index:])
    )

    index_gap = len(modified_word) - len(original_word)
    return modify_sentence(span_tuple, modified_sentence, increased_len + index_gap)


def create_ner(sentence: str, ner_token_list: List[NerToken]) -> str:
    """The replace_entities function replaces words that are recognized
    as the token words with opening and closing span tags.
    Args:
        sentence (str): the orignal sentence
        ner_token_list (NerToken): a list of NerToken
    Returns:
        a str
    """
    modified_ner_token_list = add_textsubscript(ner_token_list)
    return modify_sentence(modified_ner_token_list, sentence)
