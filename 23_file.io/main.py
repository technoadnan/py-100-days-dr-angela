# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
existing_letter = ""

with open("23_file.io/Input/Letters/starting_letter.txt") as letter:
   existing_letter = letter.read()
# print(existing_letter[0].split(" ")[1].split(",")[0][1:-1])

with open("23_file.io/Input/Names/invited_names.txt") as file:
   for j in file.readlines():
      with open("23_file.io/Input/Names/invited_names.txt") as new_letter:
         # name = existing_letter[0].split(" ")[1].split(",")[0][1:-1]
         new_letter.write(f"{existing_letter.replace('[name]',j)}")
      # names.append(j)


