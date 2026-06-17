def marketing_analysis(df):

    top_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    top_category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .iloc[0]
    )

    top_product = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    top_product_sales = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .iloc[0]
    )

    top_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .index[0]
    )

    return f"""
MARKETING ANALYSIS

Top Category

{top_category}

Revenue:

${top_category_sales:,.0f}

Top Product

{top_product}

Revenue:

${top_product_sales:,.0f}

Top Region

{top_region}

Recommendations

Increase marketing spend
on the top category.

Promote the highest
revenue-generating product.

Focus campaigns on
the strongest region.
"""