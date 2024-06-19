from tkinter import *
from tkinter import Label, Button
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Courier"


 

class QuizInterface:
   def __init__(self,quiz_brain: QuizBrain) -> None:
      self.quiz = quiz_brain

      self.window = Tk()
      self.window.title("Quizzler")
      self.window.config(padx=20,pady=20,bg=THEME_COLOR)


      self.score = Label(self.window, text=f"Score: {self.quiz.score}",font=(FONT_NAME,14,"bold"),background=THEME_COLOR,foreground="#fff")
      self.score.grid(column=1,row=0)

      # draw a textbox 
      self.canvas = Canvas(width=300, height=250, bg="white")
      self.question_text = self.canvas.create_text(150, 125, text="new_question = Question(question_text, question_answer)", font=("Arial", 20, "italic"), anchor="center", width=270)
      self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

      # draw two btns
      check_img = PhotoImage(file="images/true.png")
      self.btn_check = Button(image=check_img, highlightthickness=0, command=self.right)
      self.btn_check.grid(row=2,column=0)

      wrong_img = PhotoImage(file="images/false.png")
      self.btn_wrong = Button(image=wrong_img, highlightthickness=0, command=self.wrong)
      self.btn_wrong.grid(row=2,column=1)
      # self.btn_check.grid(column=3,row=0)

      self.get_next_question()

      self.window.mainloop()
   
   def get_next_question(self):
      self.canvas.config(bg="white")
      if self.quiz.still_has_questions():   
         self.score.config(text=f"Score: {(str(self.quiz.score))}")
         q_text = self.quiz.next_question()
         self.canvas.itemconfig(self.question_text, text=q_text)
      else:
         self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
         self.btn_check.config(state="disabled")
         self.btn_wrong.config(state="disabled")


         
   def right(self):
      self.give_feedback(self.quiz.check_answer("True"))

   def wrong(self):
      self.give_feedback(self.quiz.check_answer("False"))

   def give_feedback(self, is_right):
      if is_right:
         self.canvas.config(bg="green")
      else:
         self.canvas.config(bg="red")
         
      self.window.after(1000, self.get_next_question)
