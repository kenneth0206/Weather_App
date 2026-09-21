import tkinter as tk
import requests

# Your OpenWeather API Key
api_key = "cc5cee7e0819dac0c0eb04bc43a7f6d2"


def get_weather():

    city = city_entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data["cod"] == 200:

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        result_label.config(
            text=f"""
City: {city.title()}

Temperature: {round(temperature,1)} °C
Humidity: {humidity} %
Weather: {weather.title()}
Wind Speed: {wind_speed} m/s
"""
        )

    else:
        result_label.config(
            text="❌ City not found.\nPlease enter a valid city name."
        )


# Create Window
window = tk.Tk()
window.title("Kenneth's Weather App")
window.geometry("500x400")
window.configure(bg="lightblue")

# Heading
title_label = tk.Label(
    window,
    text="Weather App",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title_label.pack(pady=10)

# City Label
city_label = tk.Label(
    window,
    text="Enter City:",
    font=("Arial", 12),
    bg="lightblue"
)
city_label.pack()

# City Input
city_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 12)
)
city_entry.pack(pady=10)

# Weather Button
weather_button = tk.Button(
    window,
    text="Get Weather",
    command=get_weather,
    font=("Arial", 11, "bold")
)
weather_button.pack(pady=10)

# Results Label
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    bg="lightblue",
    justify="left"
)
result_label.pack(pady=20)

window.mainloop()