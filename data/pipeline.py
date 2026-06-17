import pandas as pd


def get_data_quality_report(df):

    total_rows = len(df)

    total_columns = len(df.columns)

    missing_values = df.isnull().sum().sum()

    duplicate_rows = df.duplicated().sum()

    quality_score = 100

    quality_score -= min(
        (missing_values / max(total_rows, 1)) * 10,
        40
    )

    quality_score -= min(
        (duplicate_rows / max(total_rows, 1)) * 10,
        40
    )

    quality_score = max(
        round(quality_score, 2),
        0
    )

    return {
        "rows": total_rows,
        "columns": total_columns,
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows,
        "quality_score": quality_score
    }


def clean_dataset(df):

    df = df.drop_duplicates()

    return df