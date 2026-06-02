class OpportunityDiscoveryEngine:
    def discover_opportunities(self, df, selected_metric):
        opportunities = []

        average_value = df[selected_metric].mean()
        max_value = df[selected_metric].max()
        min_value = df[selected_metric].min()

        if max_value > average_value * 1.5:
            opportunities.append({
                "type": "High-Performance Opportunity",
                "insight": f"Some records in '{selected_metric}' are significantly above average.",
                "recommendation": "Investigate the top-performing records to identify repeatable growth patterns.",
                "priority": "High"
            })

        if min_value < average_value * 0.5:
            opportunities.append({
                "type": "Improvement Opportunity",
                "insight": f"Some records in '{selected_metric}' are significantly below average.",
                "recommendation": "Review low-performing records to identify operational, pricing, or customer-related issues.",
                "priority": "Medium"
            })

        if df[selected_metric].std() > average_value:
            opportunities.append({
                "type": "Performance Variation Opportunity",
                "insight": f"'{selected_metric}' shows high variation across the dataset.",
                "recommendation": "Segment the data by customer, product, or region to identify where performance differences are coming from.",
                "priority": "Medium"
            })

        if not opportunities:
            opportunities.append({
                "type": "Stable Performance",
                "insight": f"'{selected_metric}' appears relatively stable with no major opportunity signals detected.",
                "recommendation": "Continue monitoring this metric and compare it with customer, product, or regional data.",
                "priority": "Low"
            })

        return opportunities
