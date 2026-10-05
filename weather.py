import requests

api_key = "your api key"


city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
print(api_key)
data = response.json()

print(data)
