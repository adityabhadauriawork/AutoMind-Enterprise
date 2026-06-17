import streamlit as st


def show_root_cause(
    worst_states,
    worst_categories,
    avg_discount,
    loss_orders,
    worst_state,
    worst_category
):

    st.header("🔍 Root Cause Analysis Engine")

    st.write("### Worst Profit States")
    st.dataframe(
        worst_states.reset_index()
    )

    st.write("### Worst Profit Sub-Categories")
    st.dataframe(
        worst_categories.reset_index()
    )

    st.write(
        f"Average Discount: {avg_discount:.2%}"
    )

    st.write(
        f"Loss Making Orders: {len(loss_orders)}"
    )

    st.error(
        f"""
        AutoMind Analysis:

        Most problematic state:
        {worst_state}

        Most problematic sub-category:
        {worst_category}

        Average discount level:
        {avg_discount:.2%}

        Negative profit orders:
        {len(loss_orders)}
        """
    )