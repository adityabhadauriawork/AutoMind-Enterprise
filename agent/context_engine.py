def generate_state_context(df, state_name):

    state_df = df[
        df["State"].str.lower()
        == state_name.lower()
    ]

    if state_df.empty:

        return f"""
        No data found for {state_name}.
        """

    total_sales = (
        state_df["Sales"]
        .sum()
    )

    total_profit = (
        state_df["Profit"]
        .sum()
    )

    avg_discount = (
        state_df["Discount"]
        .mean()
    )

    top_categories = (
        state_df.groupby("Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    worst_subcategories = (
        state_df.groupby("Sub-Category")["Profit"]
        .sum()
        .sort_values()
        .head(10)
    )

    top_products = (
        state_df.groupby("Product Name")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    worst_products = (
        state_df.groupby("Product Name")["Profit"]
        .sum()
        .sort_values()
        .head(10)
    )

    return f"""
    STATE ANALYSIS

    State:
    {state_name}

    Total Sales:
    {total_sales:,.2f}

    Total Profit:
    {total_profit:,.2f}

    Average Discount:
    {avg_discount:.2f}

    MOST PROFITABLE CATEGORIES

    {top_categories.to_string()}

    BIGGEST LOSS-MAKING SUB-CATEGORIES

    {worst_subcategories.to_string()}

    MOST PROFITABLE PRODUCTS

    {top_products.to_string()}

    BIGGEST LOSS-MAKING PRODUCTS

    {worst_products.to_string()}
    """
def generate_product_context(df):

    top_products = (
        df.groupby("Product Name")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
    )

    worst_products = (
        df.groupby("Product Name")["Profit"]
        .sum()
        .sort_values()
        .head(15)
    )

    return f"""
    PRODUCT ANALYSIS

    TOP PRODUCTS

    {top_products.to_string()}

    WORST PRODUCTS

    {worst_products.to_string()}
    """
def generate_executive_context(df):

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

    return f"""
    EXECUTIVE OVERVIEW

    Total Revenue:
    {total_revenue:,.2f}

    Total Profit:
    {total_profit:,.2f}

    Top Revenue Category:
    {top_category}

    Most Profitable Region:
    {top_region}
    """