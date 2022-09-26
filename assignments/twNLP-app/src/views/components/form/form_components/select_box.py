from streamlit import selectbox
from typing import Callable, Optional, Tuple


def add_selectbox(
    title: str,
    options: Tuple[str],
    key: Optional[str] = None,
    on_change: Optional[Callable] = None,
):
    return selectbox(title, options=options, key=key, on_change=on_change)
