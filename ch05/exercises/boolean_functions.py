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

## Test
# print(is_passing(percentage_to_letter(85)))
# print(is_passing(percentage_to_letter(65)))
# print(is_passing(percentage_to_letter(110)))
# print(is_passing(percentage_to_letter(-1)))

### Solution
# def getGrade(percentage):
#     letter = 'F'
#     if percentage >= 90:
#         letter = 'A'
#     elif percentage >= 80:
#         letter = 'B'
#     elif percentage >= 70:
#         letter = 'C'
#     elif percentage >= 60:
#         letter = 'D'
#     return letter


# def isPassing(letter):
#     if letter == 'A': 
#         return True
#     elif letter == 'B':
#         return True
#     elif letter == 'C':
#         return True
#     return False

# print(isPassing(getGrade(85)))
# print(isPassing(getGrade(65)))
# print(isPassing(getGrade(110)))
# print(isPassing(getGrade(-1)))

# def isPassing(letter):
#     #method 1
#     # if letter == "A" or letter == "B" or letter == "C":
#     # if letter == 'A': 
#     #     return True
#     # elif letter == 'B':
#     #     return True
#     # elif letter == 'C':
#     #     return True
#     # return False
#     # method 2
#     # if letter in "ABC":
#     #     return True
#     # else:
#     #     return False
#     return letter in "ABC"