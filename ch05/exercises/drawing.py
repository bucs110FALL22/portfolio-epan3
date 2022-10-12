import turtle

def drawEqShape(myturtle=None, num_sides=0, side_length = 0):
  for i in num_sides * [360 / num_sides]:
    myturtle.forward(side_length)
    myturtle.left(i)

turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.color("green")
sides = int(input("Enter number of sides: "))
length = int(input("Enter side length: "))
drawEqShape(turtle, sides, length)
    

# import turtle

# def drawEqShape(myturtle=None, num_sides=0, side_length = 0, angle = 0):
#   for i in range(num_sides):
#     myturtle.forward(side_length)
#     myturtle.left(angle)

# turtle = turtle.Turtle()
# sides = int(input("Enter number of sides: "))
# length = int(input("Enter side length: "))
# angle = int(input("Enter angle: "))
# drawEqShape(turtle, sides, length, angle)