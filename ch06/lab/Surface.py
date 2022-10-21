# importing rectangle module
import Rectangle

# defining surface class
class Surface:
  # init method
  def __init__(self, filename, x, y, h, w):
    self.image = filename
    self.rect = Rectangle.Rectangle(x, y, h, w)

  # get rectangle method
  def getRect(self):
    return self.rect