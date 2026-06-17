import streamlit as st
import sqlite3
import pandas as pd


def show_model_registry():

    st.title("🧠 MLOps Model Registry")

    conn = sqlite3.connect(
        "database/automind.db"
    )

    query = """
    SELECT *
    FROM model_registry
    ORDER BY created_at DESC
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    if len(df) == 0:

        st.warning(
            "No model runs found."
        )

        return

    st.subheader(
        "📊 Model History"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    best_model = df.sort_values(
        "r2_score",
        ascending=False
    ).iloc[0]

    st.success(
        f"""
Best Model:

{best_model['model_name']}

R²: {best_model['r2_score']:.3f}

MAE: {best_model['mae']:.2f}

RMSE: {best_model['rmse']:.2f}
"""
    )