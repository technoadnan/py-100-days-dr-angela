import time
from turtle import Turtle

class Ball(Turtle):
   def __init__(self):
      super().__init__()
      self.shape("circle")
      self.color("white")
      self.penup()
      # self.shapesize(1,1)
      # self.goto(400,300)
   
   def move(self):
      # x = self.xcor() + .01
      # y = self.ycor() + .01
      # time.sleep(0.05)
      # self.goto(self.xcor() + .10,self.ycor() + .10)
      self.goto(self.xcor() + .05,self.ycor() + .05)
