#variables
#* is multiply (e.g. 10 times 5)
multiply = 10 * 5
#** is exponent (e.g. 10 to the power of 2)
exponent = 10 ** 2
#/ is division (e.g. 15 divided by 10)
divide = 15 / 10
#// is division (e.g. 15 divide by 10 = 1.5 --> 1)
#//this is for a positive number ^^
floor_divide = 15 // 10
#// is division (e.g. -15 divide by 10 = -1.5 --> -2)
#this is for a negative number ^^
floor_divide1 = -15 // 10
#% is modulo (aka remainder) (e.g. 15 modulo 10 = 1.5 --> 5 is remainder)
modulo = 15 % 10
#% is modulo (aka remainder) (e.g. 10 modulo 15 = 10)
modulo1 = 10 % 15
#% is modulo (aka remainder) (e.g. 10 modulo 10 = 0)
#reason is there is no remainder
modulo2 = 10 % 10
#% is modulo (aka remainder) (e.g. 0 modulo 10 = 0)
#reason is there is no remainder
modulo3 = 0 % 10
#outputs 0.6666666666..... (or 2/3)
divide1 = 10 / 15
#printing the results
print("10 * 5 =", multiply)
print("10 ** 2 =", exponent)
print("15 / 10 =", divide)
print("15 // 10 =", floor_divide)
print("-15 // 10 =", floor_divide1)
print("15 % 10 =", modulo)
print("10 % 15 =", modulo1)
print("10 % 10 =", modulo2)
print("0 % 10 =", modulo3)
#this outputs a repeating decimal
print("10 / 15 =", divide1)