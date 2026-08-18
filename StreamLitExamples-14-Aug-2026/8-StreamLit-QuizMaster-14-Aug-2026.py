import streamlit as st

st.title("🧠 Python Quick Quiz")

score = 0

q1 = st.radio("1. Which tool is used to draw shapes line-by-line?", ["Tkinter", "Turtle", "Streamlit"])
if q1 == "Turtle":
    score += 1

q2 = st.radio("2. What keyword is used to define a function in Python?", ["function", "def", "create"])
if q2 == "def":
    score += 1

q3 = st.radio("3. Streamlit web applications run in a:", ["Web Browser", "Turtle Canvas", "Terminal Only"])
if q3 == "Web Browser":
    score += 1

if st.button("Submit Answers"):
    st.write(f"### Your Final Score: {score} / 3")
    if score == 3:
        st.success("Perfect Score! You are doing amazing! 🎉")
        st.balloons()
    else:
        st.warning("Good try! Review the topics and test yourself again.")