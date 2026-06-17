def get_top_loss_products(df):

    return (
        df.groupby("Product Name")["Profit"]
        .sum()
        .sort_values()
        .head(10)
    )


def get_top_loss_categories(df):

    return (
        df.groupby("Sub-Category")["Profit"]
        .sum()
        .sort_values()
        .head(10)
    )


def get_worst_states(df):

    return (
        df.groupby("State")["Profit"]
        .sum()
        .sort_values()
        .head(10)
    )
def get_top_states(df):

    return (
        df.groupby("State")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
def get_top_categories(df):

    return (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )