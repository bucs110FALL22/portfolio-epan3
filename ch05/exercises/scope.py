#multiply
def multiply(num1, num2):
  result = 0
  for i in range(num2):
    result = result + num1
  return result

#exponent
def exponent(num, exp):
  result = 1
  for i in range(exp):
    result = result * num
  return result

def square(num):
  return multiply(num, num)

def main():
  num1 = int(input("Enter 1st number to multiply: "))
  num2 = int(input("Enter 2nd number to multiply: "))
  multiplication = multiply(num1, num2)
  print(multiplication)
  
  base = int(input("Enter base number: "))
  power = int(input("Enter the power number: "))
  exp = exponent(base, power)
  print(exp)

  base1 = int(input("Enter base number to square: "))
  result = square(base1)
  print(result)
main()











# Write the following functions:
# Write a function that multiplies two numbers together using a loop and accumulator (no multiplication) and return the resulting value


# Write a function that takes a number and exponent as parameters and raises the number to the exponent and return the resulting value (no exponentiation)


# Write another function, called square, that takes a single parameter and squares it by only calling your multiplication function and return the resulting value
# Test your code by calling each function with whatever value you choose, then printing their results, i.e. the return value.



# remove vowels code
# def removeVowels(text):
#   vowels = "aeiou"
#   vowels += vowels.upper() #list of vowels
#   newtext = "" #accumulator - startingn value is empty string
#   for ch in text:
#     if ch not in vowels:
#       newtext += ch
#   return newtext

# def main():
#   mystr = input("Enter a string: ")
#   string = removeVowels(mystr)
#   print(string)
  
# main()