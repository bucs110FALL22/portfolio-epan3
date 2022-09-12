#imports turtle
import turtle

my_turtle = turtle.Turtle()

#list
colors = ["red", "purple"]

#creating turtle and color
my_turtle.shape("turtle")

#variables
length = 50
square = 4
angle = 360 / square

#for loop for square
for c in colors:
  my_turtle.color(c)
  for i in [angle] * square:
    my_turtle.forward(length)
    my_turtle.left(i)
  
  #picks pen up from paper
  my_turtle.up()
  #moves the hand to the left 80 units
  my_turtle.backward(80)
  #puts the pen back down on paper
  my_turtle.down()
  
#waits for the click before closing
window = turtle.Screen()
window.exitonclick()

#note: constant can be a variable in all caps