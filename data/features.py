def create_business_features(df):

    df = df.copy()

    required_columns = [
        "Sales",
        "Profit",
        "Discount"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    df["Profit Margin"] = (
        df["Profit"] /
        df["Sales"]
    ) * 100

    df["Revenue Per Order"] = df["Sales"]

    df["Discount Impact"] = (
        df["Sales"] *
        df["Discount"]
    )

    df["Profit Per Customer"] = (
        df["Profit"]
    )

    df["High Discount Flag"] = (
        df["Discount"] > 0.20
    ).astype(int)

    return df