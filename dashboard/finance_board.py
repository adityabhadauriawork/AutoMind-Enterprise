import streamlit as st


def show_finance_board(
    worst_state,
    worst_state_profit,
    worst_product,
    worst_product_profit,
    avg_discount
):

    st.subheader("💰 Finance Executive Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Worst State",
            worst_state
        )

    with col2:
        st.metric(
            "Worst Product",
            worst_product[:20]
        )

    with col3:
        st.metric(
            "Avg Discount",
            f"{avg_discount:.2%}"
        )

    st.divider()

    st.error(
        f"""
        Financial Alert

        • {worst_state} is generating the highest losses.

        • {worst_product} is the most unprofitable product.

        • Average discount is {avg_discount:.2%}.

        Recommendation:

        Reduce discount leakage,
        review pricing strategy,
        and investigate loss-making products.
        """
    )