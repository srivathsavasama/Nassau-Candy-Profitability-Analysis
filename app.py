import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Nassau Candy Profitability",
    layout="wide"
)

st.title("Nassau Candy Distributor")
st.subheader("Product Line Profitability & Margin Performance")

df = pd.read_csv("Nassau Candy Distributor.csv")

total_sales = df["Sales"].sum()
total_profit = df["Gross Profit"].sum()
total_cost = df["Cost"].sum()
margin = total_profit / total_sales * 100 if total_sales else 0

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Sales", f"${total_sales:,.2f}")
c2.metric("Gross Profit", f"${total_profit:,.2f}")
c3.metric("Total Cost", f"${total_cost:,.2f}")
c4.metric("Profit Margin", f"{margin:.2f}%")

df["Order Date"] = pd.to_datetime(
    df["Order Date"], errors="coerce"
)

monthly = (
    df.dropna(subset=["Order Date"])
    .assign(Month=lambda x: x["Order Date"].dt.to_period("M").astype(str))
    .groupby("Month")[["Sales", "Gross Profit"]]
    .sum()
)

st.subheader("Monthly Sales and Gross Profit")
st.line_chart(monthly)

st.subheader("Top 10 Products by Gross Profit")
products = (
    df.groupby("Product Name")["Gross Profit"]
    .sum()
    .nlargest(10)
    .sort_values()
)
st.bar_chart(products)
