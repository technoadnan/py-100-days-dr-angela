from turtle import Turtle, Screen
from random import randint
t = Turtle()
s = Screen()
t.hideturtle()
s.setup(500,400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_axis = -70

user_bet = str(s.textinput("Make your bet","enter a color: "))
a = user_bet
user_index = colors.index(user_bet)

for i in range(len(colors)):
   t = Turtle(shape="turtle")
   all_turtles.append(t)
   t.color(colors[i])
   t.penup()
   y_axis+=30
   t.goto(-230,y_axis)
status = True

while status:
   for turtle in all_turtles:
      turtle.fd(randint(0,10))
      if turtle.xcor() >= 230:
         status = False
         if turtle.pencolor() == user_bet:
            print("winner")
         else:
            print("lost")
         

s = Screen()
s.exitonclick()
