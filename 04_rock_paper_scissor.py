import random

all_choices = ['r','p','s']

computer = random.choice(all_choices)

user  = input("Enter 'r' or 'p' or 's': ")
if computer == user:
   print("Tie")
elif computer == "r" and user == "s":
   print("Computer win!!!")
   # print("Rock wins against scissors")
elif computer == "s" and user == "p":
   print("Computer win!!!")
elif computer == "p" and user == "r":
   print("computer win!!!")
else:
   print("You win!!!")
print(f"You picked {user} and computer picked {computer}")
