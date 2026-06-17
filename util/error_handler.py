import streamlit as st
from util.logger import logger


def handle_error(error):

    logger.error(str(error))

    st.error(
        f"""
❌ AutoMind Error

{str(error)}
"""
    )