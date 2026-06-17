import streamlit as st
import pandas as pd
import plotly.express as px

from util.logger import logger
from dashboard.dashboard import show_dashboard
from dashboard.analytics import show_analytics
from dashboard.time_intelligence import show_time_intelligence
from dashboard.root_cause import show_root_cause
from model.forecasting import show_forecasting
from agent.business_copilot import show_business_copilot
from report.pdf_report import generate_pdf_report
from dashboard.ai_executive_board import (
    show_ai_executive_board
)

from data.pipeline import (
    get_data_quality_report,
    clean_dataset
)
from data.features import (
    create_business_features
)
from dashboard.data_engineering import (
    show_data_engineering
)


from config.settings import (
    APP_NAME,
    APP_VERSION
)
from dashboard.model_registry import (
    show_model_registry
)
from util.error_handler import (
    handle_error
)
from dashboard.project_overview import (
    show_project_overview
)
from util.custom_css import load_css

@st.cache_data
def load_data(file):

    return pd.read_csv(
        file,
        encoding="latin1"
    )
st.set_page_config(
    page_title="AutoMind Enterprise",
    layout="wide"
)
st.markdown("""
    <style>

    /* Metric Cards */
    [data-testid="metric-container"] {
        background-color: #0E1525;
        border: 1px solid #26354A;
        padding: 20px;
        border-radius: 18px;
        transition: all 0.3s ease;
    }

    [data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0px 8px 25px rgba(0,255,150,0.15);
    }

    /* Buttons */
    .stButton button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        transform: scale(1.02);
    }

    /* Dataframes */
    [data-testid="stDataFrame"] {
        border-radius: 15px;
        overflow: hidden;
    }

    /* Headers */
    h1,h2,h3 {
        font-weight: 700;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0B1220;
    }

    /* Success Boxes */
    .stSuccess {
        border-radius: 15px;
    }

    </style>
    """, unsafe_allow_html=True)
load_css()
st.title(f"🚀 {APP_NAME}")
st.subheader("AI-Powered Business Intelligence Platform")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    logger.info(
        f"Dataset uploaded: {uploaded_file.name}"
    )

    df = load_data(
        uploaded_file
    )
    quality_report = get_data_quality_report(df)

    df = clean_dataset(df)
    df = create_business_features(df)
    # =========================
    # GLOBAL FILTERS
    # =========================
    st.sidebar.markdown(
        """
    # 🚀 AutoMind Enterprise

    ### AI Business Operating System
    """
    )

    st.sidebar.success(
        """
    🟢 SYSTEM STATUS

    • AI Agents Online

    • ML Models Active

    • Analytics Engine Running

    • Enterprise Version 2.0
    """
    )

    st.sidebar.markdown("---")

    st.sidebar.info(
        """
    ### Platform Capabilities

    ✅ Data Analytics

    ✅ Business Intelligence

    ✅ Machine Learning

    ✅ Generative AI

    ✅ Agentic AI

    ✅ Data Engineering
    """
    )

    st.sidebar.markdown("---")

    st.sidebar.markdown("# 🚀 AutoMind Enterprise")
    

    with st.sidebar.expander(
        "👨‍💻 Creator Information",
        expanded=False
    ):

        st.markdown("""
    ### 👨‍💻 Aditya Bhadauria

    AI & Data Science Enthusiast

    📧 [Email Contact](mailto:adityabhadauriawork@gmail.com)

    🔗 [LinkedIn Profile](https://www.linkedin.com/in/aditya-pratap-singh-bhadauria-a20198343/)

    💻 [GitHub Repository](https://github.com/adityabhadauriawork)

    🚀 Creator of AutoMind Enterprise
    """)
    

    st.sidebar.markdown("---")
    st.sidebar.subheader(
        "🚀 PROJECT OVERVIEW"
    )

    if st.sidebar.button(
        "AutoMind Architecture",
        use_container_width=True
    ):
        st.session_state.page = (
            "🚀 Project Overview"
        )

    st.sidebar.markdown("---")
    st.sidebar.subheader("🧠 AGENTIC AI")

    if st.sidebar.button(
        "AI Executive Board",
        use_container_width=True
    ):
        st.session_state.page = "🧠 AI Executive Board"
    st.sidebar.markdown("---")

    st.sidebar.subheader("🤖 GENERATIVE AI")

    if st.sidebar.button(
        "Business Copilot",
        use_container_width=True
    ):
        st.session_state.page = "🤖 Business Copilot"

    st.sidebar.markdown("---")

    st.sidebar.subheader("🏗 DATA ENGINEERING")

    if st.sidebar.button(
        "Data Engineering",
        use_container_width=True
    ):
        st.session_state.page = "🏗 Data Engineering"

    st.sidebar.markdown("---")

    st.sidebar.subheader("📊 BUSINESS INTELLIGENCE")

    if st.sidebar.button(
        "Executive Dashboard",
        use_container_width=True
    ):
        st.session_state.page = "📊 Executive Dashboard"

    if st.sidebar.button(
        "Analytics",
        use_container_width=True
    ):
        st.session_state.page = "📈 Analytics"

    if st.sidebar.button(
        "Time Intelligence",
        use_container_width=True
    ):
        st.session_state.page = "⏳ Time Intelligence"

    if st.sidebar.button(
        "Root Cause Analysis",
        use_container_width=True
    ):
        st.session_state.page = "🔍 Root Cause Analysis"

    st.sidebar.markdown("---")

    st.sidebar.subheader("🔮 MACHINE LEARNING")

    if st.sidebar.button(
        "Forecasting",
        use_container_width=True
    ):
        st.session_state.page = "🔮 Forecasting"
    if st.sidebar.button(
        "🧠 Model Registry",
        use_container_width=True
    ):
        st.session_state.page = "🧠 Model Registry"

    st.sidebar.markdown("---")

    st.sidebar.subheader("📈 DATA ANALYTICS")

    if st.sidebar.button(
        "Overview",
        use_container_width=True
    ):
        st.session_state.page = "🌍 Overview"

    st.sidebar.markdown("---")

    st.sidebar.subheader("📄 REPORTING")

    if st.sidebar.button(
        "AI Insights",
        use_container_width=True
    ):
        st.session_state.page = "📝 AI Insights"

    page = st.session_state.get(
        "page",
        "🤖 Business Copilot"
    )

    st.sidebar.markdown("---")

    st.sidebar.caption(
        """
    AutoMind Enterprise v2.0
    """
    )
    st.sidebar.header("🔍 Filters")

    selected_region = st.sidebar.selectbox(
        "Select Region",
        ["All"] + sorted(df["Region"].unique().tolist())
    )

    if selected_region != "All":
        df = df[df["Region"] == selected_region]
    
    selected_state = st.sidebar.selectbox(
        "Select State",
        ["All"] + sorted(df["State"].unique().tolist())
    )
    if selected_state != "All":
        df = df[df["State"] == selected_state]
    selected_category = st.sidebar.selectbox(
        "Select Category",
        ["All"] + sorted(df["Category"].unique().tolist())
    )

    if selected_category != "All":
        df = df[df["Category"] == selected_category]

    selected_subcategory = st.sidebar.selectbox(
        "Select Sub-Category",
        ["All"] + sorted(df["Sub-Category"].unique().tolist())
    )

    if selected_subcategory != "All":
        df = df[df["Sub-Category"] == selected_subcategory]

    st.success("Dataset uploaded successfully!")
    st.subheader("🛠 Data Quality Report")

    q1, q2, q3, q4, q5 = st.columns(5)

    with q1:
        st.metric(
            "Rows",
            quality_report["rows"]
        )

    with q2:
        st.metric(
            "Columns",
            quality_report["columns"]
        )

    with q3:
        st.metric(
            "Missing Values",
            quality_report["missing_values"]
        )

    with q4:
        st.metric(
            "Duplicates",
            quality_report["duplicate_rows"]
        )

    with q5:
        st.metric(
            "Quality Score",
            f'{quality_report["quality_score"]}/100'
        )

    st.divider()

    # =========================
    # DATA PREVIEW
    # =========================

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # =========================
    # DATASET INFO
    # =========================

    st.subheader("Dataset Information")

    info1, info2, info3 = st.columns(3)

    with info1:
        st.metric("Rows", df.shape[0])

    with info2:
        st.metric("Columns", df.shape[1])

    with info3:
        st.metric(
            "Missing Values",
            df.isnull().sum().sum()
        )

    st.subheader("Column Names")
    st.write(list(df.columns))

    # =========================
    # PAGE NAVIGATION
    # =========================

    if page == "🚀 Project Overview":

        show_project_overview()

        st.stop()
    
    elif page == "🧠 AI Executive Board":
        with st.spinner(
            "🧠 Activating Executive Agents..."
        ):
            import time
            time.sleep(1)

        show_ai_executive_board(df)

        st.stop()
    elif page == "🌍 Overview":

        show_dashboard(df)

        show_analytics(df)

        show_time_intelligence(df)
    elif page == "📊 Executive Dashboard":
        

        with st.spinner(
            "🚀 Loading Executive Dashboard..."
        ):
            import time
            time.sleep(1)

        show_dashboard(df)

        st.stop()

        st.subheader("🧠 Executive AI Summary")

        revenue = df["Sales"].sum()
        profit = df["Profit"].sum()

        top_category = (
            df.groupby("Category")["Sales"]
            .sum()
            .idxmax()
        )

        top_region = (
            df.groupby("Region")["Profit"]
            .sum()
            .idxmax()
        )

        if profit > 0:
            health = "🟢 Healthy"
        else:
            health = "🔴 Attention Required"

        st.success(
            f"""
        ### Executive Summary

        **Revenue:** ${revenue:,.0f}

        **Profit:** ${profit:,.0f}

        **Top Category:** {top_category}

        **Top Region:** {top_region}

        **Business Health:** {health}

        ### Recommendation

        Focus investment on **{top_category}** and optimize discount strategy to improve profitability.
        """
        )
        st.subheader("🏆 Enterprise Scorecard")

        score1, score2, score3, score4, score5 = st.columns(5)

        with score1:
            st.metric(
                "Data Quality",
                "100/100"
            )

        with score2:
            st.metric(
                "Forecasting",
                "88/100"
            )

        with score3:
            st.metric(
                "AI Readiness",
                "95/100"
            )

        with score4:
            st.metric(
                "Business Health",
                "92/100"
            )

        with score5:
            st.metric(
                "MLOps",
                "85/100"
            )

        st.success(
            """
        Overall Enterprise Score: 92/100

        AutoMind Enterprise is operating within healthy business and analytical thresholds.
        """
        )
        st.subheader("🏥 Enterprise Health Center")

        health1, health2, health3, health4 = st.columns(4)

        with health1:
            st.metric(
                "Business Health",
                "92/100"
            )

        with health2:
            st.metric(
                "Forecast Confidence",
                "88/100"
            )

        with health3:
                st.metric(
                "Data Quality",
                f"{quality_report['quality_score']}/100"
            )

        with health4:
            st.metric(
                "AI Readiness",
                "95/100"
            )

        st.success(
            """
        🟢 Enterprise Status: HEALTHY

        All major systems are operating within expected thresholds.
        """
        )
        st.subheader("📄 Executive PDF Report")

        if st.button("Generate Executive Report"):

            revenue = df["Sales"].sum()

            profit = df["Profit"].sum()

            top_category = (
                df.groupby("Category")["Sales"]
                .sum()
                .sort_values(ascending=False)
                .index[0]
            )

            top_region = (
                df.groupby("Region")["Profit"]
                .sum()
                .sort_values(ascending=False)
                .index[0]
            )

            pdf_file = generate_pdf_report(
                df,
                revenue,
                profit,
                top_category,
                top_region
            )

            with open(pdf_file, "rb") as file:

                st.download_button(
                    label="⬇ Download Executive Report",
                    data=file,
                    file_name=pdf_file,
                    mime="application/pdf"
                )

        st.stop()

    elif page == "📈 Analytics":
        show_analytics(df)
        st.stop()
    elif page == "🏗 Data Engineering":

        show_data_engineering(
            df,
            quality_report
        )

        st.stop()

    elif page == "⏳ Time Intelligence":
        show_time_intelligence(df)
        st.stop()

    elif page == "📝 AI Insights":
        pass
    elif page == "🔍 Root Cause Analysis":

        worst_states = (
            df.groupby("State")["Profit"]
            .sum()
            .sort_values()
            .head(5)
        )

        worst_categories = (
            df.groupby("Sub-Category")["Profit"]
            .sum()
            .sort_values()
            .head(5)
        )

        avg_discount = df["Discount"].mean()

        loss_orders = df[df["Profit"] < 0]

        worst_state = worst_states.index[0]

        worst_category = worst_categories.index[0]

        show_root_cause(
            worst_states,
            worst_categories,
            avg_discount,
            loss_orders,
            worst_state,
            worst_category
        )

        st.stop()
    elif page == "🔮 Forecasting":

        logger.info(
            "Forecasting module opened"
        )
        with st.spinner(
            "🔮 Initializing Forecast Engine..."
        ):
            import time
            time.sleep(1)

        show_forecasting(df)

        st.stop()
    elif page == "🧠 Model Registry":

        show_model_registry()

        st.stop()
    elif page == "🤖 Business Copilot":
        
        logger.info(
            "Business Copilot opened"
        )
        with st.spinner(
            "🤖 Starting Business Copilot..."
        ):
            import time
            time.sleep(1)

        show_business_copilot(df)

        st.stop()

    # =========================
    # PROFIT BY REGION
    # =========================

    st.subheader("🌎 Profit by Region")

    region_profit = (
        df.groupby("Region")["Profit"]
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        region_profit,
        names="Region",
        values="Profit",
        title="Profit Distribution by Region"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # =========================
    # TOP PRODUCTS
    # =========================

    st.subheader("🏆 Top 10 Products")

    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig3 = px.bar(
        top_products,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top 10 Products by Revenue"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # =========================
    # TOP STATES
    # =========================

    st.subheader("🏙️ Top States")

    state_sales = (
        df.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig4 = px.bar(
        state_sales,
        x="State",
        y="Sales",
        title="Top States by Revenue"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    # =========================
    # AI BUSINESS INSIGHTS
    # =========================

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    top_category = category_sales.loc[
        category_sales["Sales"].idxmax()
    ]

    top_region = region_profit.loc[
        region_profit["Profit"].idxmax()
    ]

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()

    st.subheader("🤖 AI Business Insights")

    st.success(
        f"""
        Top Revenue Category: {top_category['Category']}

        Highest Profit Region: {top_region['Region']}

        Total Revenue: ${total_sales:,.0f}

        Total Profit: ${total_profit:,.0f}
        """
    )
    

    # =========================
    # ROOT CAUSE ANALYSIS
    # =========================

    st.subheader("🔍 Root Cause Analysis Engine")

    worst_states = (
        df.groupby("State")["Profit"]
        .sum()
        .sort_values()
        .head(5)
    )

    st.write("### Worst Profit States")

    st.dataframe(
        worst_states.reset_index()
    )

    worst_categories = (
        df.groupby("Sub-Category")["Profit"]
        .sum()
        .sort_values()
        .head(5)
    )

    st.write("### Worst Profit Sub-Categories")

    st.dataframe(
        worst_categories.reset_index()
    )

    avg_discount = df["Discount"].mean()

    st.write(
        f"Average Discount: {avg_discount:.2%}"
    )

    loss_orders = df[df["Profit"] < 0]

    st.write(
        f"Loss Making Orders: {len(loss_orders)}"
    )

    worst_state = worst_states.index[0]
    worst_category = worst_categories.index[0]

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
    if page == "🔍 Root Cause Analysis":

        st.stop()