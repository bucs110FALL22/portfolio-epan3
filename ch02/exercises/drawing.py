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

# #Chapter 2 Turtle Exercise Solutions
# import turtle


# wn = turtle.Screen()
# franklin = turtle.Turtle()
# franklin.shape('turtle')
# width = input("what is the width of one side?")
# width = int(width)
# length = int(input("what is the length of one side?"))
# for s in range(2):
#     franklin.forward(width)
#     franklin.right(90)

#     franklin.forward(length)
#     franklin.right(90)







# wn.exitonclick()