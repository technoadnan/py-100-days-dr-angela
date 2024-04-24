from turtle import Turtle

class Control(Turtle):
   def __init__(self) -> None:
      super().__init__()
      
   def mv_up(self):
      self.goto(350,10)
   