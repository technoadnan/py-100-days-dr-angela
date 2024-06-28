import requests

AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v1"
API_TOKEN = "Rpyh4kTOXQxVvqLygbSAy2foijBJ"
# API_KEY = "Y5CpzFgPByIsWvqZWDgPa432IyKCUvE9"
# API_SECRECT = "1g8OYHyKlJDjyC9i"


headers = {
    "Authorization" : f"Bearer {API_TOKEN}",
}


class FlightSearch:
    def __init__(self):
        pass
    
    def get_iata_code(self,city_name):
        params = {
            "keyword": city_name,
        }
        request_data = requests.get(url=f"{AMADEUS_ENDPOINT}/reference-data/locations/cities", params=params, headers=headers).json()
        iata_code = request_data["data"][0]["iataCode"]
        return iata_code
        # print(iata_code)
    
    #This class is responsible for talking to the Flight Search API.
    pass

FlightSearch()