import random
#Part A
#setting variables
weeks = 16
classes = 5
tuition = 6000
#calculating cost per week in a variable
cost_per_week = ((tuition / classes) / weeks)
#printing cost per week
print("Cost per week:", cost_per_week)
#setting new variable classes per week
classes_per_week = 3
#calculating cost per class
cost_per_class = cost_per_week / classes_per_week
#printing cost per class
print("Cost per class:", cost_per_class)
#number variables value & type (ints)
print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(classes_per_week, type(classes_per_week))
#equation variables value & type (floats)
print(cost_per_week, type(cost_per_week))
print(cost_per_class, type(cost_per_class))
#syntax: numbers are integers because they are set without decimals (they are whole numbers) (e.g. 16)
#syntax: equations are floats since after calculating they can be a possible decimal

#Part B
#list of data objects [int(s), float(s), and string(s)]
##all integer variables
integer = 5
integer1 = 10
##all float variables
float = 1.00
float1 = 2.00
##all string variables
string = "Hi"
string1 = "Howdy"
#saving list of choices in choice variable
choice = (integer,float,string,integer1,float1,string1)
#using "random.choice" to randomly choose a result
result = random.choice(choice)
#printing & generating the random result
print("Generating....\n[User] {}".format(result))