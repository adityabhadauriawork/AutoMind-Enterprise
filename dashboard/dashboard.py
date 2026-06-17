import streamlit as st
import time

def show_dashboard(df):

    st.subheader("📊 Executive Dashboard")

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    total_customers = df["Customer Name"].nunique()

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    rev_placeholder = kpi1.empty()
    profit_placeholder = kpi2.empty()
    orders_placeholder = kpi3.empty()
    customers_placeholder = kpi4.empty()

    for i in range(0, 101, 5):

        rev_placeholder.metric(
            "Revenue",
            f"${int(total_sales * i / 100):,}"
        )

        profit_placeholder.metric(
            "Profit",
            f"${int(total_profit * i / 100):,}"
        )

        orders_placeholder.metric(
            "Orders",
            int(total_orders * i / 100)
        )

        customers_placeholder.metric(
            "Customers",
            int(total_customers * i / 100)
        )

        time.sleep(0.02)