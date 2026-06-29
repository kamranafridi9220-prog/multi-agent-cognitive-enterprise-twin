import streamlit as st
import pandas as pd
import plotly.express as px
from textwrap import dedent

from health_score_engine import EnterpriseHealthScoreEngine
from shock_simulator import StrategicShockSimulator
from executive_voting_engine import ExecutiveVotingEngine
from enterprise_time_machine import EnterpriseTimeMachine
from competitor_twin import AICompetitorTwin

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
# =====================================================
# CUSTOM EXECUTIVE UI THEME
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0F172A 0%, #111827 45%, #1E293B 100%);
    color: #F8FAFC;
}

section[data-testid="stSidebar"] {
    background-color: #020617;
    border-right: 1px solid #334155;
}

h1 {
    font-size: 3rem !important;
    font-weight: 800 !important;
    color: #F8FAFC !important;
    letter-spacing: -1px;
}

h2, h3 {
    color: #E2E8F0 !important;
    font-weight: 700 !important;
}

p, label, span, div {
    color: #E5E7EB;
}

[data-testid="stMetric"] {
    background: linear-gradient(145deg, #111827, #1E293B);
    border: 1px solid #334155;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
}

[data-testid="stMetricLabel"] {
    color: #94A3B8 !important;
    font-size: 0.9rem !important;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"] {
    color: #38BDF8 !important;
    font-size: 1.8rem !important;
    font-weight: 800 !important;
}

.stButton > button {
    background: linear-gradient(90deg, #06B6D4, #2563EB);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.7rem 1.2rem;
    font-weight: 700;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #0891B2, #1D4ED8);
    color: white;
}

[data-testid="stExpander"] {
    background-color: #111827;
    border: 1px solid #334155;
    border-radius: 16px;
}

.stDataFrame {
    border-radius: 16px;
    overflow: hidden;
}

div[data-testid="stAlert"] {
    border-radius: 14px;
    border: 1px solid #334155;
}

hr {
    border: none;
    height: 1px;
    background: #334155;
    margin: 2rem 0;
}

.hero-container {
    padding: 38px 42px;
    border-radius: 28px;
    background:
        radial-gradient(circle at top left, rgba(20, 184, 166, 0.26), transparent 35%),
        radial-gradient(circle at top right, rgba(99, 102, 241, 0.22), transparent 32%),
        linear-gradient(135deg, rgba(15, 23, 42, 0.96), rgba(30, 41, 59, 0.92));
    border: 1px solid rgba(148, 163, 184, 0.24);
    box-shadow: 0 24px 80px rgba(0, 0, 0, 0.45);
    margin-bottom: 22px;
}

.hero-badge {
    display: inline-block;
    padding: 8px 14px;
    border-radius: 999px;
    background: rgba(20, 184, 166, 0.14);
    color: #5EEAD4 !important;
    border: 1px solid rgba(94, 234, 212, 0.28);
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 0.14em;
    margin-bottom: 16px;
}

.hero-title {
    font-size: 3.4rem !important;
    font-weight: 900 !important;
    letter-spacing: -1.7px;
    margin-bottom: 12px;
    background: linear-gradient(90deg, #F8FAFC, #A5B4FC, #5EEAD4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    max-width: 980px;
    font-size: 1.05rem;
    line-height: 1.75;
    color: #CBD5E1 !important;
}

.agent-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 28px;
}

.agent-pill {
    padding: 10px 14px;
    border-radius: 999px;
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid rgba(148, 163, 184, 0.22);
    color: #E2E8F0 !important;
    font-size: 0.86rem;
    font-weight: 700;
    box-shadow: 0 10px 28px rgba(0,0,0,0.28);
}
.mission-control {
    padding: 26px 30px;
    border-radius: 24px;
    background:
        radial-gradient(circle at top right, rgba(59, 130, 246, 0.22), transparent 30%),
        linear-gradient(135deg, rgba(17, 24, 39, 0.96), rgba(15, 23, 42, 0.96));
    border: 1px solid rgba(148, 163, 184, 0.22);
    box-shadow: 0 22px 60px rgba(0, 0, 0, 0.36);
    margin-bottom: 24px;
}

.mission-label {
    color: #5EEAD4 !important;
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 0.16em;
    margin-bottom: 8px;
}

.mission-title {
    color: #F8FAFC !important;
    font-size: 1.7rem;
    font-weight: 850;
    margin-bottom: 8px;
}

.mission-text {
    color: #CBD5E1 !important;
    max-width: 900px;
    line-height: 1.7;
}

.mc-card {
    padding: 24px;
    border-radius: 22px;
    background:
        linear-gradient(145deg, rgba(15, 23, 42, 0.98), rgba(30, 41, 59, 0.92));
    border: 1px solid rgba(148, 163, 184, 0.20);
    box-shadow: 0 18px 45px rgba(0, 0, 0, 0.35);
    min-height: 150px;
}

.mc-label {
    color: #94A3B8 !important;
    font-size: 0.78rem;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.mc-value {
    color: #5EEAD4 !important;
    font-size: 2.35rem;
    font-weight: 900;
    line-height: 1;
    margin-bottom: 12px;
}

.mc-note {
    color: #CBD5E1 !important;
    font-size: 0.9rem;
}

.executive-alerts {
    margin-top: 24px;
    padding: 24px;
    border-radius: 22px;
    background: rgba(2, 6, 23, 0.64);
    border: 1px solid rgba(148, 163, 184, 0.18);
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.32);
}

.alert-title {
    color: #F8FAFC !important;
    font-size: 1.1rem;
    font-weight: 850;
    margin-bottom: 14px;
}

.alert-row {
    padding: 12px 14px;
    border-radius: 14px;
    margin-bottom: 10px;
    font-size: 0.92rem;
    font-weight: 650;
}

.alert-row.good {
    background: rgba(16, 185, 129, 0.12);
    color: #A7F3D0 !important;
    border: 1px solid rgba(16, 185, 129, 0.22);
}

.alert-row.info {
    background: rgba(59, 130, 246, 0.12);
    color: #BFDBFE !important;
    border: 1px solid rgba(59, 130, 246, 0.22);
}

.alert-row.warning {
    background: rgba(245, 158, 11, 0.12);
    color: #FDE68A !important;
    border: 1px solid rgba(245, 158, 11, 0.22);
}
.agent-timeline {
    margin-top: 24px;
    padding: 26px;
    border-radius: 24px;
    background:
        linear-gradient(145deg, rgba(15, 23, 42, 0.94), rgba(30, 41, 59, 0.88));
    border: 1px solid rgba(148, 163, 184, 0.18);
    box-shadow: 0 22px 55px rgba(0, 0, 0, 0.34);
}

.timeline-title {
    color: #F8FAFC !important;
    font-size: 1.2rem;
    font-weight: 850;
    margin-bottom: 20px;
}

.timeline-item {
    display: flex;
    gap: 14px;
    align-items: flex-start;
    padding: 14px 0;
    border-bottom: 1px solid rgba(148, 163, 184, 0.12);
}

.timeline-item:last-child {
    border-bottom: none;
}

.timeline-dot {
    width: 13px;
    height: 13px;
    border-radius: 50%;
    margin-top: 6px;
    box-shadow: 0 0 18px rgba(94, 234, 212, 0.65);
}

.timeline-dot.active {
    background: #5EEAD4;
}

.timeline-dot.warning {
    background: #FBBF24;
    box-shadow: 0 0 18px rgba(251, 191, 36, 0.65);
}

.timeline-agent {
    color: #E2E8F0 !important;
    font-size: 0.98rem;
    font-weight: 800;
    margin-bottom: 4px;
}

.timeline-text {
    color: #CBD5E1 !important;
    font-size: 0.9rem;
    line-height: 1.55;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-container">
    <div class="hero-badge">AI EXECUTIVE OPERATING SYSTEM</div>
    <h1 class="hero-title">Cognitive Enterprise Twin OS</h1>
    <p class="hero-subtitle">
        A multi-agent strategic intelligence platform that simulates executive reasoning,
        enterprise memory, risk assessment, future scenarios, investment decisions,
        and boardroom-level recommendations for SMEs.
    </p>
</div>

<div class="agent-strip">
    <div class="agent-pill">Revenue Agent Active</div>
    <div class="agent-pill">Risk Agent Active</div>
    <div class="agent-pill">Forecast Agent Active</div>
    <div class="agent-pill">CEO Advisor Online</div>
    <div class="agent-pill">Boardroom Ready</div>
</div>
""", unsafe_allow_html=True)

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

    # =====================================================
    # ENTERPRISE MISSION CONTROL DASHBOARD
    # =====================================================

    st.markdown("## Enterprise Mission Control")

    st.markdown(dedent("""
    <div class="mission-control">
        <div>
            <div class="mission-label">COMMAND STATUS</div>
            <div class="mission-title">Executive Intelligence Activated</div>
            <div class="mission-text">
                Dataset connected. Cognitive agents are analysing enterprise health,
                strategic risk, growth potential, forecasting signals, and boardroom-level decisions.
            </div>
        </div>
    </div>
    """), unsafe_allow_html=True)

    mc1, mc2, mc3, mc4 = st.columns(4)

    with mc1:
        st.markdown("""
        <div class="mc-card">
            <div class="mc-label">Data Records</div>
            <div class="mc-value">{}</div>
            <div class="mc-note">Enterprise rows analysed</div>
        </div>
        """.format(df.shape[0]), unsafe_allow_html=True)

    with mc2:
        st.markdown("""
        <div class="mc-card">
            <div class="mc-label">Business Dimensions</div>
            <div class="mc-value">{}</div>
            <div class="mc-note">Dataset columns detected</div>
        </div>
        """.format(df.shape[1]), unsafe_allow_html=True)

    with mc3:
        st.markdown("""
        <div class="mc-card">
            <div class="mc-label">Data Quality</div>
            <div class="mc-value">{}</div>
            <div class="mc-note">Missing values found</div>
        </div>
        """.format(int(df.isnull().sum().sum())), unsafe_allow_html=True)

    with mc4:
        st.markdown("""
        <div class="mc-card">
            <div class="mc-label">AI Agents</div>
            <div class="mc-value">18</div>
            <div class="mc-note">Executive intelligence units</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(dedent("""
    <div class="executive-alerts">
        <div class="alert-title">Executive Signal Feed</div>
        <div class="alert-row good">Dataset successfully connected to the Cognitive Enterprise Twin OS.</div>
        <div class="alert-row info">Enterprise health engine is ready for diagnostic scoring.</div>
        <div class="alert-row warning">Strategic agents awaiting metric selection for deeper analysis.</div>
    </div>
    """), unsafe_allow_html=True)

st.markdown("""
<div class="agent-timeline">
    <div class="timeline-title">AI Agent Activity Timeline</div>

    <div class="timeline-item">
        <div class="timeline-dot active"></div>
        <div>
            <div class="timeline-agent">Data Intelligence Layer</div>
            <div class="timeline-text">Dataset connected and prepared for enterprise analysis.</div>
        </div>
    </div>

    <div class="timeline-item">
        <div class="timeline-dot active"></div>
        <div>
            <div class="timeline-agent">Enterprise Health Engine</div>
            <div class="timeline-text">Diagnostic scoring activated across financial, revenue, growth, risk, and operational dimensions.</div>
        </div>
    </div>

    <div class="timeline-item">
        <div class="timeline-dot active"></div>
        <div>
            <div class="timeline-agent">Revenue Optimization Agent</div>
            <div class="timeline-text">Ready to identify high-value opportunities and revenue improvement patterns.</div>
        </div>
    </div>

    <div class="timeline-item">
        <div class="timeline-dot warning"></div>
        <div>
            <div class="timeline-agent">Risk Officer Agent</div>
            <div class="timeline-text">Monitoring data quality, volatility, missing values, and potential strategic exposure.</div>
        </div>
    </div>

    <div class="timeline-item">
        <div class="timeline-dot active"></div>
        <div>
            <div class="timeline-agent">AI Executive Boardroom</div>
            <div class="timeline-text">CFO, CMO, COO, CRO, and Digital CEO agents standing by for strategic review.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

    st.subheader("Enterprise Health Score Engine")

    health_engine = EnterpriseHealthScoreEngine(df)
    health_result = health_engine.calculate_health_score()

    h_col1, h_col2, h_col3 = st.columns(3)

    h_col1.metric("Enterprise Health Score", f"{health_result['overall_score']}/100")
    h_col2.metric("Enterprise Status", health_result["status"])
    h_col3.metric("Decision Priority", "Strategic Review")

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

        st.subheader("AI Executive Voting System")

        st.markdown("""
        The AI Executive Voting System simulates how the executive board would vote on the current strategic decision.
        Each executive agent votes based on financial viability, commercial opportunity, operational readiness, and risk exposure.
        """)

        voting_engine = ExecutiveVotingEngine()

        voting_result = voting_engine.generate_votes(
            decision_score=decision_score,
            risk_level=risk_output["risk_level"],
            estimated_impact=revenue_output["estimated_impact"],
            health_score=health_result["overall_score"],
            shock_severity=shock_result["severity"]
        )

        v1, v2, v3, v4 = st.columns(4)

        v1.metric("YES Votes", voting_result["yes_votes"])
        v2.metric("CAUTION Votes", voting_result["caution_votes"])
        v3.metric("NO Votes", voting_result["no_votes"])
        v4.metric("Confidence", f"{voting_result['confidence']}%")

        st.markdown("### Executive Vote Breakdown")

        for executive, vote_data in voting_result["votes"].items():
            if vote_data["vote"] == "YES":
                st.success(f"**{executive}: {vote_data['vote']}** — {vote_data['reason']}")
            elif vote_data["vote"] == "CAUTION":
                st.warning(f"**{executive}: {vote_data['vote']}** — {vote_data['reason']}")
            else:
                st.error(f"**{executive}: {vote_data['vote']}** — {vote_data['reason']}")

        st.markdown("### Final Board Vote Decision")

        if voting_result["final_result"] == "Approved":
            st.success(voting_result["final_result"])
        elif voting_result["final_result"] == "Conditional Approval":
            st.warning(voting_result["final_result"])
        else:
            st.error(voting_result["final_result"])

        st.subheader("Enterprise Time Machine")

        st.markdown("""
        The Enterprise Time Machine simulates future business outcomes based on strategic what-if scenarios.
        It helps leaders explore how different decisions may affect future performance, risk, and enterprise value.
        """)

        time_machine_scenarios = [
            "Marketing spend increases by 15%",
            "Customer retention improves by 10%",
            "Operational efficiency improves by 20%",
            "Pricing increases by 5%",
            "Sales conversion improves by 12%",
            "Market demand decreases by 10%"
        ]

        selected_future_scenario = st.selectbox(
            "Select a future scenario",
            time_machine_scenarios
        )

        time_machine = EnterpriseTimeMachine()

        future_result = time_machine.simulate_future(
            selected_metric=selected_metric,
            total_value=total_value,
            average_value=average_value,
            scenario=selected_future_scenario
        )

        tm1, tm2, tm3 = st.columns(3)

        tm1.metric("Current Value", future_result["current_total_value"])
        tm2.metric("Predicted Change", future_result["predicted_change"])
        tm3.metric("Predicted Future Value", future_result["predicted_future_value"])

        tm4, tm5 = st.columns(2)

        tm4.metric("Future Direction", future_result["direction"])
        tm5.metric("Predicted Risk", future_result["risk_level"])

        st.markdown("### Time Machine Recommendation")
        st.info(future_result["recommendation"])

        st.subheader("AI Competitor Twin")

        st.markdown("""
        The AI Competitor Twin simulates how different competitor profiles may affect enterprise performance, market position, and strategic risk.
        It helps leaders prepare defensive and offensive strategies against competitive pressure.
        """)

        competitor_profiles = [
            "Low-cost competitor",
            "Premium competitor",
            "Technology-driven competitor",
            "New market entrant",
            "Dominant market leader"
        ]

        selected_competitor = st.selectbox(
            "Select competitor profile",
            competitor_profiles
        )

        competitor_twin = AICompetitorTwin()

        competitor_result = competitor_twin.analyse_competitor(
            selected_metric=selected_metric,
            total_value=total_value,
            average_value=average_value,
            competitor_type=selected_competitor
        )

        ct1, ct2, ct3 = st.columns(3)

        ct1.metric("Competitor Type", competitor_result["competitor_type"])
        ct2.metric("Threat Level", competitor_result["threat_level"])
        ct3.metric("Estimated Pressure", competitor_result["estimated_pressure"])

        ct4, ct5 = st.columns(2)

        ct4.metric("Current Value", round(total_value, 2))
        ct5.metric("Value After Competitive Pressure", competitor_result["future_value_after_pressure"])

        st.markdown("### Competitor Strategy")
        st.warning(competitor_result["competitor_strategy"])

        st.markdown("### Enterprise Risk")
        st.error(competitor_result["enterprise_risk"])

        st.markdown("### Recommended Strategic Response")
        st.success(competitor_result["recommended_response"])

        st.subheader("Strategic Growth Navigator")

        st.markdown("""
        The Strategic Growth Navigator converts enterprise intelligence into a practical strategic roadmap.
        It gives SME leaders a 30-day, 90-day, and 12-month action plan based on the selected growth objective.
        """)

        growth_goal = st.selectbox(
            "Select Strategic Growth Goal",
            [
                "Revenue Growth",
                "Market Expansion",
                "Cost Reduction",
                "Customer Retention",
                "Digital Transformation",
                "Product Innovation"
            ]
        )

        growth_roadmaps = {
            "Revenue Growth": {
                "30-Day Plan": [
                    "Identify highest-value customers",
                    "Review underperforming revenue segments",
                    "Launch quick upsell opportunities"
                ],
                "90-Day Plan": [
                    "Introduce tiered pricing",
                    "Build customer segmentation",
                    "Improve sales conversion process"
                ],
                "12-Month Plan": [
                    "Develop recurring revenue streams",
                    "Expand into new profitable segments",
                    "Build strategic partnerships"
                ]
            },
            "Market Expansion": {
                "30-Day Plan": [
                    "Research target markets",
                    "Analyse competitor activity",
                    "Identify demand signals"
                ],
                "90-Day Plan": [
                    "Launch pilot campaigns",
                    "Test regional demand",
                    "Develop market entry partnerships"
                ],
                "12-Month Plan": [
                    "Enter new market segments",
                    "Scale acquisition channels",
                    "Build stronger market presence"
                ]
            },
            "Cost Reduction": {
                "30-Day Plan": [
                    "Review major cost drivers",
                    "Identify operational inefficiencies",
                    "Assess supplier contracts"
                ],
                "90-Day Plan": [
                    "Automate repetitive processes",
                    "Reduce waste and duplication",
                    "Improve procurement control"
                ],
                "12-Month Plan": [
                    "Build cost-efficient workflows",
                    "Strengthen operational discipline",
                    "Create continuous improvement systems"
                ]
            },
            "Customer Retention": {
                "30-Day Plan": [
                    "Identify churn indicators",
                    "Review customer feedback",
                    "Improve customer support response"
                ],
                "90-Day Plan": [
                    "Launch loyalty initiatives",
                    "Improve customer engagement",
                    "Create retention campaigns"
                ],
                "12-Month Plan": [
                    "Build long-term retention framework",
                    "Strengthen brand loyalty",
                    "Develop customer success processes"
                ]
            },
            "Digital Transformation": {
                "30-Day Plan": [
                    "Assess digital maturity",
                    "Identify manual processes",
                    "Prioritise automation opportunities"
                ],
                "90-Day Plan": [
                    "Implement AI-supported workflows",
                    "Improve data infrastructure",
                    "Strengthen analytics capability"
                ],
                "12-Month Plan": [
                    "Build enterprise-wide automation",
                    "Create AI-enabled decision systems",
                    "Develop a digital operating model"
                ]
            },
            "Product Innovation": {
                "30-Day Plan": [
                    "Identify customer pain points",
                    "Research new product opportunities",
                    "Review competitor offerings"
                ],
                "90-Day Plan": [
                    "Develop prototype concepts",
                    "Test product-market fit",
                    "Collect early customer feedback"
                ],
                "12-Month Plan": [
                    "Launch new product lines",
                    "Expand the product portfolio",
                    "Create competitive differentiation"
                ]
            }
        }

        selected_roadmap = growth_roadmaps[growth_goal]

        g1, g2, g3 = st.columns(3)

        with g1:
            st.markdown("### 30-Day Plan")
            for action in selected_roadmap["30-Day Plan"]:
                st.success(action)

        with g2:
            st.markdown("### 90-Day Plan")
            for action in selected_roadmap["90-Day Plan"]:
                st.info(action)

        with g3:
            st.markdown("### 12-Month Plan")
            for action in selected_roadmap["12-Month Plan"]:
                st.warning(action)

        st.markdown("### Strategic Navigator Recommendation")
        st.success(
            f"The enterprise should prioritise '{growth_goal}' using a phased roadmap: immediate actions in 30 days, structured execution in 90 days, and strategic transformation over 12 months."
        )

        st.subheader("AI Investment Advisor & Capital Allocation Engine")

        st.markdown("""
        The AI Investment Advisor helps SME leaders compare strategic investment options,
        estimate expected return, assess risk, and decide where capital should be allocated first.
        """)

        investment_options = [
            "Marketing Expansion",
            "Product Development",
            "Sales Team Expansion",
            "AI Transformation",
            "Operational Efficiency",
            "Customer Retention Program"
        ]

        selected_investment = st.selectbox(
            "Select Strategic Investment Option",
            investment_options
        )

        investment_profiles = {
            "Marketing Expansion": {
                "investment_ratio": 0.04,
                "expected_roi": 24,
                "payback": "6-9 months",
                "risk": "Medium",
                "reason": "Marketing investment can increase demand generation, brand reach, and customer acquisition, but performance depends on campaign execution and conversion quality."
            },
            "Product Development": {
                "investment_ratio": 0.06,
                "expected_roi": 30,
                "payback": "9-12 months",
                "risk": "Medium-High",
                "reason": "Product development can create long-term differentiation, but requires validation, development discipline, and market adoption."
            },
            "Sales Team Expansion": {
                "investment_ratio": 0.05,
                "expected_roi": 28,
                "payback": "6-12 months",
                "risk": "Medium",
                "reason": "Sales expansion can improve pipeline coverage and revenue conversion, but depends on hiring quality, training, and market demand."
            },
            "AI Transformation": {
                "investment_ratio": 0.07,
                "expected_roi": 38,
                "payback": "12-18 months",
                "risk": "Medium",
                "reason": "AI transformation can improve decision speed, automation, forecasting, and operational intelligence, creating scalable long-term value."
            },
            "Operational Efficiency": {
                "investment_ratio": 0.035,
                "expected_roi": 22,
                "payback": "3-6 months",
                "risk": "Low",
                "reason": "Operational efficiency investment can reduce waste, improve productivity, and protect margins with relatively lower implementation risk."
            },
            "Customer Retention Program": {
                "investment_ratio": 0.03,
                "expected_roi": 26,
                "payback": "4-8 months",
                "risk": "Low-Medium",
                "reason": "Retention investment can protect existing revenue, reduce churn, and increase customer lifetime value."
            }
        }

        selected_profile = investment_profiles[selected_investment]

        recommended_investment = total_value * selected_profile["investment_ratio"]
        expected_return = recommended_investment * (selected_profile["expected_roi"] / 100)
        total_projected_value = recommended_investment + expected_return

        ia1, ia2, ia3, ia4 = st.columns(4)

        ia1.metric("Recommended Investment", f"£{round(recommended_investment, 2)}")
        ia2.metric("Expected ROI", f"{selected_profile['expected_roi']}%")
        ia3.metric("Expected Return", f"£{round(expected_return, 2)}")
        ia4.metric("Payback Period", selected_profile["payback"])

        st.markdown("### Investment Risk Assessment")

        if selected_profile["risk"] == "Low":
            st.success(f"Risk Rating: {selected_profile['risk']}")
        elif selected_profile["risk"] in ["Low-Medium", "Medium"]:
            st.warning(f"Risk Rating: {selected_profile['risk']}")
        else:
            st.error(f"Risk Rating: {selected_profile['risk']}")

        st.markdown("### Investment Rationale")
        st.info(selected_profile["reason"])

        st.markdown("### Capital Allocation Recommendation")

        if selected_profile["expected_roi"] >= 35 and selected_profile["risk"] != "Medium-High":
            investment_decision = "Strongly Recommended"
            decision_message = "This investment shows strong expected return with an acceptable risk profile. It should be prioritised for strategic capital allocation."
            st.success(investment_decision)
        elif selected_profile["expected_roi"] >= 25:
            investment_decision = "Recommended with Monitoring"
            decision_message = "This investment has attractive return potential but should be monitored closely against execution risk and performance milestones."
            st.warning(investment_decision)
        else:
            investment_decision = "Selective Investment"
            decision_message = "This investment may be useful, but capital should be allocated carefully and only after higher-return opportunities are reviewed."
            st.info(investment_decision)

        st.write(decision_message)

        investment_comparison_df = pd.DataFrame([
            {
                "Initiative": option,
                "Recommended Investment": round(total_value * profile["investment_ratio"], 2),
                "Expected ROI (%)": profile["expected_roi"],
                "Expected Return": round((total_value * profile["investment_ratio"]) * (profile["expected_roi"] / 100), 2),
                "Risk Rating": profile["risk"],
                "Payback Period": profile["payback"]
            }
            for option, profile in investment_profiles.items()
        ])

        st.markdown("### Investment Portfolio Comparison")
        st.dataframe(investment_comparison_df, use_container_width=True)

        roi_fig = px.bar(
            investment_comparison_df,
            x="Initiative",
            y="Expected ROI (%)",
            title="Expected ROI by Strategic Investment Option"
        )

        st.plotly_chart(roi_fig, use_container_width=True)

        st.markdown("### Digital CEO Investment Recommendation")

        best_investment = investment_comparison_df.sort_values(
            by="Expected ROI (%)",
            ascending=False
        ).iloc[0]

        st.success(
            f"The Digital CEO recommends prioritising {best_investment['Initiative']} because it has the highest expected ROI of {best_investment['Expected ROI (%)']}%, while still requiring risk-aware implementation."
        )
        st.subheader("Autonomous Executive Meeting Generator")

        st.markdown("""
        The Autonomous Executive Meeting Generator converts enterprise intelligence,
        boardroom analysis, strategic decisions, investment recommendations,
        and future scenarios into executive meeting minutes and action plans.
        """)

        meeting_date = pd.Timestamp.today().strftime("%d %B %Y")

        st.markdown("### Executive Meeting Details")

        m1, m2 = st.columns(2)

        with m1:
            st.metric("Meeting Date", meeting_date)

        with m2:
            st.metric("Decision Score", f"{decision_score}/100")

        strategic_priority = growth_goal
        investment_priority = best_investment["Initiative"]

        st.markdown("### Executive Meeting Minutes")

        meeting_minutes = f"""
Meeting Purpose:
Review enterprise performance, strategic opportunities, investment priorities,
and future growth initiatives.

Enterprise Status:
{health_result['status']}

Decision Classification:
{decision_classification}

Strategic Priority:
{strategic_priority}

Investment Priority:
{investment_priority}

Board Vote Result:
{voting_result['final_result']}

Future Planning:
Review forecast results, competitor threats, and growth opportunities.

Conclusion:
The executive board supports continued strategic execution with risk-aware decision making.
"""

        st.text_area(
            "Generated Meeting Minutes",
            value=meeting_minutes,
            height=300
        )

        st.markdown("### Executive Action Plan")

        action_plan_df = pd.DataFrame({
            "Action Owner": [
                "CEO",
                "CFO",
                "CMO",
                "COO",
                "CRO"
            ],
            "Strategic Action": [
                f"Execute {strategic_priority} roadmap",
                f"Review funding for {investment_priority}",
                "Improve customer acquisition initiatives",
                "Improve operational efficiency",
                "Monitor strategic and operational risks"
            ],
            "Priority": [
                "High",
                "High",
                "Medium",
                "Medium",
                "High"
            ],
            "Deadline": [
                "30 Days",
                "30 Days",
                "60 Days",
                "60 Days",
                "90 Days"
            ]
        })

        st.dataframe(action_plan_df, use_container_width=True)

        st.markdown("### Executive Follow-Up Actions")

        st.success(
            f"CEO: Lead execution of the {strategic_priority} strategic roadmap."
        )

        st.success(
            f"CFO: Evaluate capital allocation for {investment_priority}."
        )

        st.success(
            "CMO: Develop customer growth and retention initiatives."
        )

        st.success(
            "COO: Improve operational performance and process efficiency."
        )

        st.success(
            "CRO: Monitor emerging strategic, market, and financial risks."
        )

        st.markdown("### Boardroom Resolution")

        st.info(
            f"""
The Executive Board has reviewed enterprise performance, strategic priorities,
investment recommendations, competitor intelligence, future simulations,
and risk assessments.

Resolution:
Proceed with strategic execution focused on '{strategic_priority}'
while prioritising investment in '{investment_priority}'.

Decision Status:
{voting_result['final_result']}
"""
        )
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
