import csv
# with open("24_pandas/weather_data.csv") as file:
#    # print(file.readlines())
#    datafile = file.readlines()
#    data = csv.reader(datafile)
#    temperatures = []
#    for row in data:
#       temperatures.append(row[1])
#    print(temperatures)

# print("\n")


import pandas
data = pandas.read_csv("weather_data.csv")
avg = sum(data["temp"].to_list()) / len(data["temp"].tolist())

avg = data["temp"].mean()


mon = data[data.day == "Monday"].temp  # to get the certain row use conditions
print(type(mon))
print((mon * 9/5)+32)

data_dict = {
   "students": ["Amy", "James", "Angela"],
   "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("students.csv")
