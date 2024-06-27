import requests
API_ENDPOINT = "https://api.sheety.co/8c6e05b8c817e140544bf493cc9a0812/flightDeals/prices"
headers = {
   'Content-Type': 'application/json',
   "Authorization": "Bearer SEwLKJmhkhjdytNMLKvghgbOLgF"
}

class DataManager:
    a = requests.get(url=API_ENDPOINT,headers=headers)
    print(a.text)
    #This class is responsible for talking to the Google Sheet.
    # pass

DataManager()