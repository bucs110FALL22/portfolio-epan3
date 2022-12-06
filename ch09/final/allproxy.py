import requests
import BoredAPI
import NumbersAPI

def BoredProxy():
  api_1 = BoredAPI.BoredAPI()
  results_1 = api_1.get()
  formats_1 = api_1.format()
  
  print(formats_1)

def NumbersProxy():
  api_2 = NumbersAPI.NumbersAPI(0)
  results_2 = api_2.get()
  formats_2 = api_2.format()

  print(formats_2)

  # result = api.results()
  # print(result)

# def __str__(self):
