import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')


michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
michelangelo.speed(1)
leonardo.speed(1)

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
#generating random distance for turtles
random_distance = random.randrange(1,100)
random_distance1 = random.randrange(1,100)

#moving turtles forward
michelangelo.forward(random_distance)
leonardo.forward(random_distance1)
#resetting their position
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# for i in [angle] * num_sides:
#   my_turtle.forward(length)
#   my_turtle.left(i)
#for loop
new_distance = random.randrange(0,10)
for i in [new_distance] * 10:
  michelangelo.forward(i)
  leonardo.forward(i)
#not sure if its suppose to be this fast
  
#resetting their position
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# PART B - complete part B here
# pygame.init()
# screen_width=700
# screen_height=400
# window = pygame.display.set_mode([screen_width, screen_height])

# surface = pygame.display.get_surface()
# color = "aquamarine"
# points = [(0, 1), (10, 16), (20, 40)]
# surface = pygame.draw.polygon(surface, color, points)

# coords = [list]
# num_sides = [int]
# side_length = [int]
# offset = [int]

# rectangle1 = pygame.Rect(10, 30, 50, 70)

# theta = (2.0 * math.pi * side_length) / num_sides

pygame.init()
window = pygame.display.set_mode()
window.fill((255, 255, 255))

#drawing square
pygame.draw.polygon(window, pygame.Color(255,0,0), [(100,100),(100,200),(200,200),(200,100)])

pygame.display.update()
pygame.time.wait(1000)

#drawing circle
window.fill("aquamarine")

pygame.draw.circle(window, pygame.Color("orange"), (100,100), 50, 300)


pygame.display.update()
pygame.time.wait(1000)

#draw triangle
window.fill((255, 255, 255))
# pygame.draw.polygon(window, "BLACK", [[100, 100], [0, 200], [200, 200]], 5)
pygame.draw.polygon(window, color=("red"), points=[(50,100), (100,50), (150,100)])

pygame.display.update()
pygame.time.wait(1000)

#using the code below so pygame doesn't close unless you close it
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()

# window.exitonclick()
