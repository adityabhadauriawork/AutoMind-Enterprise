import streamlit as st
import pandas as pd
import plotly.express as px

def show_analytics(df):

    st.subheader("📈 Sales by Category")

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        title="Sales by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )