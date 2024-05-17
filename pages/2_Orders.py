import time

import streamlit as st

st.set_page_config(
    page_title="Sample",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded",
)


def page_dressing():
    st.title("Coffee shop")
    st.markdown("#### Place your orders here")
    st.sidebar.markdown("# Orders")


def coffee_order():
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'{i+1} ml coffee extracted')
        bar.progress(i + 1)
        time.sleep(0.1)


page_dressing()
if st.button("Espresso", type="primary"):
    coffee_order()
