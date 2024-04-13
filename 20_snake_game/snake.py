from turtle import Turtle
positions = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
   def __init__(self):
      self.segments = []
      self.create_snake()
      self.head = self.segments[0]

   def create_snake(self):
      for position in positions:
         self.add_seg(position)

   def add_seg(self,position):
      t = Turtle()
      t.shape("square")
      t.color("white")
      t.penup()
      t.goto(position)
      self.segments.append(t)

   def extend(self):
      self.add_seg(self.segments[-1].pos())

   def move(self):
      for seg_num in range(len(self.segments)-1,0,-1):
         new_seg = self.segments[seg_num - 1].pos()
         self.segments[seg_num].goto(new_seg)
      self.segments[0].fd(20)
   
   def up(self):
      self.segments[0].setheading(90)
   def down(self):
      self.segments[0].setheading(270)
   def left(self):
      self.segments[0].setheading(180)
   def right(self):
      self.segments[0].setheading(0)
      