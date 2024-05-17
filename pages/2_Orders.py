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


def coffee_order(drink: str):
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        # ml per percent for an espresso
        c = (i+1)/4
        latest_iteration.text(f'{int(c)} ml coffee extracted')
        bar.progress(i + 1)
        time.sleep(0.1)
    st.success("One "+drink+" ready to go!")
    st.session_state[drink] = ''
    st.write(st.session_state[drink])


page_dressing()
if st.button("Espresso", type="primary"):
    coffee_order(drink="espresso")
