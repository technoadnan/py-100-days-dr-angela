from tkinter import *

THEME_COLOR = "#375362"
FONT_NAME = "Courier"




class QuizInterface:
   def __init__(self) -> None:
      self.window = Tk()
      self.window.title("Quizzler")
      self.window.config(padx=20,pady=20,bg=THEME_COLOR)

      score = Label(text="Score",font=(FONT_NAME,40,"bold"))
      score.grid(column=1,row=0)

      # draw a textbox 


      # draw two btns
      self.window.mainloop()
   
   def right(self):pass
   def wrong(self):pass