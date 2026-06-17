def ceo_analysis(df):

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

    return f"""
CEO STRATEGIC ANALYSIS

Business Overview

Total Revenue:
${total_revenue:,.0f}

Total Profit:
${total_profit:,.0f}

Biggest Risk

Worst Profit State:
{worst_state}

Worst Sub-Category:
{worst_subcategory}

Growth Opportunities

Top Revenue Category:
{top_category}

Most Profitable Region:
{top_region}

Strategic Recommendation

Expand high-performing categories
while reducing losses in
underperforming states and
sub-categories.
"""