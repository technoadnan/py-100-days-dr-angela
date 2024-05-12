##### Hard Starting Project #####
import pandas as pd
import datetime as dt
import os
import random
import smtplib
# ----------------------- CONSTANTS ----------------- # 
MY_EMAIL = "adpd1000@gmail.com"
PASSWORD = "gdek vnkh agik zzzt"
# ---------------------- DATA ---------------------- #
data = pd.read_csv("birthdays.csv", index_col=False)
info_date_month = [tuple(row) for row in data[['month', 'day']].values]
today = dt.datetime.now()
date_month = (today.month, today.day)
# ------------ READ FILE ---------------- #
letter = ""
for j in info_date_month:
   if j == date_month:
      directory = "./letter_templates"
      files = os.listdir(directory)
      random_file = random.choice(files)
      with open(os.path.join(directory, random_file), mode='r+') as file:
         letter = file.read()
         letter = letter.replace("[NAME]", data.loc[(data['month'] == today.month) & (data['day'] == today.day), 'name'].values[0])
# ------------- EMAIL ----------------- #
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
   connection.starttls()
   connection.login(user=MY_EMAIL, password=PASSWORD)
   connection.sendmail(
      from_addr=MY_EMAIL,
      to_addrs="expert.technoadnan@gmail.com",
      msg=f"Subject: Happy Birthday!\n\n{letter}"
   )