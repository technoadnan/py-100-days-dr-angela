print("Welcome to Treasure Island.\nYour mission is to find treasure")

l_r = input("left or right?")
if l_r == "left":
   s_w = input("Swim or wait?")
   if s_w == "wait":
      color = input("which color 'red', 'yellow', 'blue' ")
      if color == "yellow":
         print("You win")
      elif color == "red":
         print("Burned in fire\nGame over")
      elif color == "blue":
         print("Eaten by beasts\nGame over")
      else:
         print("Game over")
   else:
      print("Attacked by trout.\nGame over")
else:
   print("Fall into a hole")
   print("Game Over")

