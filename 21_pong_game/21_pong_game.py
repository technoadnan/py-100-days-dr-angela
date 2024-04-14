from turtle import Screen
# from controls import Control
from pong_setup import PongSetup
from ball import Ball

import time
screen = Screen()
ball = Ball()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

computer = PongSetup(x=350, y=0)
user = PongSetup(x=-350, y=0)
screen.onkey(fun=computer.mv_fd,key="w")
screen.onkey(fun=computer.mv_bk,key="s")

while True:   
   screen.update()
   ball.move()

   # collisions 
   if ball.xcor() >= 295 or ball.ycor() >= 395:
      ball.goto(ball.xcor()+0.05,ball.ycor()-0.1)
      # ball.xcor() - 10




screen.exitonclick()
