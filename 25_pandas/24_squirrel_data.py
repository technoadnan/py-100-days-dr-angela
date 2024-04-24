import pandas
data = pandas.read_csv("squirrel_data.csv")
fur_colors = data["Primary Fur Color"]

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
   "Fur Color": ["gray", "cinnamon", "black"],
   "count": [gray, cinnamon, black]
}

pandas.DataFrame(data_dict).to_csv("fur color squirrel.csv")
