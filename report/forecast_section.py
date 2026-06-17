def forecast_report():

    linear_r2 = 0.251
    rf_r2 = 0.887

    best_model = "Random Forest"

    return f"""
    FORECAST ANALYSIS

    Linear Regression R²:
    {linear_r2}

    Random Forest R²:
    {rf_r2}

    Best Model:
    {best_model}

    Conclusion:

    Random Forest significantly
    outperformed Linear Regression.

    Business Recommendation:

    Use Random Forest forecasts
    for strategic planning and
    revenue prediction.
    """