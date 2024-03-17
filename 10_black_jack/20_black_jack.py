import random
from black_jack_art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []


def start():
   start_stop = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
   while start_stop == "y":
      print(logo)
      global user_cards, computer_cards
      user_cards = [random.choice(cards), random.choice(cards)]
      computer_cards = [random.choice(cards), random.choice(cards)]
      print(f"Your card: {user_cards} current score: {sum(user_cards)}")
      print(f"Computer's first card: {computer_cards[0]}")
      return True

start()
second_round = True
while second_round:
   another_card = input("Type 'y' to get another card, type 'n' to pass: ")
   if another_card == 'y':
      user_cards.append(random.choice(cards))
      print(f"Your card: {user_cards} current score: {sum(user_cards)}")
      print(f"Computer first hand: {computer_cards[0]}")

      if sum(user_cards) > 21:
         print(f"Your final hand: {user_cards} final score: {sum(user_cards)}")
         print(f"Computer final hand: {computer_cards} final score: {sum(computer_cards)}")
         print("You went over")
         second_round = False
         break
      elif sum(user_cards) == 21:
         print("You win by blackjack")
   
   elif another_card == "n":
      loop_times = ((21 - sum(computer_cards))//2) + 1
      cards_play = random.randint(1, loop_times)
      for j in range(cards_play):
         computer_cards.append(random.choice(cards))
         if sum(computer_cards) > 21:
            print(f"Your final hand: {user_cards} final score: {sum(user_cards)}")
            print(f"Computer final hand: {computer_cards} final score: {sum(computer_cards)}")
            print("Opponent went over. You win 😁")
            second_round = False
            break
         elif sum(user_cards) == 21:
            print("You win by blackjack")
   