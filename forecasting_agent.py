class ForecastingAgent:
    def analyse(self, df, selected_metric):
        latest_value = round(df[selected_metric].mean(), 2)

        forecast_3_month = round(latest_value * 1.05, 2)
        forecast_6_month = round(latest_value * 1.10, 2)
        forecast_12_month = round(latest_value * 1.20, 2)

        return {
            "role": "Forecasting Agent",
            "current_value": latest_value,
            "forecast_3_month": forecast_3_month,
            "forecast_6_month": forecast_6_month,
            "forecast_12_month": forecast_12_month,
            "insight": (
                f"Based on the current average value of {latest_value}, "
                f"the system estimates a 3-month forecast of {forecast_3_month}, "
                f"a 6-month forecast of {forecast_6_month}, and a 12-month forecast of {forecast_12_month}."
            )
        }
