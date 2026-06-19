import streamlit as st
import requests
import json
import google.generativeai as genai

from agent.agent_router import route_agent

from agent.analytics_engine import (
    get_top_loss_products,
    get_top_loss_categories,
    get_worst_states
)

from agent.context_engine import (
    generate_state_context,
    generate_product_context,
    generate_executive_context
)
from agent.query_router import detect_intent, extract_state

def generate_business_context(df):

        total_revenue = df["Sales"].sum()

        total_profit = df["Profit"].sum()

        total_orders = df["Order ID"].nunique()

        total_customers = df["Customer Name"].nunique()

        top_categories = (
            df.groupby("Category")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
        )

        top_regions = (
            df.groupby("Region")["Profit"]
            .sum()
            .sort_values(ascending=False)
        )

        top_states = (
            df.groupby("State")["Profit"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        worst_states = (
            df.groupby("State")["Profit"]
            .sum()
            .sort_values()
            .head(10)
        )

        top_products = (
            df.groupby("Product Name")["Profit"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        worst_products = (
            df.groupby("Product Name")["Profit"]
            .sum()
            .sort_values()
            .head(10)
        )

        avg_discount = df["Discount"].mean()

        context = f"""

        BUSINESS OVERVIEW

        Total Revenue:
        {total_revenue:,.2f}

        Total Profit:
        {total_profit:,.2f}

        Total Orders:
        {total_orders}

        Total Customers:
        {total_customers}

        Average Discount:
        {avg_discount:.2f}

        TOP CATEGORIES

        {top_categories.to_string()}

        TOP REGIONS

        {top_regions.to_string()}

        TOP STATES BY PROFIT

        {top_states.to_string()}

        WORST STATES BY PROFIT

        {worst_states.to_string()}

        TOP PRODUCTS

        {top_products.to_string()}

        WORST PRODUCTS

        {worst_products.to_string()}
        """

        return context

    
def ask_llama(prompt):

    st.write(
        "API Key Loaded:",
        "GEMINI_API_KEY" in st.secrets
    )

    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel(
        "gemini-1.5-flash"
    )

    response = model.generate_content(
        prompt
    )

    return response.text

def show_business_copilot(df):

    st.header("🤖 AutoMind Business Copilot")

    user_question = st.text_input(
        "Ask a business question"
    )

    if user_question:

        question = user_question.lower()

        # =========================
        # TOP CATEGORY
        # =========================

        if "category" in question and (
            "revenue" in question
            or "sales" in question
        ):

            category_sales = (
                df.groupby("Category")["Sales"]
                .sum()
                .sort_values(ascending=False)
            )

            top_category = category_sales.index[0]

            top_sales = category_sales.iloc[0]

            st.success(
                f"""
                Top Revenue Category:
                {top_category}

                Revenue:
                ${top_sales:,.0f}
                """
            )

        elif "region" in question and (
            "profit" in question
            or "profitable" in question
        ):

            region_profit = (
                df.groupby("Region")["Profit"]
                .sum()
                .sort_values(ascending=False)
            )

            st.success(
                f"""
                Most Profitable Region:

                {region_profit.index[0]}

                Profit:
                ${region_profit.iloc[0]:,.0f}
                """
            )

        elif "worst state" in question:

            worst_state = (
                df.groupby("State")["Profit"]
                .sum()
                .sort_values()
                .index[0]
            )

            st.error(
                f"Worst Profit State: {worst_state}"
            )

        elif (
            "worst sub-category" in question
            or "worst category" in question
        ):

            worst_sub = (
                df.groupby("Sub-Category")["Profit"]
                .sum()
                .sort_values()
                .index[0]
            )

            st.error(
                f"Worst Sub-Category: {worst_sub}"
            )

        elif (
            "total revenue" in question
            or "revenue" in question
        ):

            revenue = df["Sales"].sum()

            st.success(
                f"Total Revenue: ${revenue:,.0f}"
            )
        elif (
            "executive summary" in question
            or "summary" in question
        ):

            total_revenue = df["Sales"].sum()

            total_profit = df["Profit"].sum()

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

            worst_state = (
                df.groupby("State")["Profit"]
                .sum()
                .sort_values()
                .index[0]
            )

            worst_subcategory = (
                df.groupby("Sub-Category")["Profit"]
                .sum()
                .sort_values()
                .index[0]
            )

            st.success(
                f"""
                EXECUTIVE SUMMARY

                Total Revenue:
                ${total_revenue:,.0f}

                Total Profit:
                ${total_profit:,.0f}

                Top Revenue Category:
                {top_category}

                Most Profitable Region:
                {top_region}

                Worst Profit State:
                {worst_state}

                Worst Sub-Category:
                {worst_subcategory}

                Recommendation:
                Focus on high-performing categories
                while investigating losses in
                low-performing regions and products.
                """
            )

        else:
            intent = detect_intent(user_question)

            st.info(f"Detected Intent: {intent}")

            if intent == "state":

                state_name = extract_state(user_question)

                if state_name:

                    business_context = generate_state_context(
                        df,
                        state_name
                    )
                    st.text_area(
                        "Debug Context",
                        business_context,
                        height=400
                    )

                else:

                    business_context = generate_business_context(df)
            elif intent == "product":

                business_context = generate_product_context(df)
            elif intent == "executive":

                business_context = generate_executive_context(df)

            else:

                business_context = generate_business_context(df)

            loss_products = get_top_loss_products(df)

            loss_categories = get_top_loss_categories(df)

            worst_states = get_worst_states(df)

            prompt = f"""
            You are AutoMind Enterprise AI.

            You are an expert in:

            - Business Intelligence
            - Data Analytics
            - Data Science
            - Forecasting
            - Executive Reporting

            BUSINESS CONTEXT:

            {business_context}

            ANALYTICS ENGINE FINDINGS

            TOP LOSS PRODUCTS

            {loss_products.to_string()}

            TOP LOSS CATEGORIES

            {loss_categories.to_string()}

            WORST STATES

            {worst_states.to_string()}

            USER QUESTION:

            {user_question}

            IMPORTANT RULES:

            1. Use ONLY the provided business context.

            2. Every claim must reference numbers,
            products, categories or states from
            the context.

            3. Never suggest:
            - market conditions
            - competition
            - economy
            - regulations
            unless they are explicitly present in the context.

            4. Identify the biggest losses first.

            5. Mention specific products,
            sub-categories and profit values.

            6. Explain findings using the data.

            7. If losses are visible,
            identify the largest contributors.

            8. Do not say
            "more analysis is needed"
            unless information is genuinely missing.
            """

            with st.spinner("🧠 AutoMind AI is analyzing your business..."):

                agent_response = route_agent(
                    user_question,
                    df
                )

                st.info(agent_response)

                answer = ask_llama(prompt)

                st.success(answer)

