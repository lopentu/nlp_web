import pickle
from configs import ckip_path


def connect_ckip_drivers(nlp_model: str) -> tuple:
    """The connect_ckip_drivers function connects to the ckip drivers.

    Args:
        nlp_model (str): the nlp model name
    Returns:
        a tuple, containing CkipWordSegmenter, CkipPosTagger and CkipNerChunker.
    """

    driver_path = ckip_path / f"{nlp_model}_drivers.pickle"

    with open(driver_path, "rb") as file:
        return pickle.load(file)