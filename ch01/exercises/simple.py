##Working With Data (Part 1)
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

##Working With Data (Part 2)
#sets variable for fee
fee = 3
#asks the user to input the current exchange rate
str_rate = input("What is the current exchange rate for Euro to Dollars?\n")
#sets the string input as an int
rate = float(str_rate)
#asks the user to input how much they want to exchange
str_amount = input("How much Euro would you like to exchange for Dollars?\n")
#sets the string input as an int 
amount = float(str_amount)
#calculates the total
total = rate * amount
#the result is a total with a $3 fee (subtracting the $3)
result = total - fee
#formatting amount to ##.00 (e.g. 1.00 or 2.99)
##may still have issues with it ask for help
format(amount, '.2f')
format(total, '.2f')
format(fee, '.2f')
format(result, '.2f')
#outputting the exchange result without fee
print("Exchanging", amount, "Euros = ${}".format(total))
#system displaying message of adding $3 fee
print("Adding the ${} fee...".format(fee))
#outputting the final result with the fee subtracted from the total
print("Your new total will be ${}".format(result))
