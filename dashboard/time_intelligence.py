import streamlit as st
import pandas as pd
import plotly.express as px


def show_time_intelligence(df):

    st.header("📅 Time Intelligence Dashboard")

    # =========================
    # DATE PREPARATION
    # =========================

    df = df.copy()

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

    df = df.dropna(subset=["Order Date"])

    # =========================
    # DATE FILTERS
    # =========================

    min_date = df["Order Date"].min().to_pydatetime()
    max_date = df["Order Date"].max().to_pydatetime()

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input(
            "📅 Start Date",
            value=min_date
        )

    with col2:
        end_date = st.date_input(
            "📅 End Date",
            value=max_date
        )

    start_date = pd.Timestamp(start_date)
    end_date = pd.Timestamp(end_date)

    df = df[
        (df["Order Date"] >= start_date)
        &
        (df["Order Date"] <= end_date)
    ]

    # =========================
    # MONTH COLUMN
    # =========================

    df["Month"] = (
        df["Order Date"]
        .dt.to_period("M")
        .astype(str)
    )

    # =========================
    # MONTHLY SALES
    # =========================

    monthly_sales = (
        df.groupby("Month")["Sales"]
        .sum()
        .reset_index()
    )

    # =========================
    # MONTHLY PROFIT
    # =========================

    monthly_profit = (
        df.groupby("Month")["Profit"]
        .sum()
        .reset_index()
    )

    # =========================
    # MONTHLY ORDERS
    # =========================

    monthly_orders = (
        df.groupby("Month")["Order ID"]
        .nunique()
        .reset_index()
    )

    monthly_orders.columns = [
        "Month",
        "Orders"
    ]

    # =========================
    # GROWTH %
    # =========================

    monthly_sales["Growth %"] = (
        monthly_sales["Sales"]
        .pct_change()
        * 100
    )

    latest_growth = (
        monthly_sales["Growth %"]
        .iloc[-1]
        if len(monthly_sales) > 1
        else 0
    )

    # =========================
    # MOVING AVERAGE
    # =========================

    monthly_sales["MA_3"] = (
        monthly_sales["Sales"]
        .rolling(3)
        .mean()
    )

    # =========================
    # KPI CARDS
    # =========================

    st.subheader("📌 Time Intelligence KPIs")

    k1, k2, k3 = st.columns(3)

    with k1:
        st.metric(
            "Latest Monthly Sales",
            f"${monthly_sales['Sales'].iloc[-1]:,.0f}"
        )

    with k2:
        st.metric(
            "Latest Monthly Profit",
            f"${monthly_profit['Profit'].iloc[-1]:,.0f}"
        )

    with k3:
        st.metric(
            "Sales Growth %",
            f"{latest_growth:.2f}%"
        )

    # =========================
    # MONTHLY SALES TREND
    # =========================

    st.subheader("📈 Monthly Sales Trend")

    fig_sales = px.line(
        monthly_sales,
        x="Month",
        y=["Sales", "MA_3"],
        markers=True,
        title="Monthly Sales with 3-Month Moving Average"
    )

    st.plotly_chart(
        fig_sales,
        use_container_width=True
    )

    # =========================
    # MONTHLY PROFIT TREND
    # =========================

    st.subheader("💰 Monthly Profit Trend")

    fig_profit = px.line(
        monthly_profit,
        x="Month",
        y="Profit",
        markers=True,
        title="Monthly Profit Trend"
    )

    st.plotly_chart(
        fig_profit,
        use_container_width=True
    )

    # =========================
    # MONTHLY ORDERS TREND
    # =========================

    st.subheader("📦 Monthly Orders Trend")

    fig_orders = px.line(
        monthly_orders,
        x="Month",
        y="Orders",
        markers=True,
        title="Monthly Orders Trend"
    )

    st.plotly_chart(
        fig_orders,
        use_container_width=True
    )