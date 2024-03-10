import random
import hangman_words, hangman_art

chosen_word = random.choice(hangman_words.word_list)
lives = 6


display = []
for j in chosen_word: # ["_", "_", "_", "_", "_"]
   display.append('_');

print(hangman_art.logo)

stages_num = 0 
while 0<=lives <= 6:
   if display.count("_") == 0:
      break
   guess = input("Guess a letter: ").lower()
   i = 0
   if guess in chosen_word:
      for letter in chosen_word:
         if letter == guess:
            if display[i] == letter:
               print("you guessed already")
            display[i] = letter
         i += 1
      print(display)
   else:
      lives = lives - 1
      print(hangman_art.stages[stages_num])
      print(f"{guess} not the word ")
      stages_num += 1

print(chosen_word);