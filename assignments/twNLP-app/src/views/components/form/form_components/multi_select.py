from streamlit import sidebar
from typing import Callable, List, Optional


def add_multiselect(
    title: str,
    options: List[str],
    key: Optional[str] = None,
    on_change: Optional[Callable] = None,
    format_func: Optional[Callable] = None
):
    return sidebar.multiselect(
        title, options=options, default=list(options), key=key, on_change=on_change, format_func=format_func
    )
