import streamlit as st

def load_css():

    st.markdown(
        """
        <style>

        .main {
            padding-top: 1rem;
        }

        .stMetric {
            background-color: #111827;
            border: 1px solid #374151;
            padding: 15px;
            border-radius: 15px;
        }

        .stMetric:hover {
            border: 1px solid #3B82F6;
        }

        div[data-testid="stMetricValue"] {
            font-size: 36px;
            font-weight: bold;
        }

        div[data-testid="stMetricLabel"] {
            font-size: 18px;
        }

        h1 {
            color: white;
        }

        h2 {
            color: white;
        }

        h3 {
            color: white;
        }

        </style>
        """,
        unsafe_allow_html=True
    )