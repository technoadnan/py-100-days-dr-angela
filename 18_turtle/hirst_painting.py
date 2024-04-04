import turtle, random, colorgram
turtle.colormode(255)
t = turtle.Turtle()
t.up()
t.speed(0)
CIRCLE = 20
SPACE = 50
x = -180
y = -180
t.goto(x,y)

colors = [(251, 249, 245), (209, 165, 125), (249, 234, 237), (140, 48, 106), (164, 169, 38), (244, 80, 56)]

change = [10,20,30,40,50,60,70,80,90]
for K in range(100):
   if K in change:
      t.up()
      y+= SPACE
      t.goto(x,y)
   t.color(random.choice(colors))
   t.down()
   t.dot(CIRCLE)
   t.up()
   t.fd(SPACE)
   t.down()

turtle.exitonclick()