from random import randint
from higher_lower_art import logo,vs
from higher_lower_game_data import data
print(logo)

a = data[randint(0,len(data)-1)]
a_follower = a['follower_count']
b = data[randint(0,len(data)-1)]
b_follower = b['follower_count']

score = 0
k = True
while k:
   print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
   print(vs)
   print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
   user = input("Who has more followers? Type 'A' or 'B': ").lower()

   if (user == "a" and a_follower > b_follower) or (user == "b" and b_follower > a_follower):
      score += 1
      a=b
      a_follower=b_follower
      b = data[randint(0,len(data)-1)]
      b_follower = b['follower_count']
      if b == a:
         b = data[randint(0,len(data)-1)]
         b_follower = b['follower_count']
      continue
   k = False

print("Sorry, that's wrong. Final score: ",score)