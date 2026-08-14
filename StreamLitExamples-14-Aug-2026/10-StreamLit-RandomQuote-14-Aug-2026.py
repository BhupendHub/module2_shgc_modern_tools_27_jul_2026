import streamlit as st
import random

st.title("💡 Inspiration & Surprises")

quotes = [
    "“The secret of getting ahead is getting started.” – Mark Twain",
    "“It always seems impossible until it's done.” – Nelson Mandela",
    "“The best way to predict the future is to create it.” – Peter Drucker",
    "“Programming isn't about what you know; it's about what you can figure out.” – Chris Pine"
]

if st.button("Get Random Quote 🎲"):
    st.subheader(random.choice(quotes))

st.markdown("---")

show_secret = st.checkbox("Show Hidden Celebration Image")

if show_secret:
    # Uses a placeholder web image
    st.image(
        "https://images.unsplash.com/photo-1513151233558-d860c5398176?w=600",
        caption="Celebration Time! You've learned Streamlit!"
    )
    st.snow()