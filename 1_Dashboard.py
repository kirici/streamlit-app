"""
A sample streamlit application.
"""
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


@st.cache_data
def init_data() -> pd.DataFrame:
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    return chart_data


def render(df=pd.DataFrame):
    st.line_chart(df)

    x = st.slider('x')
    st.write(x, 'squared is', x * x)


page_dressing()
render(df=init_data())
