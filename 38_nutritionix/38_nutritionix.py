# import requests
# from datetime import datetime

# GENDER = "male"
# WEIGHT_KG = 54
# HEIGHT_CM = 167
# AGE = 17

# APP_ID = "fa375371"
# API_KEY = "33782dcf2c07fd0d23e47fa80001b1bb"

# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheet_endpoint = "https://api.sheety.co/8c6e05b8c817e140544bf493cc9a0812/myworkouts/workouts"

# exercise_text = input("Tell me which exercises you did: ")

# headers = {
#    "x-app-id": APP_ID,
#    "x-app-key": API_KEY,
# }

# parameters = {
#    "query": exercise_text,
#    "gender": GENDER,
#    "weight_kg": WEIGHT_KG,
#    "height_cm": HEIGHT_CM,
#    "age": AGE
# }

# headers1 = {
#    'Content-Type': 'application/json',
#    "Authorization": "Bearer lkoyihkgmfbkgfjhklmgboprte"
# }

# response = requests.post(exercise_endpoint, json=parameters, headers=headers)
# result = response.json()
# print(result)
# ################### Start of Step 4 Solution ######################

# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")

# for exercise in result["exercises"]:
#    sheet_inputs = {
#       "workout": {
#          "date": today_date,
#          "time": now_time,
#          "exercise": exercise["name"].title(),
#          "duration": exercise["duration_min"],
#          "calories": exercise["nf_calories"]
#       }
#    }

#    sheet_response = requests.post(
#       sheet_endpoint, json=sheet_inputs, headers=headers1)
#    print(sheet_response.text)


import requests
import datetime

date = datetime.datetime.now().strftime("%Y%m%d")

NUTRITIONX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOUINT = "https://api.sheety.co/8c6e05b8c817e140544bf493cc9a0812/myworkouts/workouts"

# API_KEY = "33782dcf2c07fd0d23e47fa80001b1bb2"

headers = {
   "x-app-id" : "fa375371",
   "x-app-key" : API_KEY,

}
params = {
   "query" : "speed walk for 30 min",
   # "query" : input("etn"),
   "weight_kg" : 54,
   "height_cm" : 167,
   "age" : 17
}

# response = requests.post(url=NUTRITIONX_ENDPOINT, headers=headers, json=params)
# print(response.text)

# edit a row
edit_row = {
   "workout" : {
      "date" : "23/07/2020",
      "time" : "16:00:00",
      "exercise" : "running",
      "duration" : "22",
      "calories" : "100"
   }
}
headers = {
   'Content-Type': 'application/json',
   # "Authorization" : "Bearer lkoyihkgmfbkgfjhklmgboprte2"
}

edit = requests.post(url=SHEETY_ENDPOUINT, json=edit_row, headers=headers)
print(edit.text)