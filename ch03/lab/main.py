import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.screensize()
#makes turtle screen full screen found online stackOverflow
window.setup(width=1.0, height=1.0, startx=None, starty=None)
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
#setup for pygame and display
pygame.init()
window = pygame.display.set_mode()

#variables (not sure what to do with these)
coords = []
num_sides = 4
side_length = 100
offset = 50

#calculating sides (will figure out later)
# theta = (2.0 * math.pi * side_length) / num_sides
# print(theta)

#colors rgb (r,g,b) codes
black = (0, 0, 0)
pink = (255, 0, 225)
red = (255, 0, 0)
aquamarine = (126,255,212)
blue = (0, 0, 255)
green = (28, 224, 25)
white = (255, 255, 255)

#shapes coordinates
triangle = [(110,175),(200,20),(290,175)]
square = [(150,50),(150,150),(250,150),(250,50)]
#circle coordinates below
center = (200,100)
radius = 80
width = 300
hexagon = [(235,35),(271,97),(235,159),(163,159),(127,97),(163,35)]
nonagon = [(200,164),(160,148),(135,109),(143,65),(177,36),(223,36),(257,65),(265,110),(242,148)]

#drawing equilateral triangle
window.fill(black)
pygame.draw.polygon(window, pink, triangle)
pygame.display.update()
pygame.time.wait(3000)

#drawing square
window.fill(black)
pygame.draw.polygon(window, red, square)
pygame.display.update()
pygame.time.wait(3000)

#drawing hexagon
window.fill(black)
pygame.draw.polygon(window, blue, hexagon)
pygame.display.update()
pygame.time.wait(3000)

#drawing nonagon (ask if flipped is fine)
window.fill(black)
pygame.draw.polygon(window, green, nonagon)
pygame.display.update()
pygame.time.wait(3000)

#drawing circle
window.fill(black)
pygame.draw.circle(window, aquamarine, center, radius, width)
pygame.display.update()
pygame.time.wait(3000)

#pygame looping code so it won't close
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()


# window.exitonclick()
