import streamlit as st
import pandas as pd
import plotly.express as px

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

st.set_page_config(
    page_title="Cognitive Enterprise Twin",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Cognitive Enterprise Twin")
st.subheader("A Multi-Agent Decision Intelligence Platform for SMEs")

st.markdown("""
The Cognitive Enterprise Twin uses multiple executive-style AI agents to analyse SME business data, identify risks, discover revenue opportunities, store enterprise memory, forecast future performance, and generate explainable strategic recommendations.
""")

st.sidebar.title("CET Control Panel")
st.sidebar.markdown("Upload a business dataset to activate the multi-agent decision intelligence workflow.")

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

    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    if numeric_columns:
        selected_metric = st.selectbox(
            "Select the main business metric for agent analysis",
            numeric_columns
        )

        total_value = df[selected_metric].sum()
        average_value = df[selected_metric].mean()
        max_value = df[selected_metric].max()

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

        st.subheader("Multi-Agent Intelligence Workflow")

        with st.expander("Data Scientist Agent", expanded=True):
            st.write(data_output["insight"])
            st.info(data_output["evidence"])

        with st.expander("Revenue Optimization Agent", expanded=True):
            st.write(revenue_output["insight"])
            st.success(revenue_output["recommendation"])
            st.metric("Estimated Impact", revenue_output["estimated_impact"])

        with st.expander("Risk Officer Agent", expanded=True):
            st.write(risk_output["risk_assessment"])
            st.metric("Risk Level", risk_output["risk_level"])

        with st.expander("Strategy Agent", expanded=True):
            st.write(strategy_output["strategic_view"])
            st.info(strategy_output["priority"])

        with st.expander("CEO Decision Agent", expanded=True):
            st.write(ceo_output["final_decision"])
            st.success(ceo_output["executive_summary"])

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
        {revenue_output["recommendation"]}

        **Risk View:**  
        {risk_output["risk_assessment"]}

        **Strategic Debate Summary:**  
        {debate_summary}

        **Organizational Learning:**  
        {cko_output["insight"]}

        **CEO Decision:**  
        {ceo_output["executive_summary"]}
        """)

    else:
        st.warning("No numeric business metrics found. Please upload a dataset with numeric columns.")

else:
    st.info("Upload a CSV or Excel file from the sidebar to activate the Cognitive Enterprise Twin.")
