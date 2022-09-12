import turtle

#asking user for input on sides and length
sides = input("Enter the number of sides: ")
sides = int(sides)

length = input("Enter the length of each side: ")
length = int(length)

#variables
angle = 360 / sides
angle = int(angle)

#ask user to enter the color
colors = input("Enter the color for the shape: ")

#creating turtle object
turtle.shape("turtle")
turtle.color(colors)

#for loop for drawing desired shape
for num in [angle] * sides:
  turtle.forward(length)
  turtle.left(num)

#waits for the click before closing
window = turtle.Screen()
window.exitonclick()