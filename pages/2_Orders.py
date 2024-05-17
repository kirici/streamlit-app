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


page_dressing()
