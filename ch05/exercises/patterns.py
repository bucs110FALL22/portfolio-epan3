def star_pyramid():
  triangle = int(input("How many rows: "))
  
  for i in range(triangle):
    print((i + 1) * "*")
    
star_pyramid()

def rstar_pyramid():
  triangle = int(input("How many rows: "))
  
  for i in range(triangle+1):
    print((triangle * "*"))
    triangle = triangle - 1
rstar_pyramid()
    