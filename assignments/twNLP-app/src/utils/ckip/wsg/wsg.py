from typing import List, Union
from dataclasses import dataclass
from models import connect_ckip_drivers


@dataclass
class WordSegmentation:
    """
    The WordSegmentation object divides written text in `sentence_lists` into meaningful units.
    """

    nlp_model: str
    sentence_list: List[str]

    def __post_init__(self) -> None:
        self.ws_driver = connect_ckip_drivers(self.nlp_model)[0]

    def remove_empty_string(self, sentence_list: List[str]) -> List[str]:
        """The remove_empty_string method removes empty string in `sentence_list`.
        Args:
            sentence_list (list)
        Returns:
            a list
        """
        return list(filter(lambda value: value is not "", sentence_list))

    def segment(self) -> List[Union[List[None], List[List[str]]]]:
        """The segment method divides written text in `sentence_lists` into meaningful units.
        Returns:
            a list of splitting text, an empty list otherwise.
        """
        invalid_list = not self.sentence_list or all(
            [value == "" for value in self.sentence_list]
        )

        if invalid_list:
            return self.sentence_list

        filtered_list = self.remove_empty_string(self.sentence_list)
        return self.ws_driver(filtered_list, use_delim=True)
