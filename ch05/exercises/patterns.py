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

# #define a function
# def star_pyramid():
#     levels = int(input("Enter the desired pyramid height: "))
    
#     for i in range(1, levels + 1):
#         print("*" * i)

# #define a function
# def rstar_pyramid():
#     levels = int(input("Enter the desired pyramid height: "))
#     for i in range(levels, 0, -1):
#         print("*" * i)


# star_pyramid()
# rstar_pyramid()