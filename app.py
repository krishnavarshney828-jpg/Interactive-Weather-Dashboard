import streamlit as st                 
import requests                        

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
                st.subheader(city)

                main = data["main"]
                wind = data["wind"]
                weather = data["weather"]
                conditions = weather[0]

                feels_like = main["feels_like"]
                temp = main["temp"]
                humidity = main["humidity"]
                weather_condition = conditions["main"]
                weather_description = conditions["description"]
                wind_speed = wind["speed"]

                col1, col2 = st.columns(2)
                if(weather_condition == "Clear"):
                    st.subheader(f"{weather_condition} ☀️")
                elif(weather_condition == "Clouds"):
                    st.subheader(f"{weather_condition} ☁️")
                elif(weather_condition == "Rain"):
                    st.subheader(f"{weather_condition} 🌧️")
                else:
                    st.subheader(f"{weather_condition}")

                with col1:
                    # st.write(temp)
                    st.metric(label="Temperature", value=f"{temp:.1f} °C") 
                    # st.write(feels_like)
                    st.metric(label="Feels Like", value=f"{feels_like:.1f} °C")

                with col2:
                    # st.write(humidity)
                    st.metric(label="Humidity", value=f"{humidity:.1f} %")
                    # st.write(wind_speed)
                    st.metric(label="Wind Speed", value=f"{wind_speed:.1f} m/s")
                
                st.caption(weather_description)

            elif(response.status_code == 401):
                st.error("Invalid API Key")
                
            elif(response.status_code == 404):
                st.error("City not found")
            
            else:
                st.error("Something went wrong")

        except:
            st.error("Unable to connect...")