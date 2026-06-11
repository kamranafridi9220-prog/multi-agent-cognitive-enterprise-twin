import pandas as pd
import numpy as np


class EnterpriseHealthScoreEngine:
    """
    Calculates an overall Enterprise Health Score based on
    financial, revenue, growth, risk, and operational indicators.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def _safe_score(self, value, min_value, max_value):
        if max_value == min_value:
            return 50
        score = ((value - min_value) / (max_value - min_value)) * 100
        return max(0, min(100, score))

    def calculate_health_score(self):
        numeric_cols = self.df.select_dtypes(include=np.number).columns.tolist()

        if len(numeric_cols) == 0:
            return {
                "overall_score": 50,
                "status": "Insufficient Data",
                "financial_health": 50,
                "revenue_health": 50,
                "growth_health": 50,
                "risk_health": 50,
                "operational_health": 50,
                "strengths": ["Dataset uploaded successfully"],
                "weaknesses": ["No numeric business metrics found"],
                "recommendation": "Upload a dataset with revenue, cost, sales, profit, or performance metrics."
            }

        total_values = self.df[numeric_cols].sum(numeric_only=True)
        mean_values = self.df[numeric_cols].mean(numeric_only=True)
        std_values = self.df[numeric_cols].std(numeric_only=True).fillna(0)

        financial_health = 70
        revenue_health = 70
        growth_health = 65
        risk_health = 70
        operational_health = 68

        revenue_cols = [c for c in numeric_cols if any(x in c.lower() for x in ["revenue", "sales", "income"])]
        cost_cols = [c for c in numeric_cols if any(x in c.lower() for x in ["cost", "expense", "spend"])]
        profit_cols = [c for c in numeric_cols if any(x in c.lower() for x in ["profit", "margin"])]

        if revenue_cols:
            revenue_total = self.df[revenue_cols].sum().sum()
            revenue_health = self._safe_score(revenue_total, 0, max(revenue_total, 1))
            revenue_health = min(95, max(60, revenue_health))

        if profit_cols:
            profit_total = self.df[profit_cols].sum().sum()
            financial_health = 80 if profit_total > 0 else 45

        if cost_cols and revenue_cols:
            total_cost = self.df[cost_cols].sum().sum()
            total_revenue = self.df[revenue_cols].sum().sum()

            if total_revenue > 0:
                cost_ratio = total_cost / total_revenue
                if cost_ratio < 0.4:
                    financial_health = 90
                elif cost_ratio < 0.7:
                    financial_health = 75
                else:
                    financial_health = 55

        volatility = std_values.mean()
        average_metric = abs(mean_values.mean()) if abs(mean_values.mean()) > 0 else 1
        volatility_ratio = volatility / average_metric

        if volatility_ratio < 0.25:
            risk_health = 85
        elif volatility_ratio < 0.6:
            risk_health = 70
        else:
            risk_health = 50

        missing_ratio = self.df.isnull().sum().sum() / max(1, self.df.size)

        if missing_ratio < 0.05:
            operational_health = 85
        elif missing_ratio < 0.15:
            operational_health = 70
        else:
            operational_health = 50

        if len(self.df) >= 3:
            first_half = self.df[numeric_cols].head(len(self.df) // 2).mean().mean()
            second_half = self.df[numeric_cols].tail(len(self.df) // 2).mean().mean()

            if second_half > first_half:
                growth_health = 82
            elif second_half == first_half:
                growth_health = 65
            else:
                growth_health = 48

        overall_score = round(
            (
                financial_health * 0.25 +
                revenue_health * 0.25 +
                growth_health * 0.20 +
                risk_health * 0.15 +
                operational_health * 0.15
            ),
            1
        )

        if overall_score >= 80:
            status = "Healthy Growth"
        elif overall_score >= 65:
            status = "Stable but Needs Attention"
        elif overall_score >= 50:
            status = "Moderate Risk"
        else:
            status = "Strategic Warning"

        strengths = []
        weaknesses = []

        if financial_health >= 75:
            strengths.append("Strong financial performance indicators")
        else:
            weaknesses.append("Financial efficiency requires improvement")

        if revenue_health >= 75:
            strengths.append("Revenue signals appear strong")
        else:
            weaknesses.append("Revenue performance may need strategic review")

        if growth_health >= 75:
            strengths.append("Positive growth direction detected")
        else:
            weaknesses.append("Growth trend appears weak or inconsistent")

        if risk_health >= 75:
            strengths.append("Low volatility and controlled business risk")
        else:
            weaknesses.append("Higher volatility suggests increased business risk")

        if operational_health >= 75:
            strengths.append("Dataset quality and operational consistency look strong")
        else:
            weaknesses.append("Missing or inconsistent data may affect decisions")

        recommendation = self._generate_recommendation(overall_score, weaknesses)

        return {
            "overall_score": overall_score,
            "status": status,
            "financial_health": round(financial_health, 1),
            "revenue_health": round(revenue_health, 1),
            "growth_health": round(growth_health, 1),
            "risk_health": round(risk_health, 1),
            "operational_health": round(operational_health, 1),
            "strengths": strengths,
            "weaknesses": weaknesses,
            "recommendation": recommendation
        }

    def _generate_recommendation(self, score, weaknesses):
        if score >= 80:
            return "The enterprise appears healthy. The CEO should consider controlled expansion, market growth, and investment in high-performing areas."
        elif score >= 65:
            return "The enterprise is stable, but selected weaknesses should be addressed before aggressive expansion."
        elif score >= 50:
            return "The enterprise shows moderate risk. Leadership should prioritise cost control, revenue protection, and operational improvement."
        else:
            return "The enterprise requires immediate strategic attention. The CEO should focus on stabilisation, risk reduction, and recovery planning."
