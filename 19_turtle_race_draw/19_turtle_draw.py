from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def mv_fd():
   t.fd(10)
   # print(t.pos()[0])
def mv_bk():
   t.bk(10)
def mv_right():
   t.right(10)
def mv_left():
   t.left(10)
def clear():
   t.clear()
   t.up()
   t.home()
   t.down()

# fd
s.listen()
s.onkey(key="w",fun=mv_fd)

# bk
s.onkey(key="s",fun=mv_bk)

# right
s.onkey(key="d",fun=mv_right)
# left
s.onkey(key="a",fun=mv_left)
s.onkey(key="c",fun=clear)

s.exitonclick()