import asyncio
from .ner import create_ner
from typing import List, Tuple, Union
from ckip_transformers.nlp.util import NerToken


async def chunk_entities(zip_value: Tuple[Union[str, NerToken]]) -> str:
    sentence, ner_token_list = zip_value
    return create_ner(sentence, ner_token_list)


async def chunk_multiple_entities(data: zip) -> List[str]:
    return await asyncio.gather(*list(map(chunk_entities, data)))