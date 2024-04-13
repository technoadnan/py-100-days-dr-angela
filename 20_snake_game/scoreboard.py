from food import Food
from turtle import Turtle
class Scoreboard(Turtle):
   def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
      super().__init__(shape, undobuffersize, visible)
      self.score = 0
      self.write_score()
   
   def write_score(self):
      self.hideturtle()
      self.goto(0,250)
      self.color("white")
      self.write(f"Score: {self.score}",False, align="center",font=("Arial",20,""))

   def update_scoreboard(self):
      self.clear()
      self.score += 1
      self.write_score()
   
   def gameover(self):
      self.hideturtle()
      self.goto(0,0)
      self.color("white")
      self.write(f"GAME OVER",False, align="center",font=("Arial",20,""))
