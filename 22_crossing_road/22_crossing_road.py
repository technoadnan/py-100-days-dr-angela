import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="w")
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
   time.sleep(0.1)
   screen.update()
   cars.random_cars()
   cars.move_cars()
   # if player.distance(cars) <= 10: # can't detect collision b/c not self
   for car in cars.cars:
      car_y = car.ycor()
      player_y = player.ycor()
      abs_y = abs(car_y - player_y)
      # No need to measure the player as we know it is always at X = 0
      abs_x = abs(car.xcor()) 
      if abs_y < 18 and abs_x <= 20: # check the middle point of the car
         # player y is 0, when car y is close to 20, it's a collosion b/c xcor() is the middle point of the turtle 
         score.game_over()
         game_is_on = False
      if player.ycor() >= 290:
         score.next_level()
         player.start()

screen.exitonclick()