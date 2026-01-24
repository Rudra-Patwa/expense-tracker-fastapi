import streamlit as st
import requests
from datetime import date

API_BASE_URL = "http://127.0.0.1:8000"

st.title("➕ Add Expense")

with st.form("expense_form"):
    amount = st.number_input("Amount", min_value=0.0, step=0.01)
    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Rent", "Shopping", "Bills", "Other"]
    )
    description = st.text_input("Description")
    expense_date = st.date_input("Expense Date", value=date.today())
    payment_mode = st.selectbox(
        "Payment Mode",
        ["Cash", "UPI", "Card", "NetBanking"]
    )

    submitted = st.form_submit_button("Add Expense")

if submitted:
    payload = {
        "amount": amount,
        "category": category,
        "description": description,
        "expense_date": expense_date.isoformat(),
        "payment_mode": payment_mode
    }

    try:
        response = requests.post(
            f"{API_BASE_URL}/expenses",
            json=payload,
            timeout=5
        )

        if response.status_code == 200:
            st.success("Expense added successfully ✅")
        else:
            st.error(f"Failed to add expense: {response.text}")

    except requests.exceptions.RequestException as e:
        st.error("Backend is not reachable 🚨")
        st.exception(e)
