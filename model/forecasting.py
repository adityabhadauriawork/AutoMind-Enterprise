import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from config.settings import (
    RF_ESTIMATORS,
    RANDOM_STATE
)

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    root_mean_squared_error
)


from database.sqlite_manager import (
    save_forecast,
    save_model_metrics
)


def show_forecasting(df):

    st.header("🔮 Forecasting Engine")
    st.write("STEP 1")

    # =========================
    # PREPARE DATA
    # =========================

    df = df.copy()

    df["Order Date"] = pd.to_datetime(
        df["Order Date"]
    )

    monthly_sales = (
        df.groupby(
            pd.Grouper(
                key="Order Date",
                freq="ME"
            )
        )["Sales"]
        .sum()
        .reset_index()
    )

    st.subheader("📊 Historical Monthly Sales")

    st.dataframe(
        monthly_sales.tail(12)
    )

    # =========================
    # MACHINE LEARNING MODEL
    # =========================

    monthly_sales["Month_Number"] = np.arange(
        len(monthly_sales)
    )
    monthly_sales["Previous_Month_Sales"] = (
        monthly_sales["Sales"]
        .shift(1)
    )

    monthly_sales = (
        monthly_sales
        .dropna()
    )

    X = monthly_sales[
        [
            "Month_Number",
            "Previous_Month_Sales"
        ]
    ]
    y = monthly_sales["Sales"]
    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )
    )

    # =========================
    # LINEAR REGRESSION
    # =========================

    linear_model = LinearRegression()

    linear_model.fit(
        X_train,
        y_train
    )
    linear_predictions = linear_model.predict(
        X_test
    )
    # =========================
    # RANDOM FOREST
    # =========================

    rf_model = RandomForestRegressor(
        n_estimators=RF_ESTIMATORS,
        random_state=RANDOM_STATE
    )

    rf_model.fit(
        X_train,
        y_train
    )
    rf_predictions = rf_model.predict(
        X_test
    )    
    
    # =========================
    # MODEL METRICS
    # =========================

    # =========================
    # MODEL METRICS
    # =========================

    linear_r2 = r2_score(
        y_test,
        linear_predictions
    )

    rf_r2 = r2_score(
        y_test,
        rf_predictions
    )
    linear_mae = mean_absolute_error(
        y_test,
        linear_predictions
    )

    rf_mae = mean_absolute_error(
        y_test,
        rf_predictions
    )

    linear_rmse = root_mean_squared_error(
        y_test,
        linear_predictions
    )

    rf_rmse = root_mean_squared_error(
        y_test,
        rf_predictions
    )
    # save_model_metrics(
    #     "Linear Regression",
    #     "v1",
    #     linear_r2,
    #     linear_mae,
    #     linear_rmse
    # )

    # save_model_metrics(
    #     "Random Forest",
    #     "v1",
    #     rf_r2,
    #     rf_mae,
    #     rf_rmse
    # )

    # =========================
    # FUTURE PREDICTIONS
    # =========================
    st.write("STEP 2")
    future_months = st.slider(
        "Forecast Horizon (Months)",
        min_value=1,
        max_value=24,
        value=6
    )

    future_index = np.arange(
        len(monthly_sales),
        len(monthly_sales) + future_months
    )

    last_sales = monthly_sales["Sales"].iloc[-1]

    future_features = pd.DataFrame({
        "Month_Number": future_index,
        "Previous_Month_Sales": [last_sales] * len(future_index)
    })

    future_sales = rf_model.predict(
        future_features
    )

    future_dates = pd.date_range(
        start=monthly_sales["Order Date"].max(),
        periods=future_months + 1,
        freq="ME"
    )[1:]

    forecast_df = pd.DataFrame(
        {
            "Order Date": future_dates,
            "Predicted Sales": future_sales
        }
    )

    if st.button("Generate Forecast"):

        for _, row in forecast_df.iterrows():

            save_forecast(
                str(row["Order Date"]),
                float(row["Predicted Sales"])
            )

        st.success("Forecast Saved")

    # =========================
    # FORECAST TABLE
    # =========================

    st.subheader("📊 Model Performance")
    comparison_df = pd.DataFrame(
        {
            "Model": [
                "Linear Regression",
                "Random Forest"
            ],

            "R²": [
                linear_r2,
                rf_r2
            ],

            "MAE": [
                linear_mae,
                rf_mae
            ],

            "RMSE": [
                linear_rmse,
                rf_rmse
            ]
        }
    )

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            "Linear Regression R²",
            f"{linear_r2:.3f}"
        )

    with m2:
        st.metric(
            "Random Forest R²",
            f"{rf_r2:.3f}"
        )

    with m3:
        st.metric(
            "Best Model",
            "Random Forest"
            if rf_r2 > linear_r2
            else "Linear Regression"
        )
    st.dataframe(
        comparison_df,
        use_container_width=True
    )

    st.subheader("🔮 Next 6 Months Forecast")

    st.dataframe(
        forecast_df
    )

    # =========================
    # FORECAST CHART
    # =========================

    historical_chart = monthly_sales[
        ["Order Date", "Sales"]
    ].copy()

    historical_chart.columns = [
        "Order Date",
        "Value"
    ]

    historical_chart["Type"] = "Historical"

    forecast_chart = forecast_df.copy()

    forecast_chart.columns = [
        "Order Date",
        "Value"
    ]

    forecast_chart["Type"] = "Forecast"

    chart_df = pd.concat(
        [
            historical_chart,
            forecast_chart
        ]
    )

    fig = px.line(
        chart_df,
        x="Order Date",
        y="Value",
        color="Type",
        markers=True,
        title="Sales Forecast"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )