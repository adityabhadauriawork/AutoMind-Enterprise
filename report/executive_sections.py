def executive_summary(
    revenue,
    profit,
    orders,
    customers
):

    return f"""
    The business generated
    ${revenue:,.0f} in revenue
    and ${profit:,.0f} in profit.

    Total orders processed:
    {orders:,}

    Total customers served:
    {customers:,}

    Management should focus on
    scaling profitable regions
    and improving loss-making
    products and categories.
    """

def ai_executive_insights(
    revenue,
    profit,
    top_category,
    top_region
):

    return f"""
    AI EXECUTIVE INSIGHTS

    Revenue Performance:

    The business generated
    ${revenue:,.0f}
    in revenue.

    Category Insight:

    {top_category}
    is the strongest revenue driver.

    Regional Insight:

    {top_region}
    is the most profitable region.

    Executive Recommendation:

    Continue investing in
    high-performing categories
    while reducing exposure
    to low-profit products.

    Strategic Priority:

    Improve performance in
    loss-making products and
    expand profitable regions.
    """
def forecast_summary():

    return """
    FORECAST RESULTS

    Forecast Model:
    Random Forest Regressor

    Model Performance:

    Random Forest achieved
    significantly higher accuracy
    compared to Linear Regression.

    Business Outlook:

    Current trends indicate
    continued revenue growth.

    Recommendation:

    Continue investing in
    high-performing products
    and profitable regions.

    Strategic Focus:

    Improve low-performing
    products while scaling
    top revenue categories.
    """