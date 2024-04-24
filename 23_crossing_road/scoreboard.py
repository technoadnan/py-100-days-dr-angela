from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
   def __init__(self):
      super().__init__()
      self.current_score = 0
      self.score()

   def score(self):
      self.hideturtle()
      self.penup()
      self.goto(-250,250)
      self.color("black")
      self.write(f"Level: {self.current_score}",align="left",font=FONT)
   
   def game_over(self):
      self.goto(0,0)
      self.write("GAME OVER",align="center",font=FONT)

   def next_level(self):
      self.current_score = self.current_score + 1
      self.clear()
      self.score()


