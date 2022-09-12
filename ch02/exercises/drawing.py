import turtle

#input
sides = input("Enter the number of sides: ")
sides = int(sides)

length = input("Enter the length of each side: ")
length = int(length)

#variables
angle = 360 / sides
angle = int(angle)

#creating turtle object
turtle.shape("turtle")
turtle.color("green")

#for loop for drawing desired shape
for i in [angle] * sides:
  turtle.forward(length)
  turtle.left(i)

#waits for the click before closing
window = turtle.Screen()
window.exitonclick()