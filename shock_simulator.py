class StrategicShockSimulator:

    def simulate_shock(
        self,
        selected_metric,
        total_value,
        average_value,
        scenario
    ):

        scenario = scenario.lower()

        if scenario == "Revenue drops by 10%".lower():

            impact = total_value * 0.10

            return {
                "scenario": "Revenue drops by 10%",
                "severity": "Moderate",
                "estimated_impact": round(impact, 2),
                "cfo_response": "Review discretionary spending and preserve cash flow.",
                "cmo_response": "Increase customer retention campaigns and loyalty initiatives.",
                "coo_response": "Improve efficiency and reduce operational waste.",
                "cro_response": "Monitor churn risk and revenue concentration exposure.",
                "ceo_response": "Focus on stabilising revenue through retention and targeted growth activities."
            }

        elif scenario == "Revenue drops by 20%".lower():

            impact = total_value * 0.20

            return {
                "scenario": "Revenue drops by 20%",
                "severity": "High",
                "estimated_impact": round(impact, 2),
                "cfo_response": "Initiate cost control measures and reassess budgets.",
                "cmo_response": "Launch aggressive customer acquisition and recovery campaigns.",
                "coo_response": "Prioritise critical business operations and efficiency improvements.",
                "cro_response": "Increase risk monitoring and prepare mitigation plans.",
                "ceo_response": "Implement a revenue recovery strategy while protecting profitability."
            }

        elif scenario == "Costs increase by 15%".lower():

            impact = total_value * 0.15

            return {
                "scenario": "Costs increase by 15%",
                "severity": "High",
                "estimated_impact": round(impact, 2),
                "cfo_response": "Review margins and identify cost-saving opportunities.",
                "cmo_response": "Focus marketing on the most profitable customer segments.",
                "coo_response": "Optimise operations and supplier relationships.",
                "cro_response": "Assess financial and liquidity risks.",
                "ceo_response": "Protect profitability through efficiency and strategic cost management."
            }

        elif scenario == "Competitor enters market".lower():

            impact = total_value * 0.12

            return {
                "scenario": "Competitor enters market",
                "severity": "Medium",
                "estimated_impact": round(impact, 2),
                "cfo_response": "Assess pricing pressure and profitability impact.",
                "cmo_response": "Strengthen brand positioning and customer loyalty.",
                "coo_response": "Maintain service quality and delivery performance.",
                "cro_response": "Monitor market share and customer switching risk.",
                "ceo_response": "Differentiate the business through innovation and customer value."
            }

        elif scenario == "Supply chain disruption".lower():

            impact = total_value * 0.18

            return {
                "scenario": "Supply chain disruption",
                "severity": "High",
                "estimated_impact": round(impact, 2),
                "cfo_response": "Evaluate financial exposure from supply shortages.",
                "cmo_response": "Communicate proactively with key customers.",
                "coo_response": "Identify alternative suppliers and contingency plans.",
                "cro_response": "Escalate operational continuity risk monitoring.",
                "ceo_response": "Prioritise resilience and business continuity planning."
            }

        elif scenario == "Customer demand surge".lower():

            impact = total_value * 0.25

            return {
                "scenario": "Customer demand surge",
                "severity": "Opportunity",
                "estimated_impact": round(impact, 2),
                "cfo_response": "Assess working capital requirements for growth.",
                "cmo_response": "Accelerate conversion and customer acquisition efforts.",
                "coo_response": "Scale operations while protecting service quality.",
                "cro_response": "Monitor overexpansion and execution risks.",
                "ceo_response": "Capture growth opportunities while maintaining operational stability."
            }

        else:

            return {
                "scenario": scenario,
                "severity": "Unknown",
                "estimated_impact": 0,
                "cfo_response": "Review financial impact.",
                "cmo_response": "Review customer impact.",
                "coo_response": "Review operational impact.",
                "cro_response": "Review risk impact.",
                "ceo_response": "Conduct a strategic review."
            }
