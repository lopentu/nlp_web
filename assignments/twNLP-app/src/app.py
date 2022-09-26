import streamlit as st
from views.components.spinner import dowload_ckip_package, download_cwn_drivers


def run_app(ckip_nlp_models, cwn_upgrade) -> None:
    # need to download first because CWN packages will first check whether
    # there is .cwn_graph folder in the root directory.
    download_cwn_drivers(cwn_upgrade)
    dowload_ckip_package(ckip_nlp_models)

    from views.components.sidebar import visualize_side_bar
    from views.containers import display_cwn, display_ckip, display_data_form

    st.title("LOPE")
    input_data = display_data_form()
    model, pipeline, active_visualizers = visualize_side_bar(ckip_nlp_models)
    display_factories = {"CKIP": display_ckip, "CWN": display_cwn}

    if "input_data" in st.session_state:
        display_factories[pipeline](
            model, active_visualizers, st.session_state["input_data"]
        )


if __name__ == "__main__":
    ckip_nlp_models = ["bert-base", "albert-tiny", "bert-tiny", "albert-base"]
    run_app(ckip_nlp_models, cwn_upgrade=False)
