# range start, stop
for floor in range(1,6):
    print("Floor", floor)

# range start stop step
for i in range(0, 10, 2):
    print(i)

for i in range(5, 0, -1):
    print(i)

r = range(7)
print(type(r))

items = ["rice", "beans", "yam"]

for i in range(len(items)):
    print(i, items[i])