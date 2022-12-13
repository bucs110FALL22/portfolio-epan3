import requests
import BoredAPI
import NumbersAPI

def Proxy():
  '''Sets a constant variable of 0'''
  '''Creates instances of the BoredAPI and NumbersAPI classes'''
  '''Gets API URLs from the BoredAPI and Numbers API classes and stores in results'''
  '''Uses the format method to format the results and store in variables'''
  '''Prints the formatted results from the API URLs'''
  NUM = 0
  bored_api = BoredAPI.BoredAPI()
  numbers_api = NumbersAPI.NumbersAPI(NUM)
  bored_results = bored_api.get()
  numbers_results = numbers_api.get()
  bored_formatted = bored_api.format()
  numbers_formatted = numbers_api.format()
  print(f'{bored_formatted}\n{numbers_formatted}')