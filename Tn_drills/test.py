def first_and_last(value):
    if len(value)==0:
        first = ""
        last= ""
    else:
        first= value[0]
        last = value[len(value)-1]
    return {
        "first": first,
        "last": last
    }

print(first_and_last("Chibueze"))

user_input = "banana"

# Check if the string consists entirely of digits (0-9)
if user_input.isdigit():
    banana_count = int(user_input)
    print("Conversion successful!")
else:
    print("Warning: That is not valid number! Defaulting to 0.")
    banana_count = 0

value1 = "15"
value2 = "banana"
print(value1.isdigit())
print(value2.isdigit())

if (1,2): print('foo')

if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:
    print(1)
    print(2)
    if 'a' in 'qux':
        print(3)
print(4)

for count in range(3):
    print("Grind" + str(count))

weight = 0.0
while weight < 1.5:
    weight = weight + 0.5
    print("Current weight:" + str(weight))

for num in [1, 2, 3, 4, 5]:
    if num == 4:
        continue # continue is used for skipping in a loop while break stops the program.
    print(num)

text = "maxwell"
cap = text.capitalize()
print(f"Capitalize: {cap}")

# String Manipulation
customer_name = str(input("Enter your name: "))
customer_name = customer_name.strip().capitalize()
customer_types_label = str(input("Enter your order: "))
customer_order = customer_types_label.strip().capitalize()
print(f"Hello, {customer_name}! Your {customer_order} is ready.")