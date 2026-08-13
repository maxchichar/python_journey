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

# String Slicing
slicing_word = "espresso"
Last_word = slicing_word[-1]
print(Last_word)

chris_name = "Christopher"
print(chris_name[0:5])

# String Formatting
str_name = "Alice"
drink = "latte"
drink_price = 4.50
receipt = f"Order for {str_name}: {drink} - ${drink_price:.2f}"
print(receipt)

raw_order_list = "latte,espresso,mocha"
menu_display = ""

items = raw_order_list.split(",")

menu_display = "\n".join(items)

print(menu_display)

# Golden Rule: write it once, use it millions of times.

def greet_barista():
    print("Hello, barista!")

greet_barista()

def order_drink(drink, size):
    print("Dispensing " + size + " " + drink)

order_drink("espresso", "large")

def add_tax(subtotal):
    return subtotal * 1.08

final_total = add_tax(10.0)
print(final_total)

def configure_system(device_name,/, model="core i9", *, gen=11):
    """Print the device configuration."""
    print(f"Configuring device: {device_name}")
    print(f"Model: {model}")
    print(f"Generation: {gen}")

configure_system("Hp Elitebook", "core ultra i9", gen=17)

def print_reciept(item, cost):
    print(item + ": ₦" + str(cost))

print_reciept("Espresso", 700.75)

def cup_label(name, drink):
    print(name + " ordered " + drink)
cup_label("Chibueze", "Espresso")

