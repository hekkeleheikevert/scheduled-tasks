import requests
from twilio.rest import Client
import os

OWM = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
SID = os.environ.get("ACCOUNT_SID")
token = os.environ.get("AUTH_TOKEN")

parameters = {"lat": 44.954941,
              "lon": 13.955520,
              "appid": api_key,
              "cnt": 4,
              "units": "metric"}

response = requests.get(url=OWM, params=parameters)
response.raise_for_status()
data = response.json()
print(data)

will_rain = False
for hor_id in data["list"]:
    weather_id = hor_id["weather"][0]["id"]
    if weather_id <= 700:
        print(weather_id)
        will_rain = True
if will_rain:
    client = Client(SID, token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="JangaraMongara ! It will be raining today !",
        to="whatsapp:+385976494484"
    )
    print(message.status)

