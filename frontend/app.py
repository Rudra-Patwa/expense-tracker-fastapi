import streamlit as st

st.set_page_config(
    page_title="Expense Tracker",
    layout="wide"
)

st.title("💰 Expense Tracking System")

st.markdown("""
### What you can do:
- ➕ Add daily expenses
- 📋 View all expenses
- 📊 Analyze spending (coming next)
""")

st.info("Use the sidebar to navigate")
