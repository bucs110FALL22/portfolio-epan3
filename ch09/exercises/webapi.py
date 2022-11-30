import json
import requests

def get_results():
  response = requests.get("https://date.nager.at/api/v3/CountryInfo/143").json()
  print(response)
get_results()