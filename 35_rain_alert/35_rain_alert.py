import requests  # type: ignore
import os
from twilio.rest import Client

# twilio
account_sid = 'AC51beb3069160b7d290dd29def54074312'
auth_token = '7af95e4e1e4f9e7d11e13050895af52d2'
client = Client(account_sid, auth_token)


API_KEY = "3a64b2d689d93c7766f8005afeb42b332"

parameters = {
   "lat": 13.795,
   "lon": -72.026,
   "appid": API_KEY,
   "units": "imperial",
   "cnt": 4
}

response = requests.get(
   url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)


isRain = False
text = response.json()
for j in range(4):
   weather_id = text["list"][j]["weather"][0]["id"]
   if weather_id < 700:
      isRain = True
if isRain:
   message = client.messages.create(
      from_='whatsapp:+141552388862',
      body='"Bring Umbrella"',
      to='whatsapp:+184557280882'
   )

# 4HZLCVEZKFRFSW96FC5N8AVC2