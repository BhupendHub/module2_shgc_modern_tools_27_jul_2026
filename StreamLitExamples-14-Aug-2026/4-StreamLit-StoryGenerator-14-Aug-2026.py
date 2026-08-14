import streamlit as st

st.title("📖 The Time Traveler - Story Generator")

hero = st.text_input("Hero's Name:", "Alex")
place = st.selectbox("Choose a Destination:", ["Ancient Rome", "Cyberpunk Tokyo", "The Moon", "Medieval Castle"])
item = st.text_input("A mysterious object:", "Golden Pocket Watch")

if st.button("Generate Story ✨"):
    story = f"""
    One sunny afternoon, **{hero}** stumbled upon a strange **{item}** hidden in the attic.
    Upon touching it, a sudden flash of light transported **{hero}** straight to **{place}**!
    And that's where the greatest adventure began...
    """
    st.info(story)