import streamlit as st

st.title("🔤 Interactive Text Resizer")

# Slider control
text_size = st.slider("Select Font Size (px):", min_value=12, max_value=80, value=24)
user_text = st.text_input("Type your message:", "Streamlit is Fun!")

# Render HTML with custom font size
st.markdown(
    f"<p style='font-size:{text_size}px; font-weight:bold; color:#1E88E5;'>{user_text}</p>",
    unsafe_allow_html=True
)