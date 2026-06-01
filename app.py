import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Cognitive Enterprise Twin",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Cognitive Enterprise Twin")
st.subheader("A Multi-Agent Decision Intelligence Platform for SMEs")

st.markdown("""
This prototype analyses SME business data using executive-style AI agents:
- Data Scientist Agent
- Revenue Optimization Agent
- Risk Officer Agent
- Strategy Agent
- CEO Decision Agent
""")

uploaded_file = st.file_uploader("Upload your SME business dataset", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset uploaded successfully.")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Summary")
    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", int(df.isnull().sum().sum()))

    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    if numeric_columns:
        st.subheader("Data Scientist Agent")
        selected_metric = st.selectbox("Select a numeric metric for analysis", numeric_columns)

        total_value = df[selected_metric].sum()
        average_value = df[selected_metric].mean()
        max_value = df[selected_metric].max()

        c1, c2, c3 = st.columns(3)
        c1.metric(f"Total {selected_metric}", round(total_value, 2))
        c2.metric(f"Average {selected_metric}", round(average_value, 2))
        c3.metric(f"Highest {selected_metric}", round(max_value, 2))

        st.subheader("Visual Analysis")
        fig = px.histogram(df, x=selected_metric, title=f"Distribution of {selected_metric}")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Revenue Optimization Agent")
        st.info(
            f"The selected metric '{selected_metric}' shows a total value of {round(total_value, 2)}. "
            f"The platform will use this as a base for revenue opportunity detection."
        )

        st.subheader("Risk Officer Agent")
        if df[selected_metric].isnull().sum() > 0:
            st.warning(f"Risk detected: {selected_metric} contains missing values.")
        else:
            st.success(f"No missing-value risk detected in {selected_metric}.")

        st.subheader("CEO Decision Agent")
        st.markdown(f"""
        **Executive Recommendation:**  
        The business should review the performance of **{selected_metric}** because it may represent a key driver of SME performance.  
        
        **Initial Decision:**  
        Prioritize deeper analysis of this metric to identify growth opportunities, weak areas, and strategic risks.
        """)

    else:
        st.warning("No numeric columns found. Please upload a dataset with numeric business metrics.")

else:
    st.info("Upload a CSV or Excel file to activate the Cognitive Enterprise Twin.")
