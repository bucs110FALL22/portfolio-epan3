#importing modules
import random
import pygame
import math

#setup for pygame and display
screen_width = 468
screen_height = 225

#initiate pygame & window size
pygame.init()
window = pygame.display.set_mode((screen_width,screen_height))

#colors
black = [0,0,0]
blue = [0,0,255]
red = [255,0,0]
green = [0,255,0]
yellow = [255, 255, 0]
pink = [230,0,126]

# (Source: Stack Overflow) Change color for text in shell
class bcolors:
    ENDC = '\033[0m'
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    MAGENTA = '\u001b[35;1m'
    WHITE = '\u001b[37m'
    BRIGHT_GREEN = '\u001b[32;1m'

#blue player circular dart coordinates below
center = (115,112)
radius = 113.5
width = 300
xline = [(110,226),(110,110),(110,-1)]
yline = [(0,110),(200,110),(456,110)]

#red player circulate dart coordinates below
square = [(234.7,0),(466.9,0),(466, 229.4),(234.7, 229.4)]
center1 = (350,112)
radius1 = 113.5
width1 = 300
xline1 = [(350,226),(350,110),(350,-1)]

#setting new title
pygame.display.set_caption("Dart Game")

#Part A)
#drawing blue player dartboard
window.fill(blue)
pygame.draw.circle(window, pink, center, radius, width)
pygame.draw.polygon(window, black, xline)
pygame.draw.polygon(window, black, yline)
pygame.display.update()

#drawing red player backboard and dartboard
pygame.draw.polygon(window, red, square)
pygame.draw.circle(window, pink, center1, radius1, width1)
pygame.draw.polygon(window, black, xline1)
pygame.draw.polygon(window, black, yline)
pygame.display.update()

# Player selection using mouse click event loop
input("{}Click on screen to select Player {}{}Blue{}{} or Player {}{}Red{}{}\nAfter clicking, press {}{}enter{}{} to continue...{}".format(bcolors.GREEN, bcolors.ENDC, bcolors.BLUE, bcolors.ENDC, bcolors.GREEN, bcolors.ENDC, bcolors.RED, bcolors.ENDC,bcolors.MAGENTA, bcolors.ENDC, bcolors.WHITE, bcolors.ENDC, bcolors.MAGENTA, bcolors.ENDC))

# Detecting the player's selection
open = True
while open:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONUP:
      open = False
      position = pygame.mouse.get_pos()

      if 0 <= position[0] <= 228 and 0 < position[1] <= 225:
        print("You selected player {}blue{}".format(bcolors.BLUE, 
        bcolors.ENDC))
        player = "blue"
      else:
        print("You selected player {}red{}".format(bcolors.RED, 
        bcolors.ENDC))
        player = "red"

#Part B & C)
dartWidth = 0
score_red = 0
score_blue = 0
round = 0
for i in range(10):
  round += 1
  ## blue player dart for loop
  #random dart (x,y) dart values
  dartx = random.randrange(0,228)
  darty = random.randrange(0,225)
  #settings variables to draw circle
  center1 = (dartx,darty)
  radius1 = 2.5
  center1 = (dartx,darty)
  #determining if lands in circle
  xdistance = dartx - 115
  ydistance = darty - 112
  distance_from_center = math.hypot(xdistance, ydistance)
  screen_size = radius#(screen_width * screen_height) / 2
  is_in_circle = distance_from_center <= screen_size
  not_in_circle = distance_from_center > screen_size
  if is_in_circle:
    score_blue += 1
    pygame.draw.circle(window, green, center1, radius1, dartWidth)
    pygame.display.update()
    pygame.time.wait(700)
    print("#ROUND #{}".format(round))
    print("player {}blue{} throws...hit".format(bcolors.BLUE, 
    bcolors.ENDC)) 
    
  else:
    pygame.draw.circle(window, yellow, center1, radius1, 
    dartWidth)
    pygame.display.update()
    pygame.time.wait(700)
    print("#ROUND #{}".format(round))
    print("player {}blue{} throws...miss".format(bcolors.BLUE, 
    bcolors.ENDC)) 

  ## red player dart for loop
  #random dart (x,y) dart values
  dartx = random.randrange(234,466)
  darty = random.randrange(0,225)
  #settings variables to draw circle
  center1 = (dartx,darty)
  radius1 = 2.5
  center1 = (dartx,darty)
  #determining if lands in circle
  xdistance = dartx - 350
  ydistance = darty - 112
  distance_from_center = math.hypot(xdistance, ydistance)
  screen_size = radius#(screen_width * screen_height) / 2
  is_in_circle = distance_from_center <= screen_size
  not_in_circle = distance_from_center > screen_size
  if is_in_circle:
    score_red += 1
    pygame.draw.circle(window, green, center1, radius1, dartWidth)
    pygame.display.update()
    pygame.time.wait(700)
    print("player {}red{} throws...hit".format(bcolors.RED, 
    bcolors.ENDC)) 
  else:
    pygame.draw.circle(window, yellow, center1, radius1, 
    dartWidth)
    pygame.display.update()
    pygame.time.wait(700)
    print("player {}red{} throws...miss".format(bcolors.RED, 
    bcolors.ENDC)) 

## Displaying the results
if score_red == score_blue:
  print("\nIt was a {}tie{}.".format(bcolors.YELLOW, 
  bcolors.ENDC))
  print("So your decision does not matter...")
elif score_red < score_blue:
  print("\nPlayer {}Blue{} wins.".format(bcolors.BLUE, 
  bcolors.ENDC))
  if player == "blue":
    print("You selected Player {}Blue{}.".format(bcolors.BLUE, 
    bcolors.ENDC))
    print("Congrats on guessing {}correctly{}!".format(bcolors.BRIGHT_GREEN, 
    bcolors.ENDC)) 
  else:
    print("You selected Player {}Red{}".format(bcolors.RED, 
    bcolors.ENDC))
    print("Looks like you guessed incorrectly.")
elif score_red > score_blue:
  print("\nPlayer {}Red{} wins.".format(bcolors.RED, 
  bcolors.ENDC))
  if player == "red":
    print("You selected Player {}Red{}.".format(bcolors.RED, 
    bcolors.ENDC))
    print("Congrats on guessing {}correctly{}!".format(bcolors.BRIGHT_GREEN, 
    bcolors.ENDC)) 
  else:
    print("You selected Player {}Blue{}".format(bcolors.BLUE, 
    bcolors.ENDC))
    print("Looks like you guessed incorrectly.")
    
#pygame looping code so it won't close found online
#make sure to click on the 'X' to close the program
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()

#----------------------------------------------------------------#
# Leaving previous versions of code below here in case I need it #
#----------------------------------------------------------------#
#### trying to figure out how to use while loop to alternate turns
# moves = 0
# first_player_move = True
# while True:
#   while first_player_move is True:
#     #Part B)
#     #blue player dart for loop
#     dartWidth = 0
#     for i in range(10):
#       #random dart (x,y) dart values
#       dartx = random.randrange(0,228)
#       darty = random.randrange(0,225)
#       #settings variables to draw circle
#       center1 = (dartx,darty)
#       radius1 = 2.5
#       center1 = (dartx,darty)
#       #determining if lands in circle
#       xdistance = dartx - 115
#       ydistance = darty - 112
#       distance_from_center = math.hypot(xdistance, ydistance)
#       screen_size = radius#(screen_width * screen_height) / 2
#       is_in_circle = distance_from_center <= screen_size
#       not_in_circle = distance_from_center > screen_size
#       if is_in_circle:
#         pygame.draw.circle(window, green, center1, radius1, dartWidth)
#         pygame.display.update()
#         pygame.time.wait(700)
#         moves+=1
#       else:
#         pygame.draw.circle(window, yellow, center1, radius1, 
#         dartWidth)
#         pygame.display.update()
#         pygame.time.wait(700)
#         moves+=1
#   break
#   while first_player_move is False:
#     dartWidth = 0
#     for i in range(10):
#       #random dart (x,y) dart values
#       dartx = random.randrange(234,466)
#       darty = random.randrange(0,225)
#       #settings variables to draw circle
#       center1 = (dartx,darty)
#       radius1 = 2.5
#       center1 = (dartx,darty)
#       #determining if lands in circle
#       xdistance = dartx - 350
#       ydistance = darty - 112
#       distance_from_center = math.hypot(xdistance, ydistance)
#       screen_size = radius#(screen_width * screen_height) / 2
#       is_in_circle = distance_from_center <= screen_size
#       not_in_circle = distance_from_center > screen_size
#       if is_in_circle:
#         pygame.draw.circle(window, green, center1, radius1, dartWidth)
#         pygame.display.update()
#         pygame.time.wait(700)
#       else:
#         pygame.draw.circle(window, yellow, center1, radius1, 
#         dartWidth)
#         pygame.display.update()
#         pygame.time.wait(700)
#     break
#   break
#   break

# # red player dart for loop
# dartWidth = 0
# for i in range(10):
#   #random dart (x,y) dart values
#   dartx = random.randrange(234,466)
#   darty = random.randrange(0,225)
#   #settings variables to draw circle
#   center1 = (dartx,darty)
#   radius1 = 2.5
#   center1 = (dartx,darty)
#   #determining if lands in circle
#   xdistance = dartx - 350
#   ydistance = darty - 112
#   distance_from_center = math.hypot(xdistance, ydistance)
#   screen_size = radius#(screen_width * screen_height) / 2
#   is_in_circle = distance_from_center <= screen_size
#   not_in_circle = distance_from_center > screen_size
#   if is_in_circle:
#     pygame.draw.circle(window, green, center1, radius1, dartWidth)
#     pygame.display.update()
#     pygame.time.wait(700)
#   else:
#     pygame.draw.circle(window, yellow, center1, radius1, 
#     dartWidth)
#     pygame.display.update()
#     pygame.time.wait(700)

## Not working if, elif, and else statements
# if player == "blue":
#   print("You selected Player Blue.")
#   print("Congrats on guessing correctly!") 
# elif player != "blue":
#   print("You selected Player Blue")
#   print("Looks like you guessed incorrectly.")
# if player == "red":
#   print("You selected Player Red.")
#   print("Congrats on guessing correctly!") 
# elif player != "red":
#   print("You selected Player Red")
#   print("Congrats on guessing correctly!")
# else:
#   print("You selected a player")
#   print("But it was a tie...")
##ENDC Color Formatting
    # print("player blue throws...hit")
    # print("player" + bcolors.RED + " blue " + bcolors.ENDC + "throws...hit")

##getting window size
# x, y = window.get_size()

# #checking window size
# print(x,y)

#other code in mouse click event loop
# print(position)
# if position <= (115, 112): 
# if event.type == pygame.MOUSEBUTTONUP:
#   break

# input("Click to select Player Blue or Player Red\nAfter clicking, press on the enter key to continue...")