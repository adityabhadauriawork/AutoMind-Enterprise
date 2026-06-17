import streamlit as st


def show_data_engineering(
    df,
    quality_report
):

    st.title(
        "🛠 Data Engineering Center"
    )

    st.subheader(
        "Dataset Quality Overview"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Missing Values",
            quality_report["missing_values"]
        )

    with col2:
        st.metric(
            "Duplicates",
            quality_report["duplicate_rows"]
        )

    with col3:
        st.metric(
            "Quality Score",
            f'{quality_report["quality_score"]}/100'
        )

    st.divider()

    st.subheader(
        "Engineered Features"
    )

    st.markdown("""
    ### Created Features

    ✅ Profit Margin

    ✅ Revenue Per Order

    ✅ Discount Impact

    ✅ Profit Per Customer

    ✅ High Discount Flag
    """)

    st.dataframe(
        df[
            [
                "Profit Margin",
                "Revenue Per Order",
                "Discount Impact",
                "Profit Per Customer",
                "High Discount Flag"
            ]
        ].head()
    )