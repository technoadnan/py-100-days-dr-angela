from tkinter import *
from tkinter import Label, Button

THEME_COLOR = "#375362"
FONT_NAME = "Courier"


 

class QuizInterface:
   def __init__(self) -> None:
      self.score = 0 

      self.window = Tk()
      self.window.title("Quizzler")
      self.window.config(padx=20,pady=20,bg=THEME_COLOR)


      score = Label(text=f"Score: {self.score}",font=(FONT_NAME,14,"bold"),background=THEME_COLOR,foreground="#fff")
      score.grid(column=1,row=0)

      # draw a textbox 
      self.canvas = Canvas(width=300, height=250, bg="white")
      self.canvas.create_text(150, 125, text="new_question = Question(question_text, question_answer)", font=("Arial", 20, "italic"), anchor="center", width=250)
      self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

      # draw two btns
      check_img = PhotoImage(file="images/true.png")
      self.btn_check = Button(image=check_img, highlightthickness=0)
      self.btn_check.grid(row=2,column=0)

      wrong_img = PhotoImage(file="images/false.png")
      self.btn_check = Button(image=wrong_img, highlightthickness=0,)
      self.btn_check.grid(row=2,column=1)
      # self.btn_check.grid(column=3,row=0)

      

      self.window.mainloop()
   
   def right(self):pass
   def wrong(self):pass