#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager 
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


# get the IATA code
dm = DataManager()
fs = FlightSearch()
cities = dm.get_cities() 

iata_codes = [] 
for city in cities: 
   iata_codes.append(fs.get_iata_code(city_name=city)) 
dm.put_iata_code(iata_codes)

# for city in cities:
#    fs.get_iata_code(city)

# update IATA code into the sheets 
# comapre the the prices
# https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference
# if low then sent the message and the link  


