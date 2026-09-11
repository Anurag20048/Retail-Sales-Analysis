from pathlib import Path
import streamlit as st
from sales import category_analysis, customer_rfm, load_data, monthly_sales, subcategory_analysis

st.set_page_config(page_title="Retail Sales Analytics", page_icon="📊", layout="wide")
df = load_data(Path(__file__).resolve().parent / "Sample - Superstore.csv")
st.title("📊 Retail Sales Analytics")
st.caption("Interactive analysis of sales, profitability, discounts, and customer value.")

c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Sales", "$"+f"{df['Sales'].sum():,.0f}")
c2.metric("Total Profit", "$"+f"{df['Profit'].sum():,.0f}")
c3.metric("Orders", f"{df['Order ID'].nunique():,}")
c4.metric("Customers", f"{df['Customer Name'].nunique():,}")

st.subheader("Sales Trend")
st.line_chart(monthly_sales(df))

left,right = st.columns(2)
with left:
    st.subheader("Sales by Category")
    st.bar_chart(category_analysis(df).set_index("Category")["Sales"])
with right:
    st.subheader("Profit by Category")
    st.bar_chart(category_analysis(df).set_index("Category")["Profit"])

st.subheader("Profit by Sub-Category")
st.bar_chart(subcategory_analysis(df).set_index("Sub-Category")["Profit"])

st.subheader("Discount vs Profit")
st.scatter_chart(df[["Discount","Profit"]])

st.subheader("Customer Segmentation")
rfm = customer_rfm(df)
st.bar_chart(rfm["Segment"].value_counts())
st.dataframe(rfm.sort_values("Monetary", ascending=False).head(20), use_container_width=True)

st.subheader("Key Business Insights")
for item in [
    "High sales do not necessarily translate into high profit.",
    "Aggressive discounting can reduce profitability and should be monitored.",
    str(len(subcategory_analysis(df).query("Profit < 0"))) + " sub-categories have negative aggregate profit.",
    "High-value customers can be prioritized for retention and targeted offers.",
]:
    st.write("• " + item)
