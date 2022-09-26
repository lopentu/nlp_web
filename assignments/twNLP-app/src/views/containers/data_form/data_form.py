import streamlit as st
from .utils import clean_data
from ...components.form import form_controller


def display_data_form():
    with st.form("my_form"):
        input_data: str = form_controller("text-area", title="請輸入句子：")
        submitted = st.form_submit_button("確定")

        if submitted:
            cleaned_data = clean_data(input_data.strip())

            if not cleaned_data:
                st.error("請輸入句子！")
                return False

            st.session_state["input_data"] = cleaned_data
            return cleaned_data
