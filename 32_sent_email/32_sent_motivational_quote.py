import datetime as dt
import smtplib
import random

# ----------------------- CONSTANTS ---------------------- # 
MY_EMAIL = "adpd1000@gmail.com"
PASSWORD = "gdek vnkh agik zzzt"
quote = ""
# ----------------------- DATE TIME ---------------------- #
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

# ---------------------- QUOTES -------------------------- #
with open(file="quotes.txt", encoding="UTF-8") as file:
   l_quotes = file.readlines()
   quote = random.choice(l_quotes).strip()
# print(quote.encode("utf-8"))
# --------------------- EMAIL ---------------------------- #
if day_of_week == 5:
   with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
      connection.starttls()
      connection.login(user=MY_EMAIL, password=PASSWORD)
      connection.sendmail(
         from_addr=MY_EMAIL,
         to_addrs="expert.technoadnan@gmail.com",
         msg=f"Subject:Motivational Quote\n\n{quote.encode('ascii', 'ignore').decode('ascii')}"
      )
