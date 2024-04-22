import pandas as pd

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}


data = pd.read_csv("nato_phonetic.csv")
data_dict = {r.letter:r.code for (_,r) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


user = input("Say something").upper()
l = [data_dict[char] for char in user]
print(l)
