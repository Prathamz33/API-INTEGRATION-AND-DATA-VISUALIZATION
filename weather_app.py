import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- CONFIGURATION ---
API_KEY = "0e2dd69b5d99eaf776c7d9c10473b46d"  # <--- Put your API key here
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# --- FUNCTIONS ---
def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric' # Fetches temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# --- STREAMLIT DASHBOARD UI ---
st.set_page_config(page_title="Weather Dashboard", layout="wide")
st.title("🌍 City Weather Comparison Dashboard")
st.write("This dashboard fetches real-time data from the OpenWeatherMap API.")

# Sidebar for Input
st.sidebar.header("Settings")
cities_input = st.sidebar.text_input("Enter cities separated by commas", "London, New York, Mumbai, Tokyo, Paris")
cities_list = [c.strip() for c in cities_input.split(",")]

if st.sidebar.button("Fetch Data"):
    weather_list = []
    
    for city in cities_list:
        data = get_weather_data(city)
        if data:
            weather_list.append({
                "City": data['name'],
                "Temperature (°C)": data['main']['temp'],
                "Humidity (%)": data['main']['humidity'],
                "Wind Speed (m/s)": data['wind']['speed'],
                "Condition": data['weather'][0]['description'].capitalize()
            })
    
    if weather_list:
        df = pd.DataFrame(weather_list)

        # Display Data Table
        st.subheader("Raw Data from API")
        st.dataframe(df)

        # --- VISUALIZATIONS ---
        st.subheader("Visual Analysis")
        col1, col2 = st.columns(2)

        with col1:
            st.write("### Temperature Comparison")
            fig, ax = plt.subplots()
            sns.barplot(x="City", y="Temperature (°C)", data=df, palette="coolwarm", ax=ax)
            st.pyplot(fig)

        with col2:
            st.write("### Humidity Levels")
            fig, ax = plt.subplots()
            sns.lineplot(x="City", y="Humidity (%)", data=df, marker='o', color='teal', ax=ax)
            st.pyplot(fig)
            
        st.write("### Wind Speed Overview")
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.scatterplot(x="City", y="Wind Speed (m/s)", size="Temperature (°C)", data=df, ax=ax)
        st.pyplot(fig)
    else:
        st.error("Could not fetch data. Please check your API key or city names.")
else:
    st.info("Enter city names in the sidebar and click 'Fetch Data' to see the dashboard.")