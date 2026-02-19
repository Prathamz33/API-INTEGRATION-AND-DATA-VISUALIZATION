# API-INTEGRATION-AND-DATA-VISUALIZATION
COMPANY NAME: CODTECH IT SOLUTIONS

NAME: PRATHAMESH JADHAV

INTERN ID: CTIS4667

DOMAIN: PYTHON PROGRAMMING

INTERN DURATION: 4 WEEKS

MENTOR NAME:MEELA SANTHOSH

 🌦️ Task 1: API Integration and Data Visualization
📌 Project Overview

This project demonstrates API integration, real-time data fetching, data processing, and interactive data visualization using Python. The objective of this task was to fetch live weather data from the OpenWeatherMap API, process the JSON response, and visualize key weather metrics through graphical representations.

The application is built as an interactive dashboard using Streamlit, which allows users to compare weather conditions across multiple cities in real time.

🎯 Objective

The main goal of this task was to:

Integrate a third-party REST API (OpenWeatherMap)

Handle HTTP requests and responses

Parse JSON data

Perform structured data handling using Pandas

Visualize data using Matplotlib and Seaborn

Build an interactive dashboard interface

🛠️ Technologies and Platforms Used

Programming Language: Python

Development Environment: Visual Studio Code (VS Code)

API Provider: OpenWeatherMap

Libraries Used:

requests – for sending HTTP GET requests

pandas – for data manipulation and DataFrame creation

matplotlib – for plotting charts

seaborn – for enhanced statistical visualization

streamlit – for creating an interactive web dashboard

🔗 API Integration

The project integrates the OpenWeatherMap REST API using an API key. The requests library is used to send HTTP GET requests to the API endpoint. Query parameters such as city name, API key, and unit type (metric) are passed dynamically.

Upon receiving a successful response (status code 200), the JSON data is parsed to extract:

Temperature (°C)

Humidity (%)

Wind Speed (m/s)

Weather Description

This structured data is then converted into a Pandas DataFrame for easier analysis and visualization.

📊 Data Processing and Visualization

After collecting weather data for multiple cities, the following visualizations were implemented:

Bar Chart (Temperature Comparison)
Displays temperature differences between selected cities using Seaborn’s barplot.

Line Plot (Humidity Levels)
Shows variation in humidity across cities.

Scatter Plot (Wind Speed Overview)
Represents wind speed with temperature-based sizing for better comparative analysis.

These visualizations help in understanding weather trends and comparative analysis in a graphical and user-friendly format.

💻 Application Workflow

User enters city names in the Streamlit sidebar.

The application sends API requests for each city.

Weather data is fetched and validated.

The data is structured into a DataFrame.

Graphs are dynamically generated and displayed.

The dashboard updates interactively.

🚀 Key Learning Outcomes

Through this task, I gained practical experience in:

Working with RESTful APIs

Handling JSON responses

Data cleaning and structuring

Exploratory Data Analysis (EDA)

Data visualization techniques

Building interactive dashboards

Error handling in API-based applications

📈 Conclusion

This project successfully demonstrates real-time API integration combined with effective data visualization techniques. It highlights how external data sources can be transformed into meaningful visual insights using Python-based tools.

The implementation showcases practical knowledge of API communication, data analysis, and dashboard development, making it a strong foundation for future data-driven applications.

OUTPUT :- [Weather Dashboard.pdf](https://github.com/user-attachments/files/25425408/Weather.Dashboard.pdf)
