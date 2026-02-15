# Execution Order
print('line 1')
print('line 2') # this will be ignored because it's a comment
print('line 3')

# Datatypes
print('words') # this is a string
print("words")
print(123) #integer / int
print(-10)
print(1.5) #float 

# Operations
print(3 + 3)
print(3 - 3)
print(3 * 3)
print(3 / 3)
print(10 + 0.127817)
print(7 * 'hello')
print(16 - 1 * 4 / 7 + 2)
print(16 - 1 * 4 / (7 + 2)) 

# Variables
test_value = 123
test_value += 50
print(test_value)
print(" ")

# input
user_input = input("Please write your'e Fullname: ")
print(user_input)
print(" ")

# Execise
# Question: Create a greeter app. Write Logic to ask user for their name and then print "hello {name}, have a nice day."
print("Greeter App")
print(" ")
print("Welcome To Greeter App")
print(" ")
user_name = input("what is your name? ")
print(f"hello {user_name}, have a nice day.")