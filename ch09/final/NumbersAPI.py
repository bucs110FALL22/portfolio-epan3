import requests

class NumbersAPI:
  def __init__(self, number):
    '''
    Initialize NumbersAPI instance with instance variables api_url, payload, and base_url.
    Prompt the user to enter a number, and store it in the payload dictionary.
    '''
    self.api_url = 'http://numbersapi.com/random/math'
    number = int(input("\nEnter a number for a fact: "))
    self.payload = {'number': number}
    self.base_url = f"http://numbersapi.com/{self.payload['number']}?json"
    

  def __str__(self):
    '''
    Return a string indicating the number chosen by the user.
    '''
    string = f'You chose the number {self.payload}'
    return string

  def get(self):
    '''
    Pull data from the NumbersAPI and return it in JSON format.
    '''
    self.pull_data = requests.get(self.base_url, params=self.payload)
    self.data = self.pull_data.json()
    return self.data

  def format(self):
    '''
    Check if the returned JSON data contains a number fact, and if so, format it for readability.
    Otherwise, return a message indicating that the number is not valid.
    '''
    if self.data.get('text'):
      self.formatted = "\nYour Number: {number}\nNumber Fact: {text}".format(**self.data)
      return self.formatted
    else:
      result = "\nNot A Valid Number. Try Again."
      return result