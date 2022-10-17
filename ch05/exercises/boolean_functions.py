def percentage_to_letter(score=0):
  score = float(score)
  if score < 60:
    print("F")
  elif score < 70:
    print("D")
  elif score < 80:
    print("C")
  elif score < 90:
    print("B")
  elif score >= 90:
    print("A")
  return score
inputscore = float(input("Enter your exam percentage: "))
percentage_to_letter(inputscore)

def is_passing(letter = None):
  
  if letter == "A":
    print("True")
    return True
  elif letter == "B":
    print("True")
    return True
  elif letter == "C":
    print("True")
    return True
  elif letter == "D":
    print("False")
    return False
  elif letter == "F":
    print("False")
    return False

inputletter = input("Enter your single letter grade: ")
is_passing(inputletter)

  




    
  