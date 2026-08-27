"""
break - exits the loop immediately.
continue - skips the rest of the current iteration and jumps to the next one.
"""

# break - exit the loop
for number in [1,2,3,4,5]:
    if number == 3:
        break
    print(number)

"""break is useful when you find what you are looking for and do not need to continue"""

customers = ["Amaka", "Gloria", "Favour", "Fatima", "Charles", "Chidi", "Tunde"]
search_name = "Fatima"

for customer in customers:
    if customer == search_name:
        print("Found", customer)
        break

# Using the while loop
count = 0

while True:
    print("Count: ", count)
    count += 1
    if count >= 3:
        break

print()
print("########################################################################")
print()

# continue - skip to the next iteration
for number in [1,2,3,4,5,6,7]:
    if number == 4:
        # print(number)
        continue
    print(number)

customers = [
    {"name": "Amaka", "active": True},
    {"name": "Chidi", "active": False},
    {"name": "Fatima", "active": True},
]

for customer in customers:
    if not customer["active"]:
        continue
    print("Process", customer["name"])

# Infinite loop risks

"""
count = 0

while count < 5:
    print(count)
    # Missing count += 1
     
while True:
    print("This is infinite")

"""

# Combining break and continue
for number in range(10):
    if number == 3:
        continue # Skip 3
    if number == 7:
        break # Stop at 7
    print(number)