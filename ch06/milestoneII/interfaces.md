# Final Project Milestone #2

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

Complete this document in **your** portfolio (CH 6). 

Let's decide on our Final project. Select the idea from Milestone 1 that seems the most interesting to you.

Each class is a model of some real world object. We often refer to data classes as the ***models*** in a GUI program. Your models represent your application data.

Given what you have learned about classes on Chapter 6, describe the ***interface only*** of 3 classes you think you might need for your project.

*For example*, if you want to create a space invaders type game, you would need a class to represent the ship, which could have an interface such as: 

* class ship
    * moveLeft()
    * moveRight()
    * shoot()

## Scene Interface

* class Scene:
  * def __init__(self, bgcolor = black, switch_screen = None, screen_width = 640, screen_height = 480):
    * self.bgcolor = bgcolor
    * self.screen_width = screen_width
    * self.screen_height = screen_height
    * self.switch_screen = switch_screen
***

## Player Interface

* class Player:
  * def __init__(self, xpos = 0, ypos = 1, lives = 3):
    * self.xpos = xpos
    * self.ypos = ypos
    * self.lives = lives
***

## Item Interface

* class Item:
  * def __init__(self, image, xpos = 0, ypos = 0, size = 1):
    * self.image = image
    * self.xpos = xpos
    * self.ypos = ypos
    * self.size = size
***    

========================

