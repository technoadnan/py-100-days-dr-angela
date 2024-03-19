import random

EASY_ATTEMPT = 10
HARD_ATTEMPT = 5

print("Welcome to the Number guessing game")
print("I am thiking of a number between 1 and 100")

user_level = input("Choose a difficulty. Type 'easy' or 'hard':")
random_number = random.randint(1,100)

print(random_number)
def level_difficulty(level):
   global EASY_ATTEMPT, HARD_ATTEMPT
   if level == "easy":
      attempts = EASY_ATTEMPT
   elif level == "hard":
      attempts = HARD_ATTEMPT
   
   for round in range(attempts):
      print(f"You have {attempts - round} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if guess == random_number:
         print(f"You got the answer was {random_number}")
         quit()
      else:
         if guess > random_number:
            print("Too high")
            print("Guess again")
            continue
         else:
            if guess < random_number:
               print("Too low")
               print("Guess again")
               continue
   print("You have run out of guesses")

level_difficulty(level=user_level)