from Rectangle import Rectangle
from Surface import Surface

# main method
def main():
  # testing rectangle class
  print("Rectangle Class Test:")
  r = Rectangle(10, 10, 10, 10)
  assert((r.x, r.y, r.height, r.width) == (10,10,10,10))
  r = Rectangle(-1, 1, 1, 1)
  assert((r.x, r.y, r.height, r.width) == (0,1,1,1))
  r = Rectangle(1, -1, 1, 1)
  assert((r.x, r.y, r.height, r.width) == (1,0,1,1))
  r = Rectangle(1, 1, -1, 1)
  assert((r.x, r.y, r.height, r.width) == (1,1,0,1))
  r = Rectangle(1, 1, 1, -1)
  assert((r.x, r.y, r.height, r.width) == (1,1,1,0))
  print(r)
  print("Test Complete!")

  # testing surface class
  print("\nSurface Class Test:")
  s = Surface("myimage.png", 10, 10, 10, 10)
  assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10))
  srect = s.getRect()
  assert((srect.x, srect.y, srect.height, srect.width) == (10,10,10,10))
  assert s.image 
  print(s.getRect())
  print("Test Complete!")

main()