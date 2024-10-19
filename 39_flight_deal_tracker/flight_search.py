import requests

class FlightSearch:
    def __init__(self):
        self.AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v1"
        self.AMADEUS_ENDPOINT2 = "https://test.api.amadeus.com/v2"
        self.API_TOKEN = "Rpyh4kTOXQxVvqLygbSAy2foijBJ"
        self.headers = {
            "Authorization" : f"Bearer {self.API_TOKEN}",
        }


    def generate_api_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": "Y5CpzFgPByIsWvqZWDgPa432IyKCUvE9",  # Replace {client_id} with your actual client ID
            "client_secret": "1g8OYHyKlJDjyC9i"  # Replace {client_secret} with your actual client secret
        }
        self.API_TOKEN = requests.post(url, headers=headers, data=data, verify=False).json()["access_token"]
        # updated one
        self.headers = {
            "Authorization" : f"Bearer {self.API_TOKEN}"
        }
        print(self.API_TOKEN)


    def get_iata_code(self,city_name):
        params = {
            "keyword": city_name,
        }
        headers = {
            "Authorization": f"Bearer {self.API_TOKEN}"
        }
        try:
            request_data = requests.get(url=f"{self.AMADEUS_ENDPOINT}/reference-data/locations/cities", params=params, headers=self.headers, verify=False)
            request_data.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            self.generate_api_token()
            headers["Authorization"] = f"Bearer {self.API_TOKEN}"
            request_data = requests.get(url=f"{self.AMADEUS_ENDPOINT}/reference-data/locations/cities", params=params, headers=self.headers, verify=False)
            request_data.raise_for_status()
            
        iata_code = request_data.json()["data"][0]["iataCode"]
        print(iata_code)
        return iata_code
    
    #This class is responsible for talking to the Flight Search API.

    def get_flight_offer(self, depart, arrive, departureDate, returnDate, adult=1, nonStop=False, currencyCode="USD"):
        params = {
            "originLocationCode": depart,
            "destinationLocationCode": arrive,
            "departureDate": departureDate,
            "returnDate": returnDate,
            "adults": adult,
            "nonStop": nonStop,
            "currencyCode": currencyCode,
        }
        # try:
        response = requests.get(url=f"{self.AMADEUS_ENDPOINT2}/shopping/flight-offers", params=params, headers=self.headers, verify=False)
        response.raise_for_status()
        print(response.json())
        # except requests.exceptions.HTTPError as http_err:
        #     print(f"HTTP error occurred: {http_err}")
        # except Exception as err:
        #     print(f"Other error occurred: {err}")



a = FlightSearch()
city = a.get_iata_code("Dhaka")
r = a.get_flight_offer(depart="JFK",arrive=city,departureDate="2024-08-12",returnDate="2024-08-20",adult=1,nonStop=False)
# print(r)
