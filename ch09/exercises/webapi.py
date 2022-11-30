import json
import requests

def get_results():
  #hYvqwf2BYs0Dt4YWNDiZScLRad2nvBbc
  response = requests.get("http://apilayer.net/api/")
  print(response.status_code)
get_results()