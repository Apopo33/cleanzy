# app.py

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

st.title("🧺 Cleanzy Laundry - Juja, Kenya")

@st.cache_data
def load_data():
    return pd.read_csv("data/laundry_users.csv")

df = load_data()
days = df['preferred_day'].unique()
selected_day = st.sidebar.selectbox("Select Laundry Day", sorted(days))

# Filter clients by day
filtered = df[df['preferred_day'] == selected_day]

st.subheader(f"Clients requesting laundry on {selected_day}:")

# Create Folium map
juja_center = [-1.098, 37.012]
m = folium.Map(location=juja_center, zoom_start=15)

for _, row in filtered.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['user_id']} - {row['apartment']}",
        icon=folium.Icon(color='blue', icon='tint', prefix='fa')
    ).add_to(m)

st_data = st_folium(m, width=1000)

st.write("### Client Details")
st.dataframe(filtered[['user_id', 'apartment', 'preferred_day']].reset_index(drop=True))
