import streamlit as st                 
import requests     
from datetime import datetime                 

st.set_page_config(page_title="Weather Dashboard")
st.title("🌤️ Weather Dashboard")

city = st.text_input("Enter City Name: ", "Delhi")
api_key = st.text_input("Enter openWeatherMap API Key: ", type="password")
get_weather_btn = st.button("Get Weather")

if get_weather_btn:
    if not city or not api_key:
        st.warning("Please enter both city name and API key.")

    else:
        API_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(API_url)
            if response.status_code == 200:
                data = response.json()
                # st.write(data)
                st.subheader(city)

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

                sunrise_time = datetime.fromtimestamp(sunrise)
                sunrise_AM = sunrise_time.strftime("%I:%M %p")
                sunset_time = datetime.fromtimestamp(sunset)
                sunset_PM = sunset_time.strftime("%I:%M %p")
                visibility_unit = visibility/1000

                
                if(weather_condition == "Clear"):
                    st.subheader(f"{weather_condition} ☀️")
                elif(weather_condition == "Clouds"):
                    st.subheader(f"{weather_condition} ☁️")
                elif(weather_condition == "Rain"):
                    st.subheader(f"{weather_condition} 🌧️")
                elif(weather_condition == "Thunderstorm"):
                    st.subheader(f"{weather_condition} ⛈️")
                elif(weather_condition == "Snow"):
                    st.subheader(f"{weather_condition} ❄️")
                elif(weather_condition == "Mist"):
                    st.subheader(f"{weather_condition} 🌫️")
                else:
                    st.subheader(f"{weather_condition}")

                col1, col2 = st.columns(2)
                
                with col1:
                    # st.write(temp)
                    st.metric(label="🌡️ Temperature", value=f"{temp:.1f} °C") 
                    # st.write(feels_like)
                    st.metric(label="🤗 Feels Like", value=f"{feels_like:.1f} °C")

                    st.metric(label="🌅 Sunrise", value=f"{sunrise_AM}")

                    st.metric(label="🔵 Pressure", value=f"{pressure:.1f} hPa")

                    st.metric(label="☁️ Cloudiness Percentage", value=f"{clouds_all} %")

                with col2:
                    # st.write(humidity)
                    st.metric(label="💧Humidity", value=f"{humidity:.1f} %")

                    st.metric(label="👁️ Visibility", value=f"{visibility_unit:.1f} KM")
                    # st.write(wind_speed)
                    st.metric(label="💨 Wind Speed", value=f"{wind_speed:.1f} m/s")

                    st.metric(label="🌇 Sunset", value=f"{sunset_PM}")

               


                st.caption(weather_description)

            elif(response.status_code == 401):
                st.error("Invalid API Key")
                
            elif(response.status_code == 404):
                st.error("City not found")
            
            else:
                st.error("Something went wrong")

        except:
            st.error("Unable to connect...")