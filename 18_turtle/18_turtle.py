import turtle
import random
turtle.colormode(255)
t = turtle.Turtle()
# t.speed(1)
t.hideturtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat"]

# create a square
for _ in range(4):
   t.fd(100)
   t.right(90)
   t.fd(100)
   t.right(90)
   t.fd(100)
   t.right(90)
   t.fd(100)
   t.right(90)

# create a dashed line
for _ in range(15):
   # t.fd(10)
   t.color("white")
   t.fd(10)
   t.color("black")
   t.fd(10)

# shapes

for s in range(3, 11):
   angle = 360/s
   t.color(random.choice(colors))
   for _ in range(s):
      t.fd(100)
      t.right(angle)

t.pensize(10)
# random walk
def random_colors():
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0,255)
   return (r,g,b)
def rand_walk():
   direction = [0,90,180,270]
   t.speed(0)

   for _ in range(100):
      t.color(random_colors())
      t.fd(30)
      t.setheading(random.choice(direction))

# circle
def circle_shape():
   t.speed(0)
   t.pensize(1)
   i = 3.6
   for _ in range(100):
      t.color(random_colors())
      t.circle(100)
      t.setheading(i)
      i += 3.6

circle_shape()

turtle.exitonclick()