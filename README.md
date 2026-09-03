# 🌤️ Interactive Weather Dashboard

A simple and interactive weather dashboard built using **Python, Streamlit, Requests, and OpenWeatherMap API**.

The application allows users to enter a city name and view its current weather information through a simple web interface.

## 🚀 Features

* 🌍 Search weather by city name
* 🌡️ Current temperature
* 🥵 Feels-like temperature
* 💧 Humidity
* 💨 Wind speed
* ☀️ Weather condition with emoji
* 📝 Weather description
* ⚠️ Invalid API key handling
* 🔍 City not found handling
* 🌐 Network connection error handling
* 📊 Clean Streamlit interface

## 🛠️ Technologies Used

* **Python**
* **Streamlit** — for building the web interface
* **Requests** — for making API requests
* **OpenWeatherMap API** — for fetching weather data

## 📂 Project Structure

```text
interactive-weather-dashboard/
│
├── weather_dashboard.py
├── README.md
└── .gitignore
```

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project folder

```bash
cd interactive-weather-dashboard
```

### 3. Install required libraries

```bash
pip install streamlit requests
```

### 4. Run the application

```bash
streamlit run weather_dashboard.py
```

The application will open in your browser.

## 🔑 API Key

This project uses the **OpenWeatherMap API**.

You need your own API key to use the application. The API key is entered through the Streamlit interface and is not hard-coded into the source code.

## 🖥️ How It Works

1. User enters a city name.
2. User enters their OpenWeatherMap API key.
3. The application sends a request to the OpenWeatherMap API.
4. The API returns weather data in JSON format.
5. Python extracts the required information from the JSON response.
6. Streamlit displays the weather information in the dashboard.


## 🔮 Future Improvements

Planned improvements for future versions:

* 🌍 Display city and country
* 🌅 Sunrise and sunset time
* 🧭 Wind direction
* 🌧️ More weather condition emojis
* 🌡️ Celsius/Fahrenheit toggle
* 🎨 Improved UI design
* 🔐 Secure API key management using Streamlit Secrets
* 📅 Extended weather forecast

## 📌 Version

**Version 1.0**

This is the initial version of the Interactive Weather Dashboard.

## 👨‍💻 Author

**Krishna Varshney**

Built as part of my journey to improve my **Python, API integration, and application development skills**.
