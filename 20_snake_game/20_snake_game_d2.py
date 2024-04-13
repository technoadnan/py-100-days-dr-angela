from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


status = True
while status:
   screen.update()
   time.sleep(0.1)
   snake.move()

   if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
      scoreboard.gameover()
      status = False
   if snake.head.distance(food) < 15:
      food.refresh()
      snake.extend()
      scoreboard.update_scoreboard()
   
   for seg in snake.segments[1:]:
      if snake.head.distance(seg) < 10:
         status = False
         scoreboard.gameover()

screen.exitonclick()
