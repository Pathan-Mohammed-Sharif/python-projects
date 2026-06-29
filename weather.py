import requests

api_key = "552f27c9b5f60f9a029ce984e46df376"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\n------ Weather Report ------")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"].title())
    print("Wind Speed:", data["wind"]["speed"], "m/s")
else:
    print("City not found or API key is invalid.")
