import streamlit as st
import requests
import json
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Define your Google Maps API key here
API_KEY = "AIzaSyC1RVnh-L0wZVCRKB4nKJxINAWSWZMtcwo"

st.title("Google Maps API Distance Calculator")

# Get user inputs for origin and destination

origin = st.text_input("Enter origin (e.g., 'New York, NY'):")
destination = st.text_input("Enter destination (e.g., 'Los Angeles, CA'):")

# Get travel mode from user
travel_mode = st.selectbox("Select travel mode:", ["driving", "walking", "bicycling", "transit"])

# Calculate distance and display on map
if st.button("Calculate Distance"):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&mode={travel_mode}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    distance = data["routes"][0]["legs"][0]["distance"]["text"]
    duration = data["routes"][0]["legs"][0]["duration"]["text"]
    steps = data["routes"][0]["legs"][0]["steps"]

    st.write(f"Distance: {distance}")
    st.write(f"Estimated travel time: {duration}")

    fig, ax = plt.subplots()
    for step in steps:
        polyline = step["polyline"]["points"]
        decoded_polyline = np.array([[float(p.split(',')[1]), float(p.split(',')[0])] for p in polyline.split("|")])
        ax.plot(decoded_polyline[:, 1], decoded_polyline[:, 0], color='blue')

    st.pyplot(fig)

