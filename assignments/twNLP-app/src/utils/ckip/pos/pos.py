from typing import List, Union
from dataclasses import dataclass
from models import connect_ckip_drivers


@dataclass
class PosTagging:
    """
    The PosTagging object marks a word in `ws_result` as corresponding to a particular part of speech.
    """

    nlp_model: str
    ws_result: List[Union[List[None], List[str]]]

    def __post_init__(self) -> None:
        self.pos_driver = connect_ckip_drivers(self.nlp_model)[1]

    def pack_ws_pos_sentece(self, ws_pos_pair: tuple) -> List[tuple]:
        """The pack_ws_pos_sentece method packs both words and thier part-of-speech to a pair.
        Args:
            ws_pos_pair (tuple): the pair of a word and its corresponding part-of-speech
        Returns:
            a list of tuples: [
                ('我', 'Nh'),
                ('喜歡', 'VK'),
                ('程式', 'Na')
            ]
        """

        sentence_ws, sentence_pos = ws_pos_pair
        assert len(sentence_ws) == len(sentence_pos)
        return list(
            map(lambda word_pos_pair: word_pos_pair, zip(sentence_ws, sentence_pos))
        )

    def tag(self):
        pos_pipeline = self.pos_driver(self.ws_result, use_delim=True)
        return list(map(self.pack_ws_pos_sentece, zip(self.ws_result, pos_pipeline)))
