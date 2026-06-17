def finance_analysis(df):

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

    return f"""
FINANCE ANALYSIS

Financial Risks

Worst State:

{worst_state}

Profit:

${worst_state_profit:,.0f}

Worst Product:

{worst_product}

Profit:

${worst_product_profit:,.0f}

Average Discount:

{avg_discount:.2%}

Recommendations

Reduce losses in
low-performing states.

Review pricing and
discount strategy.

Investigate products
with persistent losses.
"""