# String Utility Class

class StringUtility:
  def __init__(self, string):
    self.string = string

  # String Function
  def __str__(self):
    return self.string

  # Vowels Function
  def vowels(self):
    count = 0
    for i in self.string:
      if i in "aeiouAEIOU":
        count = count + 1
    if count >= 5:
      return 'many'
    else:
      return str(count)

  # Both Ends Function
  def bothEnds(self):
    if len(self.string) <= 2:
      return ""
    else:
      return self.string[:2] + self.string[-2:]

  # Fix Start Function
  def fixStart(self):
    if len(self.string) <= 1:
      return self.string
    else:  
      return self.string[0] + self.string[1:].replace(self.string[0],'*')

  # ASCII Sum Function
  def asciiSum(self):
    sum = 0
    for i in self.string:
      sum = sum + ord(i)
    return sum  

  # Cipher Function
  def cipher(self):
    string = ""
    for i in self.string:
      if i.isalpha():
          if i.isupper():
              alphabet = (ord(i) - 65 + len(self.string)) % (26)
              alphabet += 65
          if i.islower():
              alphabet = (ord(i) - 97 + len(self.string)) % (26)
              alphabet += 97
          letter = chr(alphabet)
      else:
          letter = i
      string += letter
    return string