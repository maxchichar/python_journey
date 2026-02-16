#functions
# print('a value')
# print(input('ask for a value'))

#methods -> functions for datatypes
# print('value'.upper())
# print('VALUE'.lower())
# print('value'.replace('a', '4'))

# #new functions
# print(abs(-7))
# print(max(21,7))
# print(min(21,7))
# print(len('chibueze'))

#exercise
#question: create a pythogoras theorem calculator, once it runs the code should ask the user for 2 numbers that are the width and heigth of a triangle , it should output the length of the hypotenuse. Difficulty: input always returns a string, even when number was entered. 
print("Pythogoras Theorem Calculator")
print("")
import math
from num2words import num2words # this turns numbers to words ..and it's a libary you'll have to install
width = int(input("Width of the triangle: "))
print("")
height = int(input("Height of the triangle: "))
a = width ** 2 
b = pow(height, 2)
result = a + b

c = num2words(math.sqrt(result)) 
print("")
print(f"Result = {c}")
print(round(math.sqrt(result), 2)) # this rounds the result to 2 decimal places