import requests
import random
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_API_KEY = "I5FEF55T5V432CVV0ZV"
ALPHA_END_POINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = "3ead24424d9cd482330b800b816ebe2027c3"
NEWS_END_POINT = "https://newsapi.org/v2/everything"

TWILIO_ACCOUNT_SID = "AC51beb3069160b7d290dd29def5407431"
TWILIO_AUTH_TOKEN = "7af95e4e1e4f29e7d11e1233050895af52d"
client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

alpha_params = {
   "function" : "TIME_SERIES_DAILY",
   "symbol" : STOCK,
   "apikey" : ALPHA_API_KEY
}
alpha_response = requests.get(ALPHA_END_POINT,params=alpha_params).json()
print(alpha_response)

yesterday = list(alpha_response["Time Series (Daily)"])[0]
yesterday_close = float(alpha_response["Time Series (Daily)"][yesterday]["4. close"])

day_before_yesterday = list(alpha_response["Time Series (Daily)"])[1]
day_before_yesterday_close = float(alpha_response["Time Series (Daily)"][day_before_yesterday]["4. close"])


fluctuations = yesterday_close - day_before_yesterday_close
percentage_fluctuations = round((fluctuations/float(day_before_yesterday_close))*100)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_params = {
   "q" : COMPANY_NAME,
   "apiKey" : NEWS_API_KEY,
   "language" : "en"
}
news_response = requests.get(NEWS_END_POINT,params=news_params).json()
top_three_art = news_response["articles"][:3]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

up_down = None
if percentage_fluctuations < 0:
   up_down = "🔻"
   percentage_fluctuations = abs(percentage_fluctuations)
else: up_down = "🔺"

formatted_article = [f"{STOCK}: {up_down}{percentage_fluctuations}%\nHeadline:{article['title']}. \nBrief: {article['description']}"  for article in top_three_art]


for article in formatted_article:
   message = client.messages.create(
      from_='whatsapp:+14152522338886',
      body=article,
      to='whatsapp:+18425537808842'
   )

