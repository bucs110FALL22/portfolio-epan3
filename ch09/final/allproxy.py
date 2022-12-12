import requests
import BoredAPI
import NumbersAPI

def Proxy():
  '''Sets a constant variable of 0'''
  NUM = 0

  '''Creates instances of the BoredAPI and NumbersAPI classes'''
  bored_api = BoredAPI.BoredAPI()
  numbers_api = NumbersAPI.NumbersAPI(NUM)

  '''Gets API URLs from the BoredAPI and Numbers API classes and stores in results'''
  bored_results = bored_api.get()
  numbers_results = numbers_api.get()

  '''Uses the format method to format the results and store in variables'''
  bored_formatted = bored_api.format()
  numbers_formatted = numbers_api.format()

  '''Prints the formatted results from the API URLs'''
  print(f'{bored_formatted}\n{numbers_formatted}')
