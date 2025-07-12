# app.py
import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="✈️ Airline Demand", layout="centered")

st.title("📈 Airline Booking Demand Dashboard")

# Fetch data from Flask API
with st.spinner("Loading data..."):
    res = requests.get("https://airline-demand-insight-app.onrender.com")
    st.code(res.text, language="json")  # See raw response
    data = res.json()

# Show Popular Routes
st.subheader("📍 Top 5 Popular Routes")
routes_df = pd.DataFrame.from_dict(data['routes'], orient='index', columns=['Bookings'])
st.bar_chart(routes_df)

# Show Price Trends
st.subheader("💰 Average Price Trends")
price_df = pd.DataFrame.from_dict(data['trends'], orient='index', columns=['Price'])
price_df.index = pd.to_datetime(price_df.index)
price_df = price_df.sort_index()
st.line_chart(price_df)

# AI Insights
st.subheader("🤖 AI-Generated Summary")
st.write(data['summary'])