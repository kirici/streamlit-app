"""
A sample streamlit application.
"""
from time import sleep

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Sample",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded",
)


def page_dressing():
    st.title('Hello World')
    st.sidebar.markdown("# Dashboard")


def init_state():
    if "orders" not in st.session_state:
        st.session_state.orders = {}


@st.cache_data
def init_data() -> pd.DataFrame:
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    return chart_data


def drink(key: str):
    del st.session_state.orders[key]


def orders():
    st.markdown("## Beverages")
    for key in st.session_state.orders.keys():
        if st.button(key, type="primary"):
            drink(key)
            st.info("Grabbed " + key)
            sleep(1.5)
            st.rerun()


def render(df=pd.DataFrame):
    st.line_chart(df)

    x = st.slider('x')
    st.write(x, 'squared is', x * x)


page_dressing()
init_state()
render(df=init_data())
orders()
