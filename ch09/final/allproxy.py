import requests
import BoredAPI
import NumbersAPI

def Proxy():
  '''sets a constant variable of 0'''
  '''stores proxy class as a variable'''
  '''gets api url from the proxy classes & stores in results'''
  '''formats_1 & formats_2: stores format method in a variable'''
  '''prints the formatted dictionary from api url'''
  NUM = 0
  api_1 = BoredAPI.BoredAPI()
  api_2 = NumbersAPI.NumbersAPI(NUM)
  results_1 = api_1.get()
  results_2 = api_2.get()
  formats_1 = api_1.format()
  formats_2 = api_2.format()
  print(f'{formats_1}\n{formats_2}')
  # print(formats_1)
  # print(formats_2)

# def NumbersProxy():
#   '''stores proxy class as a variable'''
#   '''gets api url from the BoredAPI class'''
#   '''formats_1: stores format method in a variable'''
#   '''prints the formatted dictionary from api url'''
#   '''sets variable NUM to a constant value of 0'''
#   '''stores proxy class as a variable'''
#   '''formats_2: stores format method in a variable'''
#   '''prints the formatted dictionary from api url'''
#   NUM = 0
#   api_2 = NumbersAPI.NumbersAPI(NUM)
#   results_2 = api_2.get()
#   formats_2 = api_2.format()
  
#   print(formats_2)

  # result = api.results()
  # print(result)

# def __str__(self):
