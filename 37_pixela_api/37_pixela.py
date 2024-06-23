import requests
import datetime

date = datetime.datetime.now().strftime("%Y%m%d")

USERNAME = "technoadnan"
# TOKEN = "irukdcmoirkfdvkmlzodkl"
ID = "book"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}"
PUT_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{ID}/{date}"
print(PUT_PIXEL_ENDPOINT)
# quantity:int = 3

user_params = {
   "token" : TOKEN,
   "username" : USERNAME,
   "agreeTermsOfService" : "yes",
   "notMinor" : "yes"
}

headers = {
   "X-USER-TOKEN" : TOKEN
}

graph_config = {
   "id" : "book",
   "name" : "Book Pages",
   "unit" : "pages",
   "type" : "int",
   "color" : "sora"
}

# to post the username for first time
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# to post the name of the page for first time
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

# post a pixel
post_pixel_config = {
   "date" : date,
   "quantity" : "3"
}
# post_pixel = requests.post(url=POST_PIXEL_ENDPOINT, headers=headers, json=post_pixel_config)
# print(post_pixel.text)

# update a existing pixel
put_pixel_config = {
   "quantity" : "2"
}
# put_pixel = requests.put(url=PUT_PIXEL_ENDPOINT, headers=headers, json=put_pixel_config)
# print(put_pixel.text)

# update graph
t = {
   "name" : "reading",
}
# print(requests.put(url=POST_PIXEL_ENDPOINT, headers=headers, json=t).text)
