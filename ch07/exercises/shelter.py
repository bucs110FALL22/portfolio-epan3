import time

# class Shelter:
#   def __init__(self, arrival_date, adopt_date, name = None, Type = None):
#     self.name = name
#     self.arrival_date = time.strftime("%d/%m/%Y")

    
class Animal:
  def __init__(self, name, type):
    """
    __init__ parameters
    :param name: name of the animal
    :param type: type of the animal
    :return: none
    """
    self.name = name    # name of the animal
    self.type = type    # type of the animal
    self.id = id(self)  # id of the animal
    self.date_of_adoption = time.strftime("%d/%m/%Y")   # date of adoption
  
  def setAdopted(self):
    """
    setAdopted parameters
    :return: none
    """
    date = input("Enter the date of adoption(dd/mm/yy format): ")   # Take date of adoption from user
    self.date_of_adoption = date                               # set the date of adoption

  def __str__(self):
    """
    __str__ parameters
    :return: string
    """
    return "\nAnimal name: " + self.name + "\nAnimal type: " + self.type + \
       "\nAnimal id: " + str(self.id) + \
       "\nDate of adoption: " + self.date_of_adoption + ""    # return the string


def main():
  """
  main function
  :return: none
  """
  Robert = Animal("Robert", "dog")    # create an animal
  print(Robert)                   # print the animal
  #Setting new adoption date  
  Robert.setAdopted()           # set the date of adoption
  print(Robert)                # print the animal


if __name__ == "__main__":
  main()                       # call the main function
