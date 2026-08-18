import streamlit as st
import pandas as pd

st.title("🗺️ Indian Cities Map Explorer")

cities = {
    "New Delhi": [28.6139, 77.2090],
    "Mumbai": [19.0760, 72.8777],
    "Bengaluru": [12.9716, 77.5946],
    "Kolkata": [22.5726, 88.3639],
    "Bhopal": [23.2599, 77.4126]
}

selected_city = st.selectbox("Select a City:", list(cities.keys()))

# Get coordinates
coords = cities[selected_city]
map_df = pd.DataFrame({"lat": [coords[0]], "lon": [coords[1]]})

st.write(f"Showing location for **{selected_city}**:")
st.map(map_df, zoom=10)