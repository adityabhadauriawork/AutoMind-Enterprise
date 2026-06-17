import pandas as pd


def create_business_features(df):

    df = df.copy()

    # Profit Margin %

    df["Profit Margin"] = (
        df["Profit"] /
        df["Sales"]
    ) * 100

    # Revenue Per Order

    df["Revenue Per Order"] = (
        df["Sales"]
    )

    # Discount Impact

    df["Discount Impact"] = (
        df["Sales"] *
        df["Discount"]
    )

    # Profit Per Customer

    df["Profit Per Customer"] = (
        df["Profit"]
    )

    # High Discount Flag

    df["High Discount Flag"] = (
        df["Discount"] > 0.20
    ).astype(int)

    return df