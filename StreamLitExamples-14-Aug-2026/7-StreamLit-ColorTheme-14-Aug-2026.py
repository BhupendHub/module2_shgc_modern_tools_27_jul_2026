import streamlit as st

st.title("🎨 Web App Theme Customizer")

bg_color = st.color_picker("Pick Background Color:", "#F0F2F6")
text_color = st.color_picker("Pick Text Color:", "#000000")

# Inject dynamic CSS to update application color theme
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.write("This preview shows how custom background and font colors interact in real time!")