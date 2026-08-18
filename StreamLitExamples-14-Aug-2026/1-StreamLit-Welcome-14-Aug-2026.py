import streamlit as st

st.title("🌟 Welcome to Python Web Apps!")
st.subheader("Creating web pages with simple Python code")

# User input box
user_name = st.text_input("What is your name?", "Student")

# Dynamic response
if user_name:
    st.success(f"Welcome, **{user_name}**! You are now a web developer! 🚀")

st.markdown("---")
st.caption("Built with Streamlit and Python.")