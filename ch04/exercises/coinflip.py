# imports turtle
import turtle
import random

# setting turtle to a variable
my_turtle = turtle.Turtle()

# creating turtle shape
my_turtle.shape("turtle")

# printing screensize (x,y) coordinate & setting boundaries
screensize = turtle.screensize()
print(screensize)
xBound = screensize[0]//2
yBound = screensize[1]//2

# setting outside variable for while loop
outside = False

# while loop
while not outside:
  print(my_turtle.pos())
  coin = random.randrange(0,2)
  if coin == 1:
    my_turtle.left(90)
    coin = "heads"
    print(coin)
    if my_turtle.xcor() <= -xBound or my_turtle.xcor() >= xBound: 
      outside = True
      print("outside")
      break
  else:
    coin = "tails"
    print(coin)
    my_turtle.right(90)
    if my_turtle.ycor() <= -yBound or my_turtle.ycor() >= yBound: 
      outside = True
      print("outside")
      break
  my_turtle.forward(50)

#waits for the click before closing
window = turtle.Screen()
window.exitonclick()
### ^ not sure if the above is needed ###


### Lab instructions are located below for convenience.
# print(coin)
### Write a program that behaves in the following way:
# A turtle begins in the center of the screen.
# Flip a coin. 
# heads: turn to the left 90 degrees. 
# tails: turn to the right 90 degrees.
# Take 50 steps forward.
# If the turtle has moved outside the screen the program stops, otherwise go back to step 2 and repeat

# Hints:
# get the turtle moving randomly around the screen first
# Get the turtle's coordinates to calculate if the turtle is visible on screen
# You will need to use a while loop
# the condition should be based on whether the turtle is visible on the screen or not 
# Use the random library to simulate flipping a coin (50/50 odds)
# Use an if statement to determine the direction the turtle should turn
# move forward
# calculate if the turtle's position is on screen again