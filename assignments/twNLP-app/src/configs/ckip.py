import pickle
import asyncio
import aiofiles
from pathlib import Path


pkg_path = Path("__file__").resolve().parent / "src"
ckip_path = pkg_path / "models" / "ckip"


async def write_drivers(nlp_model: str) -> None:
    """The write drivers function writes the ckip drivers to pickle files asynchronously.
    Args:
        nlp_model (str): the nlp model name
    """
    from ckip_transformers.nlp import (
        CkipWordSegmenter,
        CkipPosTagger,
        CkipNerChunker,
    )

    drivers = (
        CkipWordSegmenter(model=nlp_model),
        CkipPosTagger(model=nlp_model),
        CkipNerChunker(model=nlp_model),
    )

    driver_path = ckip_path / f"{nlp_model}_drivers.pickle"
    async with aiofiles.open(driver_path, mode="wb") as file:
        result = pickle.dumps(drivers)
        await file.write(result)
        print(f"{nlp_model}_drivers.pickle done!")


async def download_ckip_drivers(ckip_nlp_models):
    await asyncio.gather(*list(map(write_drivers, ckip_nlp_models)))
