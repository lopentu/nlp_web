import streamlit as st
from typing import Callable
from controllers.cwn import handle_create_cwn_tags
from controllers.ckip import handle_create_ner, handle_create_pos, handle_create_wsg


TEN_MINUTES = 60 * 10


@st.cache(ttl=TEN_MINUTES, show_spinner=True)
def request(method: str, *args, **kwargs) -> Callable:
    """The request function fetches the data based on the `method`.

    Args:
        method (str): the request method
    Returns:
        a controller function
    """

    methods = {
        "ner": handle_create_ner,
        "pos": handle_create_pos,
        "wsg": handle_create_wsg,
        "cwn": handle_create_cwn_tags,
    }

    return methods[method](*args, **kwargs)
