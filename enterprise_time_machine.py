class EnterpriseTimeMachine:
    """
    Simulates future enterprise outcomes based on strategic what-if scenarios.
    """

    def simulate_future(
        self,
        selected_metric,
        total_value,
        average_value,
        scenario
    ):
        scenario = scenario.lower()

        if scenario == "Marketing spend increases by 15%".lower():
            predicted_change = total_value * 0.12
            risk_level = "Moderate"
            recommendation = "Proceed carefully with targeted marketing investment and monitor conversion performance."

        elif scenario == "Customer retention improves by 10%".lower():
            predicted_change = total_value * 0.18
            risk_level = "Low"
            recommendation = "Prioritise loyalty programmes, account management, and retention-led growth."

        elif scenario == "Operational efficiency improves by 20%".lower():
            predicted_change = total_value * 0.15
            risk_level = "Low"
            recommendation = "Invest in process automation, workflow optimisation, and cost reduction initiatives."

        elif scenario == "Pricing increases by 5%".lower():
            predicted_change = total_value * 0.08
            risk_level = "Moderate"
            recommendation = "Test pricing changes with selected customer segments before full rollout."

        elif scenario == "Sales conversion improves by 12%".lower():
            predicted_change = total_value * 0.16
            risk_level = "Low"
            recommendation = "Strengthen sales enablement, lead scoring, and pipeline prioritisation."

        elif scenario == "Market demand decreases by 10%".lower():
            predicted_change = -total_value * 0.10
            risk_level = "High"
            recommendation = "Protect revenue through retention, cost control, and selective market repositioning."

        else:
            predicted_change = 0
            risk_level = "Unknown"
            recommendation = "Run further analysis before making strategic decisions."

        predicted_future_value = total_value + predicted_change

        if predicted_change > 0:
            direction = "Positive Future Scenario"
        elif predicted_change < 0:
            direction = "Negative Future Scenario"
        else:
            direction = "Neutral Future Scenario"

        return {
            "scenario": scenario.title(),
            "selected_metric": selected_metric,
            "current_total_value": round(total_value, 2),
            "predicted_change": round(predicted_change, 2),
            "predicted_future_value": round(predicted_future_value, 2),
            "risk_level": risk_level,
            "direction": direction,
            "recommendation": recommendation
        }
