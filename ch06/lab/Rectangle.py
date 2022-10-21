# defining rectangle class
class Rectangle:

# init method
  def __init__(self, x, y, h, w):
    self.x = max(0, x)
    self.y = max(0, y)
    self.height = max(0, h)
    self.width = max(0, w)

#  str (self) method
  def __str__(self):
    s = "(x: {}, y: {}) width: {}, height: {}".format(self.x, self.y, self.width, self.height)
    return s
