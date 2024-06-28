import requests
import json

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.API_ENDPOINT = "https://api.sheety.co/8c6e05b8c817e140544bf493cc9a0812/flightDeals/prices"
        self.headers = {
            'Content-Type': 'application/json',
            "Authorization": "Bearer SEwLKJmhkhjdytNMLKvghgbOLgF"
        }
        self.cities = []
        self.price = {}
        self.data = requests.get(url=self.API_ENDPOINT, headers=self.headers).json()
        print(self.data)
    
    def get_cities(self): # ✅
        for j in self.data['prices']:
            self.cities.append(j["city"])
        return self.cities

    def get_price(self):
        for j in self.data['prices']:
            self.price[j["city"]] = j["lowestPrice"]
        return self.price

    def put_iata_code(self, iatacodes):
        length = len(self.data['prices'])
        for id_num in range(2,length+2): # add 2 b/c iteration starts from 2 not 0
            i = id_num
            edit_row = {
                "price" : {
                    "iataCode" : iatacodes[i-2]
                }
            }
            # print(id_num)
            requests.put(url=f"{self.API_ENDPOINT}/{id_num}", json=edit_row,headers=self.headers)


# DataManager()
