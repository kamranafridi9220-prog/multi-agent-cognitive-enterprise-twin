class AICompetitorTwin:
    """
    Simulates competitor pressure and strategic positioning against the enterprise.
    """

    def analyse_competitor(
        self,
        selected_metric,
        total_value,
        average_value,
        competitor_type
    ):
        competitor_type = competitor_type.lower()

        if competitor_type == "low-cost competitor".lower():
            threat_level = "High"
            estimated_pressure = total_value * 0.18
            competitor_strategy = "Competes through lower pricing, aggressive discounts, and volume-based offers."
            enterprise_risk = "Margin compression and customer switching risk."
            recommended_response = "Defend profitable segments, improve value proposition, and avoid unnecessary price wars."

        elif competitor_type == "premium competitor".lower():
            threat_level = "Medium"
            estimated_pressure = total_value * 0.12
            competitor_strategy = "Competes through brand strength, service quality, and premium positioning."
            enterprise_risk = "Loss of high-value customers and weaker differentiation."
            recommended_response = "Strengthen service quality, customer experience, and brand trust."

        elif competitor_type == "technology-driven competitor".lower():
            threat_level = "High"
            estimated_pressure = total_value * 0.20
            competitor_strategy = "Uses automation, AI, digital platforms, and data-driven customer targeting."
            enterprise_risk = "Digital capability gap and slower response to customer needs."
            recommended_response = "Invest in automation, AI-enabled decision support, and customer intelligence."

        elif competitor_type == "new market entrant".lower():
            threat_level = "Medium"
            estimated_pressure = total_value * 0.10
            competitor_strategy = "Enters the market with fresh positioning, introductory offers, and targeted acquisition."
            enterprise_risk = "Market share erosion and increased customer acquisition costs."
            recommended_response = "Protect existing customers, monitor pricing moves, and reinforce loyalty programmes."

        elif competitor_type == "dominant market leader".lower():
            threat_level = "Very High"
            estimated_pressure = total_value * 0.25
            competitor_strategy = "Uses scale, brand recognition, pricing power, and operational resources."
            enterprise_risk = "Reduced bargaining power, weaker visibility, and competitive displacement."
            recommended_response = "Focus on niche strengths, personalised service, agility, and underserved customer segments."

        else:
            threat_level = "Unknown"
            estimated_pressure = total_value * 0.05
            competitor_strategy = "Competitor behaviour is unclear."
            enterprise_risk = "Strategic uncertainty."
            recommended_response = "Collect more market intelligence before making a competitive decision."

        future_value_after_pressure = total_value - estimated_pressure

        return {
            "competitor_type": competitor_type.title(),
            "selected_metric": selected_metric,
            "threat_level": threat_level,
            "estimated_pressure": round(estimated_pressure, 2),
            "future_value_after_pressure": round(future_value_after_pressure, 2),
            "competitor_strategy": competitor_strategy,
            "enterprise_risk": enterprise_risk,
            "recommended_response": recommended_response
        }
