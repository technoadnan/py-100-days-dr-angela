import requests

AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v1"
API_TOKEN = "Qq7idBJmr1KNrM7NsPzfvp2MqKqM"
# API_KEY = "Y5CpzFgPByIsWvqZWDgPa432IyKCUvE9"
# API_SECRECT = "1g8OYHyKlJDjyC9i"

params = {
    "countryCode":"US",
    "keyword":"New York City",
}
headers = {
    "Authorization" : f"Bearer {API_TOKEN}",
}


class FlightSearch:

    a = requests.get(url=f"{AMADEUS_ENDPOINT}/reference-data/locations/cities", params=params, headers=headers)
    print(a.text)
    #This class is responsible for talking to the Flight Search API.
    pass

FlightSearch()