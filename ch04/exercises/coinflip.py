# imports turtle
import turtle
import random

my_turtle = turtle.Turtle()

# creating turtle & compile
my_turtle.shape("turtle")

# setting outside variable for while loop
outside = False

screensize = turtle.screensize()
print(screensize)

position = my_turtle.pos()

while not outside:
  value = my_turtle.xcor() + my_turtle.ycor()
  coin = random.randrange(0,2)
  if coin == 1:
    my_turtle.left(90)
    coin = "heads"
    print(coin)
    if my_turtle.xcor() <= -200 or my_turtle.xcor() >= 200: 
      outside = True
      print("outside")
      break
  else:
    coin = "tails"
    print(coin)
    my_turtle.right(90)
    if my_turtle.ycor() <= -150 or my_turtle.ycor() >= 150: 
      outside = True
      print("outside")
      break
  my_turtle.forward(50)
  

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

#waits for the click before closing
window = turtle.Screen()
window.exitonclick()
