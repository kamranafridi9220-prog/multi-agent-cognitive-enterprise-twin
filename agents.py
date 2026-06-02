from llm_engine import LLMEngine


class DataScientistAgent:
    def analyse(self, df, selected_metric):
        return {
            "role": "Data Scientist Agent",
            "insight": f"The dataset contains {df.shape[0]} records and {df.shape[1]} columns. The selected metric '{selected_metric}' is suitable for business performance analysis.",
            "evidence": f"Total {selected_metric}: {round(df[selected_metric].sum(), 2)}, Average {selected_metric}: {round(df[selected_metric].mean(), 2)}"
        }


class RevenueOptimizationAgent:
    def analyse(self, df, selected_metric):
        average_value = df[selected_metric].mean()
        total_value = df[selected_metric].sum()
        max_value = df[selected_metric].max()

        system_prompt = """
        You are a Revenue Optimization Agent for an SME decision intelligence platform.
        Your task is to analyse business performance data and generate practical revenue growth recommendations.
        Use clear executive language.
        """

        user_prompt = f"""
        Business metric analysed: {selected_metric}

        Total value: {round(total_value, 2)}
        Average value: {round(average_value, 2)}
        Maximum value: {round(max_value, 2)}

        Generate a concise revenue optimization insight and recommendation for SME decision-makers.
        """

        ai_reasoning = LLMEngine().generate_response(system_prompt, user_prompt)

        return {
            "role": "Revenue Optimization Agent",
            "insight": f"The metric '{selected_metric}' shows revenue or performance potential that should be reviewed for growth opportunities.",
            "recommendation": f"Focus on segments, products, or customers contributing above the average value of {round(average_value, 2)}.",
            "estimated_impact": "Medium to High",
            "ai_reasoning": ai_reasoning
        }


class RiskOfficerAgent:
    def analyse(self, df, selected_metric):
        missing_values = df[selected_metric].isnull().sum()
        min_value = df[selected_metric].min()
        average_value = df[selected_metric].mean()

        if missing_values > 0:
            risk = f"{missing_values} missing values detected in {selected_metric}."
        elif min_value < 0:
            risk = f"Negative values detected in {selected_metric}, which may indicate loss, refund, or data quality issues."
        else:
            risk = f"No immediate data quality risk detected for {selected_metric}."

        risk_level = "Medium" if missing_values > 0 or min_value < 0 else "Low"

        system_prompt = """
        You are a Risk Officer Agent for an SME decision intelligence platform.
        Your task is to identify business risks, data risks, operational risks, and strategic risks.
        Use clear, practical, executive-level language.
        """

        user_prompt = f"""
        Business metric analysed: {selected_metric}

        Missing values: {missing_values}
        Minimum value: {round(min_value, 2)}
        Average value: {round(average_value, 2)}
        Initial risk assessment: {risk}
        Risk level: {risk_level}

        Generate a concise risk analysis and mitigation recommendation for SME decision-makers.
        """

        ai_reasoning = LLMEngine().generate_response(system_prompt, user_prompt)

        return {
            "role": "Risk Officer Agent",
            "risk_assessment": risk,
            "risk_level": risk_level,
            "ai_reasoning": ai_reasoning
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
        system_prompt = """
        You are a CEO Decision Agent inside a Cognitive Enterprise Twin.
        Your task is to synthesize analytical, revenue, risk, and strategy outputs into a final executive decision.
        Use concise board-level language.
        """

        user_prompt = f"""
        Data Scientist Insight:
        {data_output.get("insight")}

        Revenue Recommendation:
        {revenue_output.get("recommendation")}

        Revenue AI Reasoning:
        {revenue_output.get("ai_reasoning")}

        Risk Assessment:
        {risk_output.get("risk_assessment")}

        Risk AI Reasoning:
        {risk_output.get("ai_reasoning")}

        Strategy View:
        {strategy_output.get("strategic_view")}

        Strategic Priority:
        {strategy_output.get("priority")}

        Generate a final CEO-level strategic recommendation for an SME decision-maker.
        """

        ai_reasoning = LLMEngine().generate_response(system_prompt, user_prompt)

        return {
            "role": "CEO Decision Agent",
            "final_decision": "Proceed with deeper business analysis before making strategic changes.",
            "executive_summary": "The Cognitive Enterprise Twin has identified initial performance patterns, revenue opportunities, and risk signals. The recommended next step is to prioritise high-value areas while monitoring operational and financial risks.",
            "ai_reasoning": ai_reasoning
        }


class ChiefKnowledgeOfficerAgent:
    def analyse(self, memory_data):
        if not memory_data:
            return {
                "role": "Chief Knowledge Officer Agent",
                "insight": "No historical enterprise memory is available yet. The system will begin learning as more business analyses are completed.",
                "ai_reasoning": "AI organizational learning will become available once memory records exist."
            }

        total_analyses = len(memory_data)

        average_score = round(
            sum(record["decision_score"] for record in memory_data) / total_analyses,
            2
        )

        latest_record = memory_data[-1]
        latest_score = latest_record["decision_score"]
        latest_metric = latest_record["selected_metric"]
        latest_classification = latest_record["decision_classification"]

        if latest_score >= average_score:
            trend = "The latest decision score is equal to or above the historical average, suggesting improving or stable decision quality."
        else:
            trend = "The latest decision score is below the historical average, suggesting the business should review recent risks or weak performance areas."

        system_prompt = """
        You are a Chief Knowledge Officer Agent for a Cognitive Enterprise Twin.
        Your task is to convert historical memory records into organizational learning.
        Focus on patterns, decision quality, repeated risks, and learning opportunities.
        """

        user_prompt = f"""
        Number of historical analyses: {total_analyses}
        Average decision score: {average_score}
        Latest metric analysed: {latest_metric}
        Latest decision score: {latest_score}
        Latest classification: {latest_classification}
        Trend interpretation: {trend}

        Generate an organizational learning insight for SME leadership.
        """

        ai_reasoning = LLMEngine().generate_response(system_prompt, user_prompt)

        return {
            "role": "Chief Knowledge Officer Agent",
            "insight": (
                f"The Cognitive Enterprise Twin has stored {total_analyses} historical business analysis record(s). "
                f"The average decision score is {average_score}/100. "
                f"The latest analysis focused on '{latest_metric}' with a score of {latest_score}/100, classified as '{latest_classification}'. "
                f"{trend}"
            ),
            "ai_reasoning": ai_reasoning
        }
