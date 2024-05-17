"""
A sample streamlit application.
"""
import numpy as np
import pandas as pd
import streamlit as st


def init_data() -> pd.DataFrame:
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    return chart_data


def render(df=pd.DataFrame):
    st.title('Hello World')
    st.line_chart(df)

    x = st.slider('x')
    st.write(x, 'squared is', x * x)


d = init_data()
render(df=d)
