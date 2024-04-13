from turtle import Screen, Turtle
from snake import Snake
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.listen()
snake = Snake()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



status = True
while status:
   screen.update()
   time.sleep(0.1)
   snake.move()

screen.exitonclick()
