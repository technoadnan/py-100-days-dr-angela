from random import randint
from higher_lower_art import logo,vs
from higher_lower_game_data import data
print(logo)

k = True
while k:
   score = 0
   a,a_follower = data[randint(0,len(data)-1)],a['follower_count']
   b,b_follower = data[randint(0,len(data)-1)],b['follower_count']

   print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
   print(vs)
   print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
   user = input("Who has more followers? Type 'A' or 'B': ").lower()

   if user == "a" and a_follower > b_follower:
      score += 1
      a=b
      a_follower=b_follower
   else:
      k = False


