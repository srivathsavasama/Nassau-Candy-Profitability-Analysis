
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Nassau Candy Profitability Demo",
    layout="wide"
)

st.title("Nassau Candy Distributor")
st.subheader("Product Line Profitability & Margin Analysis")
st.info("Demo dashboard using fictional sample data.")

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 14500, 13200, 16800, 15500, 18200],
    "Gross Profit": [4200, 5100, 4500, 6100, 5400, 6800]
})

df["Cost"] = df["Sales"] - df["Gross Profit"]
df["Profit Margin"] = (
    df["Gross Profit"] / df["Sales"] * 100
)

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Gross Profit", f"${df['Gross Profit'].sum():,.0f}")
col3.metric(
    "Profit Margin",
    f"{df['Gross Profit'].sum() / df['Sales'].sum() * 100:.2f}%"
)

st.subheader("Monthly Sales and Gross Profit")

chart_data = df.set_index("Month")[["Sales", "Gross Profit"]]
st.line_chart(chart_data)

st.subheader("Monthly Profit Margin")
st.bar_chart(df.set_index("Month")[["Profit Margin"]])

st.subheader("Sample Data")
st.dataframe(df, use_container_width=True)
