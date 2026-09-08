import streamlit as st
import requests
from datetime import datetime
from collections import Counter

st.set_page_config(page_title="Weather Dashboard")

st.title("🌤️ Weather Dashboard")

city = st.text_input("Enter City Name: ", "Delhi")
api_key = st.text_input("Enter openWeatherMap API Key: ", type="password")
get_weather_btn = st.button("Get Weather")
unit = st.radio("Temperature Units", ["Celsius (°C)", "Fahrenheit (°F)"])

if get_weather_btn:
    if not city or not api_key:
        st.warning("Please enter both city name and API key.")
    else:
        API_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        forecast_API = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(API_url)
            response_forecast = requests.get(forecast_API)

            if response.status_code == 200:
                data = response.json()
                forecast_data = response_forecast.json()

                # Current data
                main = data["main"]
                wind = data["wind"]
                weather = data["weather"]
                conditions = weather[0]
                sys = data["sys"]
                visibility = data["visibility"]
                clouds = data["clouds"]

                feels_like = main["feels_like"]
                temp = main["temp"]
                humidity = main["humidity"]
                weather_condition = conditions["main"]
                weather_description = conditions["description"]
                wind_speed = wind["speed"]
                pressure = main["pressure"]
                sunrise = sys["sunrise"]
                sunset = sys["sunset"]
                clouds_all = clouds["all"]
                country = sys["country"]

                # Forecast data
                f_list = forecast_data["list"]

                sunrise_time = datetime.fromtimestamp(sunrise)
                sunrise_AM = sunrise_time.strftime("%I:%M %p")

                sunset_time = datetime.fromtimestamp(sunset)
                sunset_PM = sunset_time.strftime("%I:%M %p")

                visibility_unit = visibility / 1000

                forecast_days = {}

                for item in f_list:
                    f_main = item["main"]

                    f_temp = f_main["temp"]
                    f_feels_like = f_main["feels_like"]
                    f_humidity = f_main["humidity"]
                    f_dt = item["dt_txt"]

                    # st.write(item)

                    f_date = f_dt[0:10]

                    if f_date not in forecast_days:
                        forecast_days[f_date] = []

                    forecast_days[f_date].append(item)

                # st.write(forecast_days)

                today = datetime.now()
                today_date = today.strftime("%Y-%m-%d")
                forecast_count = 0

                st.subheader(f"{city}, {country}")

                if weather_condition == "Clear":
                    st.subheader(f"{weather_condition} ☀️")
                elif weather_condition == "Clouds":
                    st.subheader(f"{weather_condition} ☁️")
                elif weather_condition == "Rain":
                    st.subheader(f"{weather_condition} 🌧️")
                elif weather_condition == "Thunderstorm":
                    st.subheader(f"{weather_condition} ⛈️")
                elif weather_condition == "Snow":
                    st.subheader(f"{weather_condition} ❄️")
                elif weather_condition == "Mist":
                    st.subheader(f"{weather_condition} 🌫️")
                else:
                    st.subheader(f"{weather_condition}")

                st.caption(weather_description)

                col1, col2 = st.columns(2)

                with col1:
                    if unit == "Celsius (°C)":
                        st.metric(
                            label="🌡️ Temperature",
                            value=f"{temp:.1f} °C"
                        )

                        st.metric(
                            label="🤗 Feels Like",
                            value=f"{feels_like:.1f} °C"
                        )

                    elif unit == "Fahrenheit (°F)":
                        temp_f = (temp * 9 / 5) + 32
                        feels_like_f = (feels_like * 9 / 5) + 32

                        st.metric(
                            label="🌡️ Temperature",
                            value=f"{temp_f:.1f} °F"
                        )

                        st.metric(
                            label="🤗 Feels Like",
                            value=f"{feels_like_f:.1f} °F"
                        )

                    st.metric(
                        label="🌅 Sunrise",
                        value=f"{sunrise_AM}"
                    )

                    st.metric(
                        label="🔵 Pressure",
                        value=f"{pressure:.1f} hPa"
                    )

                    st.metric(
                        label="☁️ Cloudiness Percentage",
                        value=f"{clouds_all} %"
                    )

                with col2:
                    st.metric(
                        label="💧Humidity",
                        value=f"{humidity:.1f} %"
                    )

                    st.metric(
                        label="👁️ Visibility",
                        value=f"{visibility_unit:.1f} KM"
                    )

                    st.metric(
                        label="💨 Wind Speed",
                        value=f"{wind_speed:.1f} m/s"
                    )

                    st.metric(
                        label="🌇 Sunset",
                        value=f"{sunset_PM}"
                    )

                for date, records in forecast_days.items():

                    if date == today_date:
                        continue

                    temps = []
                    feels_likes = []
                    humiditys = []
                    weathers = []

                    for record in records:
                        for_temp = record["main"]["temp"]
                        for_feels_like = record["main"]["feels_like"]
                        for_humidity = record["main"]["humidity"]
                        for_weather = record["weather"][0]["main"]

                        temps.append(for_temp)
                        feels_likes.append(for_feels_like)
                        humiditys.append(for_humidity)
                        weathers.append(for_weather)

                    daily_weather = Counter(weathers)
                    common_weather = daily_weather.most_common()
                    c_weather = common_weather[0][0]

                    avg_humidity = sum(humiditys) / len(humiditys)
                    avg_feels_like = sum(feels_likes) / len(feels_likes)
                    min_temp = min(temps)
                    max_temp = max(temps)

                    st.subheader(date)

                    col1, col2, col3, col4, col5 = st.columns(5)

                    with col1:
                        st.metric(
                            label="Min Temperature",
                            value=f"{min_temp}"
                        )

                    with col2:
                        st.metric(
                            label="Max Temperature",
                            value=f"{max_temp}"
                        )

                    with col3:
                        st.metric(
                            label="Feels Like",
                            value=f"{avg_feels_like}"
                        )

                    with col4:
                        st.metric(
                            label="Humidity",
                            value=f"{avg_humidity}"
                        )

                    with col5:
                        st.metric(
                            label="Weather",
                            value=f"{c_weather}"
                        )

                    forecast_count += 1

                    if forecast_count == 4:
                        break

            elif response.status_code == 401:
                st.error("Invalid API Key")

            elif response.status_code == 404:
                st.error("City not found")

            else:
                st.error("Something went wrong")

        except:
            st.error("Unable to connect...")