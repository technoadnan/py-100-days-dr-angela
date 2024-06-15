import requests  # type: ignore
from datetime import datetime

MY_LAT = 10.3452
MY_LONG = 173.7554

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude, iss_longitude)

def is_iss_nearme():
   if (iss_latitude-5 <= MY_LAT <= iss_latitude+5) and (iss_longitude-5 <= MY_LONG <= iss_longitude+5):
      return True
   else:
      return False
   
print(is_iss_nearme())
# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
   "lat": MY_LAT,
   "lng": MY_LONG,
   "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
