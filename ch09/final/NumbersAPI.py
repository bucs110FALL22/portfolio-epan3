import requests

class NumbersAPI:
  def __init__(self, number):
    '''contains the api url'''
    '''input: asks user to enter a #'''
    '''storage: takes input # and stores into dictionary & api url'''
    self.api_url = 'http://numbersapi.com/random/math'
    number = int(input("\nEnter a number for a fact: "))
    self.payload = {'number': number}
    self.base_url = f"http://numbersapi.com/{self.payload['number']}?json"
    

  def __str__(self):
    '''stores f string with number chosen into a variable'''
    '''returns string'''
    string = f'You chose the number {self.payload}'
    return string

  def get(self):
    'pulls/requests data from the api url'
    'returns the converted to json/dictionary data from the api'
    self.pull_data = requests.get(self.base_url, params=self.payload)
    self.data = self.pull_data.json()
    return self.data

  def format(self):
      '''checks if result is found or not'''
      '''formats json/dictionary so it looks better'''
      '''returns the formatted data'''
      if self.data.get('text'):
        self.formatted = "\nYour Number: {number}\nNumber Fact: {text}".format(**self.data)
        return self.formatted
      else:
        result = "\nNot A Valid Number. Try Again."
        return result
# api_url = 'http://numbersapi.com/random/math?json'
# http://numbersapi.com/{number}/math?json
# response = requests.get(api_url)
# print(response.json())