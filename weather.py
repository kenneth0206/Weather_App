import requests

api_key = "cc5cee7e0819dac0c0eb04bc43a7f6d2"


city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
print(api_key)
data = response.json()

print(data)