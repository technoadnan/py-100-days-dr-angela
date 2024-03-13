alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print(len(alphabet))
# print(alphabet.index('z'))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
   upt_text = ""
   if direction == "decode":
      shift *= 1
   for i in text:
      if  i in text:
         position = alphabet.index(i)
         new_pos = position + shift
         if new_pos >= len(alphabet):
            new_pos = 0 + (shift-1)
         upt_text = upt_text + alphabet[new_pos%26]
      else:
         upt_text = upt_text + i
   print("The encoded text is: " + upt_text)

caesar(text=text, shift=shift, direction=direction)