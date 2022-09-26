import asyncio
import pandas as pd
import streamlit as st
from .base import Block
from typing import List
from dataclasses import dataclass


@dataclass
class CWNSenseTagBlock(Block):
    """
    The CWNSenseTagBlock object visualizes the cwn sense tags.
    """

    title: str
    sentence_list: List[str]
    cwn_tags: List[List[List[tuple]]]

    def create_data_frame(self, value):
        df = pd.DataFrame(value)
        df = df.drop([2], axis=1)
        df = df.rename({0: "詞彙", 1: "詞類", 3: "釋義"}, axis=1)
        return df

    async def create_multiple_dfs(self, data: List[tuple]):
        return list(map(self.create_data_frame, data))

    async def gather_multiple_dfs(self, cwn_tags: List[List[List[tuple]]]):
        return await asyncio.gather(*list(map(self.create_multiple_dfs, cwn_tags)))

    def visualize(self) -> None:
        st.subheader(self.title)
        data_frames = asyncio.run(self.gather_multiple_dfs(self.cwn_tags))
        table_result = zip(self.sentence_list, data_frames)

        for sentence, tables in table_result:
            with st.expander(sentence, expanded=True):
                for table in tables:
                    st.table(table)
