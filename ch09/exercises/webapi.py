import json
import requests

def get_results():
  response = requests.get("http://numbersapi.com/random/math?json").json()
  # print(type(response.text))
  # print(type(response.json()))
  print(response)
get_results()