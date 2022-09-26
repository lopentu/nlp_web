import streamlit as st
from pathlib import Path
from configs import download_cwn_models, cwn_model_path


def download_cwn_drivers(upgrade):
    cwn_drivers = [
        cwn_model_path / "cwn-graph-v.2022.08.01.pyobj",
        cwn_model_path / "manifest.json",
        cwn_model_path / "cwn-wsd-model",
        cwn_model_path / "tagmodel",
    ]

    while not all(list(map(lambda path: Path(path).exists(), cwn_drivers))):
        with st.spinner("Downloading CWN models ..."):
            download_cwn_models(upgrade)

        if all(list(map(lambda path: Path(path).exists(), cwn_drivers))):
            break
