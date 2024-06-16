import requests  # type: ignore
import smtplib
from datetime import datetime

MY_LAT = 2.0369
MY_LONG = -79.677

my_email = "code.technoadnan@gmail.com"
password = "vgvg daeo elaa sxis"


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

time_now = datetime.now().hour
print(sunrise,sunset)

if time_now >= sunrise and is_iss_nearme:
   with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
      connection.starttls()
      connection.login(user=my_email, password=password)
      connection.sendmail(
         from_addr=my_email,
         to_addrs="expert.technoadnan@gmail.com",
         msg="look up at the sky"
      )



# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
