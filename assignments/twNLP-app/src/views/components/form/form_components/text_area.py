from typing import Optional
from streamlit import text_area


def add_text_area(
    title: str,
    placeholder: Optional[str] = "",
    height: Optional[int] = None,
    key: Optional[str] = None,
):
    return text_area(title, placeholder=placeholder, height=height, key=key)
