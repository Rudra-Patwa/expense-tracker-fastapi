import streamlit as st
import requests
import pandas as pd

API_BASE_URL = "http://127.0.0.1:8000"

st.title("📋 View Expenses")

try:
    response = requests.get(f"{API_BASE_URL}/expenses", timeout=5)

    if response.status_code == 200:
        expenses = response.json()

        if expenses:
            df = pd.DataFrame(expenses)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No expenses found")

    else:
        st.error("Failed to fetch expenses")

except requests.exceptions.RequestException:
    st.error("Backend is not reachable 🚨")
