from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
positions = [0,-20,-40]  

segments = []
for i in range(3):
   t = Turtle()
   t.shape("square")
   t.color("white")
   t.penup()
   t.goto(positions[i],0)
   segments.append(t)

status = True
while status:
   screen.update()
   time.sleep(0.1)
   for seg in segments:
      seg.fd(20)


screen.exitonclick()