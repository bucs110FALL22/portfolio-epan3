def percentage_to_letter(score=0):
  score = float(score)
  if score < 60:
    return "F"
  elif score < 70:
    return "D"
  elif score < 80:
    return "C"
  elif score < 90:
    return "B"
  elif score >= 90:
    return "A"

def is_passing(letter = None):
  
  if letter == "A":
    return True
  elif letter == "B":
    return True
  elif letter == "C":
    return True
  elif letter == "D":
    return False
  elif letter == "F":
    return False

inputscore = float(input("Enter your exam percentage: "))
result = percentage_to_letter(inputscore)
print(result)

result = is_passing(result)
print(result)