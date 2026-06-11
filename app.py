import streamlit as st
import pandas as pd
import plotly.express as px
from health_score_engine import EnterpriseHealthScoreEngine
from shock_simulator import StrategicShockSimulator

from agents import (
    DataScientistAgent,
    RevenueOptimizationAgent,
    RiskOfficerAgent,
    StrategyAgent,
    CEODecisionAgent,
    ChiefKnowledgeOfficerAgent
)

from decision_engine import StrategicDecisionEngine
from memory_engine import EnterpriseMemoryEngine
from forecasting_agent import ForecastingAgent
from opportunity_engine import OpportunityDiscoveryEngine
from llm_engine import LLMEngine

from boardroom_agents import (
    ChiefFinancialOfficerAgent,
    ChiefMarketingOfficerAgent,
    ChiefOperationsOfficerAgent,
    ChiefRiskOfficerBoardAgent,
    BoardroomChairAgent
)

st.set_page_config(
    page_title="Cognitive Enterprise Twin",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Cognitive Enterprise Twin")
st.subheader("A Multi-Agent AI Decision Intelligence Platform for SMEs")

st.markdown("""
The Cognitive Enterprise Twin uses multiple executive-style AI agents to analyse SME business data, identify risks, discover revenue opportunities, store enterprise memory, forecast future performance, and generate AI-powered strategic recommendations.
""")

st.sidebar.title("CET Control Panel")
st.sidebar.markdown("Upload a business dataset to activate the multi-agent AI decision intelligence workflow.")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV or Excel dataset",
    type=["csv", "xlsx"]
)

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset uploaded successfully.")

    st.subheader("Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    st.subheader("Enterprise Data Summary")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Missing Values", int(df.isnull().sum().sum()))

    st.subheader("Enterprise Health Score Engine")

    health_engine = EnterpriseHealthScoreEngine(df)
    health_result = health_engine.calculate_health_score()

    h_col1, h_col2, h_col3 = st.columns(3)

    h_col1.metric(
        "Enterprise Health Score",
        f"{health_result['overall_score']}/100"
    )

    h_col2.metric(
        "Enterprise Status",
        health_result["status"]
    )

    h_col3.metric(
        "Decision Priority",
        "Strategic Review"
    )

    st.progress(health_result["overall_score"] / 100)

    st.markdown("### Health Dimensions")

    hd1, hd2, hd3, hd4, hd5 = st.columns(5)

    hd1.metric("Financial", f"{health_result['financial_health']}/100")
    hd2.metric("Revenue", f"{health_result['revenue_health']}/100")
    hd3.metric("Growth", f"{health_result['growth_health']}/100")
    hd4.metric("Risk", f"{health_result['risk_health']}/100")
    hd5.metric("Operational", f"{health_result['operational_health']}/100")

    st.markdown("### Strengths Detected")
    for strength in health_result["strengths"]:
        st.success(strength)

    st.markdown("### Weaknesses Detected")
    for weakness in health_result["weaknesses"]:
        st.warning(weakness)

    st.markdown("### Digital CEO Health Recommendation")
    st.info(health_result["recommendation"])

    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    if numeric_columns:
        selected_metric = st.selectbox(
            "Select the main business metric for agent analysis",
            numeric_columns
        )

        total_value = df[selected_metric].sum()
        average_value = df[selected_metric].mean()
        max_value = df[selected_metric].max()
        missing_values = df[selected_metric].isnull().sum()

        st.subheader("Selected Metric Performance")

        c1, c2, c3 = st.columns(3)
        c1.metric(f"Total {selected_metric}", round(total_value, 2))
        c2.metric(f"Average {selected_metric}", round(average_value, 2))
        c3.metric(f"Highest {selected_metric}", round(max_value, 2))

        st.subheader("Metric Distribution")
        fig = px.histogram(
            df,
            x=selected_metric,
            title=f"Distribution of {selected_metric}"
        )
        st.plotly_chart(fig, use_container_width=True)

        data_agent = DataScientistAgent()
        revenue_agent = RevenueOptimizationAgent()
        risk_agent = RiskOfficerAgent()
        strategy_agent = StrategyAgent()
        ceo_agent = CEODecisionAgent()
        cko_agent = ChiefKnowledgeOfficerAgent()
        forecasting_agent = ForecastingAgent()
        opportunity_engine = OpportunityDiscoveryEngine()

        decision_engine = StrategicDecisionEngine()
        memory_engine = EnterpriseMemoryEngine()

        cfo_agent = ChiefFinancialOfficerAgent()
        cmo_agent = ChiefMarketingOfficerAgent()
        coo_agent = ChiefOperationsOfficerAgent()
        cro_board_agent = ChiefRiskOfficerBoardAgent()
        boardroom_chair = BoardroomChairAgent()

        data_output = data_agent.analyse(df, selected_metric)
        revenue_output = revenue_agent.analyse(df, selected_metric)
        risk_output = risk_agent.analyse(df, selected_metric)
        forecast_output = forecasting_agent.analyse(df, selected_metric)
        opportunities = opportunity_engine.discover_opportunities(df, selected_metric)
        strategy_output = strategy_agent.analyse(revenue_output, risk_output)

        ceo_output = ceo_agent.analyse(
            data_output,
            revenue_output,
            risk_output,
            strategy_output
        )

        decision_score = decision_engine.generate_decision_score(
            risk_output["risk_level"],
            revenue_output["estimated_impact"]
        )

        decision_classification = decision_engine.classify_decision(decision_score)

        cfo_view = cfo_agent.analyse(
            selected_metric,
            total_value,
            average_value,
            decision_score
        )

        cmo_view = cmo_agent.analyse(
            selected_metric,
            total_value,
            average_value
        )

        coo_view = coo_agent.analyse(
            selected_metric,
            missing_values,
            risk_output["risk_level"]
        )

        cro_view = cro_board_agent.analyse(
            selected_metric,
            risk_output["risk_assessment"],
            risk_output["risk_level"]
        )

        boardroom_consensus = boardroom_chair.summarise_boardroom(
            cfo_view,
            cmo_view,
            coo_view,
            cro_view
        )

        agent_debate = decision_engine.generate_agent_debate(
            revenue_output,
            risk_output,
            strategy_output
        )

        debate_summary = decision_engine.generate_debate_summary(agent_debate)

        memory_record = memory_engine.create_memory_record(
            dataset_name=uploaded_file.name,
            selected_metric=selected_metric,
            decision_score=decision_score,
            decision_classification=decision_classification,
            revenue_view=revenue_output["recommendation"],
            risk_view=risk_output["risk_assessment"],
            ceo_decision=ceo_output["executive_summary"]
        )

        updated_memory = memory_engine.add_memory_record(memory_record)
        memory_summary = memory_engine.summarize_memory(memory_record)
        historical_summary = memory_engine.summarize_historical_memory()
        cko_output = cko_agent.analyse(updated_memory)

        st.subheader("Strategic Decision Score")

        d1, d2 = st.columns(2)
        d1.metric("Decision Score", f"{decision_score}/100")
        d2.metric("Decision Classification", decision_classification)

        st.progress(decision_score / 100)

        st.subheader("Opportunity Discovery Engine")

        for opportunity in opportunities:
            if opportunity["priority"] == "High":
                st.error(f"**{opportunity['type']}**")
            elif opportunity["priority"] == "Medium":
                st.warning(f"**{opportunity['type']}**")
            else:
                st.info(f"**{opportunity['type']}**")

            st.write(opportunity["insight"])
            st.success(opportunity["recommendation"])
            st.markdown("---")

        st.subheader("Forecasting Agent")

        f1, f2, f3, f4 = st.columns(4)
        f1.metric("Current Average", forecast_output["current_value"])
        f2.metric("3-Month Forecast", forecast_output["forecast_3_month"])
        f3.metric("6-Month Forecast", forecast_output["forecast_6_month"])
        f4.metric("12-Month Forecast", forecast_output["forecast_12_month"])

        st.info(forecast_output["insight"])

        forecast_df = pd.DataFrame({
            "Period": ["Current", "3 Months", "6 Months", "12 Months"],
            "Forecast Value": [
                forecast_output["current_value"],
                forecast_output["forecast_3_month"],
                forecast_output["forecast_6_month"],
                forecast_output["forecast_12_month"]
            ]
        })

        forecast_fig = px.line(
            forecast_df,
            x="Period",
            y="Forecast Value",
            markers=True,
            title=f"Forecast Trend for {selected_metric}"
        )

        st.plotly_chart(forecast_fig, use_container_width=True)
        st.subheader("Strategic Shock Simulator")

        st.markdown("""
        The Strategic Shock Simulator tests how the enterprise would respond to major business disruptions or opportunities.
        Each scenario generates a simulated boardroom response from the CFO, CMO, COO, CRO, and Digital CEO.
        """)

        shock_scenarios = [
            "Revenue drops by 10%",
            "Revenue drops by 20%",
            "Costs increase by 15%",
            "Competitor enters market",
            "Supply chain disruption",
            "Customer demand surge"
        ]

        selected_shock = st.selectbox(
            "Select a strategic shock scenario",
            shock_scenarios
        )

        shock_simulator = StrategicShockSimulator()

        shock_result = shock_simulator.simulate_shock(
            selected_metric=selected_metric,
            total_value=total_value,
            average_value=average_value,
            scenario=selected_shock
        )

        s1, s2, s3 = st.columns(3)

        s1.metric("Scenario", shock_result["scenario"])
        s2.metric("Severity", shock_result["severity"])
        s3.metric("Estimated Impact", shock_result["estimated_impact"])

        st.markdown("### Simulated Executive Boardroom Response")

        with st.expander("CFO Shock Response", expanded=True):
            st.write(shock_result["cfo_response"])

        with st.expander("CMO Shock Response", expanded=True):
            st.write(shock_result["cmo_response"])

        with st.expander("COO Shock Response", expanded=True):
            st.write(shock_result["coo_response"])

        with st.expander("CRO Shock Response", expanded=True):
            st.write(shock_result["cro_response"])

        st.markdown("### Digital CEO Shock Decision")
        st.success(shock_result["ceo_response"])
        st.subheader("Multi-Agent AI Intelligence Workflow")

        with st.expander("Data Scientist Agent", expanded=True):
            st.write(data_output["insight"])
            st.info(data_output["evidence"])

        with st.expander("Revenue Optimization Agent", expanded=True):
            st.write(revenue_output["insight"])
            st.success(revenue_output["recommendation"])
            st.markdown("### AI Revenue Reasoning")
            st.write(revenue_output.get("ai_reasoning", "AI reasoning not available."))

        with st.expander("Risk Officer Agent", expanded=True):
            st.write(risk_output["risk_assessment"])
            st.metric("Risk Level", risk_output["risk_level"])
            st.markdown("### AI Risk Reasoning")
            st.write(risk_output.get("ai_reasoning", "AI reasoning not available."))

        with st.expander("Strategy Agent", expanded=True):
            st.write(strategy_output["strategic_view"])
            st.info(strategy_output["priority"])

        with st.expander("CEO Decision Agent", expanded=True):
            st.write(ceo_output["final_decision"])
            st.success(ceo_output["executive_summary"])
            st.markdown("### AI CEO Reasoning")
            st.write(ceo_output.get("ai_reasoning", "AI reasoning not available."))

        st.subheader("AI Executive Boardroom")

        with st.expander("Chief Financial Officer View", expanded=True):
            st.write(cfo_view)

        with st.expander("Chief Marketing Officer View", expanded=True):
            st.write(cmo_view)

        with st.expander("Chief Operations Officer View", expanded=True):
            st.write(coo_view)

        with st.expander("Chief Risk Officer View", expanded=True):
            st.write(cro_view)

        st.subheader("Boardroom Consensus Recommendation")
        st.success(boardroom_consensus)

        st.subheader("Digital CEO Advisor")

        st.markdown("""
        Ask the Digital CEO a strategic business question based on the uploaded dataset, agent analysis, boardroom discussion, enterprise memory, and decision intelligence results.
        """)

        ceo_question = st.text_area(
            "Ask the Digital CEO",
            placeholder="Example: What should the business focus on next quarter?"
        )

        if st.button("Ask Digital CEO"):
            if ceo_question.strip():
                digital_ceo_system_prompt = """
                You are the Digital CEO inside a Cognitive Enterprise Twin.
                Your role is to answer strategic business questions using the available dataset analysis,
                revenue insights, risk insights, forecasting results, boardroom consensus, enterprise memory,
                and organizational learning.

                Provide clear, practical, executive-level advice.
                Do not mention that you are an AI model.
                """

                digital_ceo_user_prompt = f"""
                User question:
                {ceo_question}

                Selected business metric:
                {selected_metric}

                Total value:
                {round(total_value, 2)}

                Average value:
                {round(average_value, 2)}

                Decision score:
                {decision_score}/100

                Decision classification:
                {decision_classification}

                Revenue reasoning:
                {revenue_output.get("ai_reasoning")}

                Risk reasoning:
                {risk_output.get("ai_reasoning")}

                Forecast insight:
                {forecast_output.get("insight")}

                Boardroom consensus:
                {boardroom_consensus}

                Enterprise memory:
                {historical_summary}

                Chief Knowledge Officer insight:
                {cko_output.get("ai_reasoning")}

                Provide a concise but strategic CEO-level answer.
                """

                digital_ceo_response = LLMEngine().generate_response(
                    digital_ceo_system_prompt,
                    digital_ceo_user_prompt
                )

                st.success(digital_ceo_response)
            else:
                st.warning("Please enter a strategic question for the Digital CEO.")

        st.subheader("Strategic Agent Debate")

        st.info(debate_summary)

        for debate_item in agent_debate:
            with st.expander(debate_item["agent"]):
                st.write(debate_item["position"])

        st.subheader("Cognitive Enterprise Memory")

        st.info(memory_summary)
        st.write(historical_summary)

        with st.expander("View Latest Memory Record"):
            st.json(memory_record)

        st.subheader("Chief Knowledge Officer Agent")

        st.success(cko_output["insight"])

        st.markdown("### AI Organizational Learning")
        st.write(cko_output.get("ai_reasoning", "AI organizational learning not available."))

        with st.expander("View Full Enterprise Memory"):
            st.json(updated_memory)

        st.subheader("Executive Decision Summary")

        opportunity_summary = " ".join(
            [f"{item['type']}: {item['recommendation']}" for item in opportunities]
        )

        st.markdown(f"""
        ### Final Strategic Recommendation

        **Selected Business Metric:** {selected_metric}

        **Decision Score:** {decision_score}/100

        **Decision Classification:** {decision_classification}

        **Opportunity View:**  
        {opportunity_summary}

        **Forecast View:**  
        {forecast_output["insight"]}

        **Revenue View:**  
        {revenue_output["ai_reasoning"]}

        **Risk View:**  
        {risk_output["ai_reasoning"]}

        **AI Executive Boardroom Consensus:**  
        {boardroom_consensus}

        **Strategic Debate Summary:**  
        {debate_summary}

        **Organizational Learning:**  
        {cko_output["ai_reasoning"]}

        **CEO Decision:**  
        {ceo_output["ai_reasoning"]}
        """)

    else:
        st.warning("No numeric business metrics found. Please upload a dataset with numeric columns.")

else:
    st.info("Upload a CSV or Excel file from the sidebar to activate the Cognitive Enterprise Twin.")
