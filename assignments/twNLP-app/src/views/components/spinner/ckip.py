import asyncio
import streamlit as st
from pathlib import Path
from configs import ckip_path, download_ckip_drivers


def dowload_ckip_package(ckip_nlp_models):
    drivers = list(
        map(lambda model: ckip_path / f"{model}_drivers.pickle", ckip_nlp_models)
    )

    while not all(list(map(lambda path: Path(path).exists(), drivers))):
        with st.spinner("Downloading CKIP models ..."):
            asyncio.run(download_ckip_drivers(ckip_nlp_models))

        if all(list(map(lambda path: Path(path).exists(), drivers))):
            break
