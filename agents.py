class DataScientistAgent:
    def analyse(self, df, selected_metric):
        return {
            "role": "Data Scientist Agent",
            "insight": f"The dataset contains {df.shape[0]} records and {df.shape[1]} columns. The selected metric '{selected_metric}' is suitable for business performance analysis.",
            "evidence": f"Total {selected_metric}: {round(df[selected_metric].sum(), 2)}, Average {selected_metric}: {round(df[selected_metric].mean(), 2)}"
        }


class RevenueOptimizationAgent:
    def analyse(self, df, selected_metric):
        total_value = df[selected_metric].sum()
        average_value = df[selected_metric].mean()

        return {
            "role": "Revenue Optimization Agent",
            "insight": f"The metric '{selected_metric}' shows revenue or performance potential that should be reviewed for growth opportunities.",
            "recommendation": f"Focus on segments, products, or customers contributing above the average value of {round(average_value, 2)}.",
            "estimated_impact": "Medium to High"
        }


class RiskOfficerAgent:
    def analyse(self, df, selected_metric):
        missing_values = df[selected_metric].isnull().sum()
        min_value = df[selected_metric].min()

        if missing_values > 0:
            risk = f"{missing_values} missing values detected in {selected_metric}."
        elif min_value < 0:
            risk = f"Negative values detected in {selected_metric}, which may indicate loss, refund, or data quality issues."
        else:
            risk = f"No immediate data quality risk detected for {selected_metric}."

        return {
            "role": "Risk Officer Agent",
            "risk_assessment": risk,
            "risk_level": "Medium" if missing_values > 0 or min_value < 0 else "Low"
        }


class StrategyAgent:
    def analyse(self, revenue_output, risk_output):
        return {
            "role": "Strategy Agent",
            "strategic_view": "The business should balance revenue growth opportunities with risk-aware execution.",
            "priority": "Review high-performing areas first, then investigate weak or risky segments."
        }


class CEODecisionAgent:
    def analyse(self, data_output, revenue_output, risk_output, strategy_output):
        return {
            "role": "CEO Decision Agent",
            "final_decision": "Proceed with deeper business analysis before making strategic changes.",
            "executive_summary": "The Cognitive Enterprise Twin has identified initial performance patterns, revenue opportunities, and risk signals. The recommended next step is to prioritise high-value areas while monitoring operational and financial risks."
        }
