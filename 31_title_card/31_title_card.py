# ------------------------- IMPORTS ----------------------------- #
import tkinter as tk
import pandas as pd
import random, time 
# ------------------------- CONSTANTS -------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel",40, "italic")
FONT_WORD = ("Ariel",60, "bold")
all_words = pd.read_csv("data/french_words.csv")
t= []
# fr_w = frwo
# -------------------------- pass ------------------------------ # 
fr_word = ""
def swap():
   global fr_word
   fr_word = random.choice(all_words.French)
   canvas.itemconfig(canvas_img,image=front_img)
   title.config(text="French",background="#fff",foreground="#000")
   word.config(text=fr_word,fg="white",borderwidth=0,highlightthickness=0,background="#fff",foreground="#000")
   canvas.after(3000, right)  # Call right function after 3 seconds
   # print("hello")
def right():
   en_word = all_words[all_words.French == fr_word].English.values[0]
   canvas.itemconfig(canvas_img, image=back_img)
   title.config(text="English", background="#91c2af",foreground="white")
   word.config(text=en_word,background="#91c2af",foreground="white")

# -------------------------- keep ------------------------------#
def wrong():
   t.append(all_words.drop(columns=fr_word))
   pass



# ------------------------ UI --------------------------------- # 
window = tk.Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR, width=800, height=526,border=0,highlightthickness=0)

canvas = tk.Canvas(width=800, height=526,highlightthickness=0,borderwidth=0)
front_img = tk.PhotoImage(file="images/card_front.png")
back_img = tk.PhotoImage(file="images/card_back.png")

canvas_img = canvas.create_image(400, 526/2, image=front_img)
canvas.grid(column=0,row=0,columnspan=2)

title = tk.Label(text=f"", font=FONT_TITLE,borderwidth=0,highlightthickness=0,background="#fff",foreground="#000")
title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


word = tk.Label(text="",font=FONT_WORD)
word.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

swap()
# window.after(3000)
# print("as")


# # buttons
right_img = tk.PhotoImage(file="images/right.png")
wrong_img = tk.PhotoImage(file="images/wrong.png")

btn_right = tk.Button(window, command=swap,highlightthickness=0,image=right_img,borderwidth=0, pady=30)
btn_right.grid(column=0,row=1,pady=30)

btn_wrong = tk.Button(text="Start",command=wrong,highlightthickness=0, image=wrong_img, borderwidth=0, pady=30)
btn_wrong.grid(column=1,row=1, pady=30)

# test
# time.sleep(3)
# bg_img.config(tk.PhotoImage(file="images/card_back.png"))
# word.config(text=)

try:
   pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
   with open("data/word_to_learn.csv", mode="w") as file:
      pass

window.mainloop()
