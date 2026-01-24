import streamlit as st
import requests
import pandas as pd

API_BASE_URL = "http://127.0.0.1:8000"

st.title("📊 Expense Analytics")

# --------------------
# Summary Section
# --------------------
st.subheader("🔎 Summary")

try:
    summary_resp = requests.get(f"{API_BASE_URL}/analytics/summary", timeout=5)

    if summary_resp.status_code == 200:
        summary = summary_resp.json()

        col1, col2 = st.columns(2)
        col1.metric("💰 Total Expense", f"₹ {summary['total_expense']:.2f}")
        col2.metric("🧾 Transactions", summary["total_transactions"])
    else:
        st.error("Failed to load summary")

except requests.exceptions.RequestException:
    st.error("Backend not reachable 🚨")

st.divider()

# --------------------
# Category-wise Chart
# --------------------
st.subheader("📂 Category-wise Spending")

try:
    cat_resp = requests.get(f"{API_BASE_URL}/analytics/category-wise", timeout=5)

    if cat_resp.status_code == 200:
        data = cat_resp.json()

        if data:
            df_cat = pd.DataFrame(data)
            st.bar_chart(
                data=df_cat,
                x="category",
                y="total_amount"
            )
        else:
            st.info("No data available for category-wise analysis")
    else:
        st.error("Failed to load category-wise data")

except requests.exceptions.RequestException:
    st.error("Backend not reachable 🚨")

st.divider()

# --------------------
# Monthly Trend Chart
# --------------------
st.subheader("📈 Monthly Expense Trend")

try:
    trend_resp = requests.get(f"{API_BASE_URL}/analytics/monthly-trend", timeout=5)

    if trend_resp.status_code == 200:
        trend_data = trend_resp.json()

        if trend_data:
            df_trend = pd.DataFrame(trend_data)
            st.line_chart(
                data=df_trend,
                x="month",
                y="total_amount"
            )
        else:
            st.info("No monthly trend data available")
    else:
        st.error("Failed to load monthly trend")

except requests.exceptions.RequestException:
    st.error("Backend not reachable 🚨")
