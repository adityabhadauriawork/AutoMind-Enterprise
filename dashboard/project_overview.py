import streamlit as st


def show_project_overview():

    st.markdown("""
    <div style="
    background: linear-gradient(90deg,#0f172a,#1e293b);
    padding:30px;
    border-radius:20px;
    border:1px solid #334155;
    margin-bottom:20px;
    ">

    <h1 style="color:white;">
    🚀 AutoMind Enterprise
    </h1>
    <p style="
    font-size:22px;
    font-style:italic;
    color:#94a3b8;
    margin-top:-10px;
    ">
    Built by Aditya Bhadauria
    </p>
    <h3 style="color:#94a3b8;">
    AI Business Intelligence Operating System
    </h3>

    <p style="color:#cbd5e1; font-size:18px;">
    Combining Data Engineering, Analytics,
    Business Intelligence, Machine Learning,
    MLOps, Generative AI and Agentic AI
    into a unified enterprise platform.
    </p>

    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Modules",
            "10+"
        )

    with col2:
        st.metric(
            "AI Agents",
            "4"
        )

    with col3:
        st.metric(
            "ML Models",
            "2"
        )

    with col4:
        st.metric(
            "MLOps Features",
            "3"
        )

    st.markdown("""
# AI-Powered Business Intelligence Platform

AutoMind Enterprise is an end-to-end AI Business Intelligence ecosystem that combines:

- Data Analytics
- Business Intelligence
- Data Engineering
- Machine Learning
- MLOps
- Generative AI
- Agentic AI

into a single enterprise-grade platform.
""")

    st.divider()

    st.header("🏗 System Architecture")

    st.code("""
CSV / Excel Dataset
          │
          ▼
┌────────────────────┐
│ DATA ENGINEERING   │
│ Validation         │
│ Profiling          │
│ Quality Checks     │
└────────────────────┘
          │
          ▼
┌────────────────────┐
│ DATA ANALYTICS     │
│ KPIs              │
│ Trends            │
│ Insights          │
└────────────────────┘
          │
          ▼
┌────────────────────┐
│ BUSINESS           │
│ INTELLIGENCE       │
│ Dashboards         │
│ Root Cause         │
│ Time Intelligence  │
└────────────────────┘
          │
          ▼
┌────────────────────┐
│ MACHINE LEARNING   │
│ Forecasting Engine │
│ Model Comparison   │
└────────────────────┘
          │
          ▼
┌────────────────────┐
│ MLOPS              │
│ Model Registry     │
│ Version Control    │
│ Performance Store  │
└────────────────────┘
          │
          ▼
┌────────────────────┐
│ GENERATIVE AI      │
│ Business Copilot   │
└────────────────────┘
          │
          ▼
┌────────────────────┐
│ AGENTIC AI         │
│ CEO Agent          │
│ Finance Agent      │
│ Marketing Agent    │
│ Data Scientist     │
└────────────────────┘
""")

    st.divider()

    st.header("🧠 Core Modules")

    st.markdown("""

### 📈 Data Analytics

Business KPIs, revenue trends, profitability analysis and performance monitoring.

### 📊 Business Intelligence

Executive dashboards, time intelligence and root cause analysis.

### 🏗 Data Engineering

Dataset validation, profiling, quality monitoring and preprocessing.

### 🔮 Machine Learning

Sales forecasting using multiple machine learning models.

### 🧠 MLOps

Model registry, model tracking, performance monitoring and champion model selection.

### 🤖 Generative AI

Business Copilot for natural language business interaction.

### 👔 Agentic AI

AI Executive Board consisting of:

- CEO Agent
- Finance Agent
- Marketing Agent
- Data Scientist Agent

Each agent performs specialized business decision making.

""")

    st.divider()

    st.header("⚙ Technology Stack")

    st.code("""
Frontend
--------
Streamlit
Plotly
Custom CSS

Backend
-------
Python
Pandas
NumPy

Database
--------
SQLite

Machine Learning
---------------
Scikit-Learn

AI Layer
--------
Rule-Based AI
Multi-Agent Architecture

Testing
-------
PyTest

Logging
-------
Python Logging
""")

    st.divider()

    st.header("🎯 Key Business Capabilities")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
    ### Business Intelligence

    ✅ Executive Dashboard

    ✅ Revenue Analytics

    ✅ Profit Analytics

    ✅ Customer Analytics

    ✅ Regional Performance

    ✅ Product Performance
    """)

        st.info("""
    ### Advanced Analytics

    ✅ Root Cause Analysis

    ✅ Time Intelligence

    ✅ Trend Analysis

    ✅ KPI Monitoring
    """)

    with col2:

        st.info("""
    ### Machine Learning

    ✅ Sales Forecasting

    ✅ Model Comparison

    ✅ Performance Evaluation

    ✅ Champion Model Selection
    """)

        st.info("""
    ### AI Layer

    ✅ Business Copilot

    ✅ AI Executive Board

    ✅ CEO Agent

    ✅ Finance Agent

    ✅ Marketing Agent

    ✅ Data Scientist Agent
    """)
        st.divider()

    st.header("🏆 Project Highlights")

    st.success("""
    ✔ End-to-End AI Business Intelligence Platform

    ✔ Data Engineering Pipeline

    ✔ Interactive BI Dashboards

    ✔ Machine Learning Forecasting Engine

    ✔ MLOps Model Registry

    ✔ Generative AI Business Copilot

    ✔ Agentic AI Executive Board

    ✔ Executive PDF Reporting

    ✔ Enterprise Modular Architecture

    ✔ Production-Ready Deployment
    """)

    st.success("""
AutoMind Enterprise transforms raw business data into
actionable executive decisions using Data Engineering,
Analytics, Machine Learning, MLOps, Generative AI
and Agentic AI.
""")