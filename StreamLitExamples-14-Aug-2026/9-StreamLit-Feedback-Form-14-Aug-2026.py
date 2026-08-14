import streamlit as st

st.title("📋 Student Registration Form")

with st.form("student_form"):
    full_name = st.text_input("Full Name:")
    email = st.text_input("Email Address:")
    course = st.selectbox("Preferred Course:", ["Python Basics", "Web Development", "Creative Coding"])
    experience = st.select_slider("Programming Experience Level:", ["Beginner", "Intermediate", "Advanced"])
    comments = st.text_area("Why do you want to join this class?")
    
    submit_button = st.form_submit_button("Submit Application")

if submit_button:
    if full_name and email:
        st.success(f"Thank you {full_name}! Your application for **{course}** has been received.")
    else:
        st.error("Please fill out both Name and Email before submitting!")