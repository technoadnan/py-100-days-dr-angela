from turtle import Turtle

class PongSetup(Turtle):
   def __init__(self,x,y):
      super().__init__()
      # self.speed(0)
      self.shape("square")
      self.penup()
      self.color("white")
      self.turtlesize(5,1)
      self.goto(x,y)

   def mv_fd(self):
      self.goto(350,self.ycor()+30)
   def mv_bk(self):
      self.goto(350,self.ycor()-30)
   
      
      