#imports turtle
import turtle

my_turtle = turtle.Turtle()

#creating turtle and color
my_turtle.shape("turtle")
my_turtle.color("purple")

#variables
length = 50
square = 4
angle = 360 / square

#for loop for square
for i in [angle] * square:
  my_turtle.forward(length)
  my_turtle.left(i)

#picks pen up from paper
my_turtle.up()

#moves the hand to the left 80 units
my_turtle.backward(80)

#puts the pen back down on paper
my_turtle.down()

#creates turtle and color
my_turtle.color("red")

#for loop for square
for i in [angle] * square:
  my_turtle.forward(length)
  my_turtle.left(i)

#waits for the click before closing
window = turtle.Screen()
window.exitonclick()