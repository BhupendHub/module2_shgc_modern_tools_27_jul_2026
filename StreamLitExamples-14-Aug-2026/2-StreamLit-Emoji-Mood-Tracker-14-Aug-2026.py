import streamlit as st

st.title("😊 Daily Mood Tracker")

mood = st.radio(
    "How are you feeling today?",
    ["Happy", "Motivated", "Tired", "Stressed"]
)

if mood == "Happy":
    st.write("Awesome! Keep spreading the positive energy! 🌟")
    st.balloons()
elif mood == "Motivated":
    st.write("Great time to write some amazing code! 💻")
elif mood == "Tired":
    st.write("Remember to take a break and get a fresh glass of water. ☕")
elif mood == "Stressed":
    st.info("Take a deep breath. You are doing great! 🧘")