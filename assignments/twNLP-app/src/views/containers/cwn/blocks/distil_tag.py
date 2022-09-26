import streamlit as st
from .base import Block
from typing import List
from dataclasses import dataclass

divider_tag = "<hr style='margin-top: 1rem;margin-bottom: 1rem;border: 0;border-top: 1px solid rgba(0,0,0,.1);'/>"


@dataclass
class DistilTagBlock(Block):
    """
    The DistilTagBlock object visualizes the distil tags.
    """

    title: str
    distil_tags: List[str]

    def render_horizontal_line(self, distil_tags: List[str]) -> str:
        """The render_horizontal_line method inserts the `divider_tag` in between each item
        in `distil_tags`.
        Args:
            distil_tags (List[str]): a list of span tags that are the result of word sense disambiguation.
        Returns:
            a str
        """
        return divider_tag.join(distil_tags)

    def visualize(self) -> None:
        html_code = self.render_horizontal_line(self.distil_tags)

        st.subheader(self.title)
        with st.expander(self.title, expanded=True):
            st.markdown(html_code, unsafe_allow_html=True)
