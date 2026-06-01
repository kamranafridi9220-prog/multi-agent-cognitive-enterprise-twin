class StrategicDecisionEngine:
    def generate_decision_score(self, risk_level, estimated_impact):
        score = 50

        if estimated_impact == "High":
            score += 30
        elif estimated_impact == "Medium to High":
            score += 20
        elif estimated_impact == "Medium":
            score += 10

        if risk_level == "High":
            score -= 30
        elif risk_level == "Medium":
            score -= 15
        elif risk_level == "Low":
            score += 10

        return max(0, min(score, 100))

    def classify_decision(self, score):
        if score >= 75:
            return "Strong Strategic Opportunity"
        elif score >= 50:
            return "Moderate Strategic Opportunity"
        else:
            return "High-Risk Decision Area"

    def generate_agent_debate(self, revenue_output, risk_output, strategy_output):
        debate = []

        debate.append({
            "agent": "Revenue Optimization Agent",
            "position": revenue_output["recommendation"]
        })

        debate.append({
            "agent": "Risk Officer Agent",
            "position": risk_output["risk_assessment"]
        })

        debate.append({
            "agent": "Strategy Agent",
            "position": strategy_output["priority"]
        })

        return debate

    def generate_debate_summary(self, debate):
        return (
            "The agent debate shows that the revenue perspective identifies growth potential, "
            "the risk perspective evaluates possible threats, and the strategy perspective balances "
            "opportunity with cautious execution before the CEO Decision Agent produces the final recommendation."
        )
