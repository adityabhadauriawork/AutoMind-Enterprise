import streamlit as st
from agent.executive_router import executive_router

from agent.ceo_agent import (
    ceo_analysis
)

from agent.finance_agent import (
    finance_analysis
)

from agent.marketing_agent import (
    marketing_analysis
)

from agent.data_scientist_agent import (
    data_scientist_analysis
)


from dashboard.finance_board import (
    show_finance_board
)

def show_ai_executive_board(df):

    st.title(
        "🤖 AI Executive Board"
    )
    revenue = df["Sales"].sum()

    profit = df["Profit"].sum()

    orders = len(df)

    customers = df["Customer ID"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Revenue",
            f"${revenue:,.0f}"
        )

    with col2:
        st.metric(
            "Profit",
            f"${profit:,.0f}"
        )

    with col3:
        st.metric(
            "Orders",
            orders
        )

    with col4:
        st.metric(
            "Customers",
            customers
        )

    st.divider()

    if st.button(
        "🚀 Executive Board Meeting"
    ):

        report = executive_router(df)

        st.subheader(
            "🚀 Executive Board Meeting"
        )

        st.markdown(report)

    st.markdown(
        """
        Executive AI Decision Center
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        ceo_btn = st.button(
            "👔 CEO Agent",
            use_container_width=True
        )

    with col2:

        finance_btn = st.button(
            "💰 Finance Agent",
            use_container_width=True
        )

    col3, col4 = st.columns(2)

    with col3:

        marketing_btn = st.button(
            "📈 Marketing Agent",
            use_container_width=True
        )

    with col4:

        ds_btn = st.button(
            "📊 Data Scientist",
            use_container_width=True
        )

    st.divider()

    if ceo_btn:

        st.success(
            ceo_analysis(df)
        )

    elif finance_btn:

        worst_state = (
            df.groupby("State")["Profit"]
            .sum()
            .sort_values()
            .index[0]
        )

        worst_state_profit = (
            df.groupby("State")["Profit"]
            .sum()
            .sort_values()
            .iloc[0]
        )

        worst_product = (
            df.groupby("Product Name")["Profit"]
            .sum()
            .sort_values()
            .index[0]
        )

        worst_product_profit = (
            df.groupby("Product Name")["Profit"]
            .sum()
            .sort_values()
            .iloc[0]
        )

        avg_discount = df["Discount"].mean()

        show_finance_board(
            worst_state,
            worst_state_profit,
            worst_product,
            worst_product_profit,
            avg_discount
        )

    elif marketing_btn:

        st.success(
            marketing_analysis(df)
        )

    elif ds_btn:

        st.success(
            data_scientist_analysis(df)
        )