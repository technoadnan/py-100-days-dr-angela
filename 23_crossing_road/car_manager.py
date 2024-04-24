from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
   def __init__(self):
      self.cars = []

   def random_cars(self):
      random_chance = random.randint(1,6)
      if random_chance == 1:
         t = Turtle()
         t.shape("square")
         t.shapesize(1,2)
         t.color(COLORS[random.randint(0,5)])
         r = random.randrange(-240,280,20)
         t.penup()
         t.left(180)
         t.goto(300,r)
         self.cars.append(t)
   
   def move_cars(self):
      for j in self.cars:
         j.fd(STARTING_MOVE_DISTANCE)
      

