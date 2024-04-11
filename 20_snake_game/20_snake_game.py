# from turtle import Screen, Turtle
# import time
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("Snake game")
# screen.tracer(0)

# def mv_fd(): 
#    t.fd(10)
# def mv_bk():
#    t.bk(10)
# def mv_left():
#    t.bk(10)
# def mv_right():
#    t.bk(10)


# positions = [0,-20,-40]  

# segments = []
# for i in range(3):
#    t = Turtle()
#    t.shape("square")
#    t.color("white")
#    t.penup()
#    t.goto(positions[i],0)
#    segments.append(t)

# screen.listen()
# screen.onkey(key="up",fun=mv_fd)
# screen.onkey(t.down,"down")
# screen.onkey(t.left,"Left")
# screen.onkey(t.right,"right")



# status = True
# while status:
#    screen.update()
#    time.sleep(0.1)

#    for seg_num in range(len(segments)-1,0,-1):
#       new_seg = segments[seg_num - 1].pos()
#       print(new_seg)
#       segments[seg_num].goto(new_seg)
#    segments[0].fd(20)
#    segments[0].left(90)

# screen.exitonclick()


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
