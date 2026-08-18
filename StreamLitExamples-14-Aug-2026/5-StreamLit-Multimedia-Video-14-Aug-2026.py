import streamlit as st

st.title("📹 Media Showcase")

st.subheader("1. Watch a Video")
video_url = st.text_input("Paste YouTube Link:", "https://www.youtube.com/watch?v=rfscVS0vtbw")

if video_url:
    st.video(video_url)

st.subheader("2. Play Audio")
st.write("Upload an MP3 audio file to test:")
uploaded_audio = st.file_uploader("Choose an audio file", type=["mp3", "wav"])

if uploaded_audio is not None:
    st.audio(uploaded_audio)