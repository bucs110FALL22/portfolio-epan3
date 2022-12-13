import requests

class BoredAPI:
  def __init__(self):
    '''
    Initialize BoredAPI instance with instance variables api_url, participants, price, and payload.
    '''
    self.api_url = 'https://www.boredapi.com/api/activity'
    self.participants = input('Enter # Of Partcipants Activity (must be > 0): ')
    self.price = float(input('Enter the cost value for the Activity (must be bewteen 0 & 1 (0 being free, excluding 1)): '))
    self.payload = {'participants': {self.participants}, 'price': {self.price}}
    
  def __str__(self):
    '''
    Return the value of participants as a string.
    '''
    return str(self.payload['participants'])
  
  def get(self):
    '''
    Pull data from BoredAPI and return it in JSON format.
    '''
    self.pull_data = requests.get(self.api_url, params=self.payload)
    self.data = self.pull_data.json()
    return self.data

  def format(self):
    '''
    Check if the returned JSON data contains an activity, and if so, format it for readability.
    Otherwise, return a message indicating that the activity does not exist.
    '''
    if self.data.get('activity'):
      self.formatted = "\nActivity: {activity}\nType: {type}\nPeople: {participants}\nPrice: {price}\nAccessibility: {accessibility}".format(**self.data)
      return self.formatted
    else:
      result = "\nActivity Does Not Exist. Try Again."
      return result