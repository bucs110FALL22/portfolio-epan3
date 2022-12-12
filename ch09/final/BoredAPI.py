import requests

class BoredAPI:
  def __init__(self):
    '''asks user for input on # of people & price of desired activity'''
    '''instance variable: api_url internal stored API url'''
    '''instance variable: contains dictionary values from input received'''
    self.participants = input('Enter # Of Partcipants Activity (must be > 0): ')
    self.price = float(input('Enter the cost value for the Activity (must be bewteen 0 & 1 (0 being  free, excluding 1)): '))
    self.api_url = 'https://www.boredapi.com/api/activity'
    self.payload = {'participants': {self.participants}, 'price': {self.price}}
    
  def __str__(self):
    '''returns as a dictonary what the user entered'''
    self.chose = str(self.payload['participants'])
    return self.chose
  
  def get(self):
    '''pulls/requests data from the api url'''
    '''formats the api in a json/dictionary format'''
    '''returns the data from the api'''
    self.pull_data = requests.get(self.api_url, params=self.payload)
    self.data = self.pull_data.json()
    return self.data

  def format(self):
    '''checks if result is found or not'''
    '''formats json/dictionary so it looks better'''
    '''returns the formatted data'''
    if self.data.get('activity'):
      self.formatted = "\nActivity: {activity}\nType: {type}\nPeople: {participants}\nPrice: {price}\nAccessibility: {accessibility}".format(**self.data)
      return self.formatted
    else:
      result = "\nActivity Does Not Exist. Try Again."
      return result
    
# api_url = 'https://www.boredapi.com/api/activity?typerecreational&activity?participants=1'
# response = requests.get(api_url)
# print(response.json())