# List: a collection of objects stored in a single variable

flavour = ["Vanilla", "Caramel", "Hazelnut", "Mocha", "Mint"]
print(flavour)
print(flavour[0])
print(flavour[-1])

specialty_set = flavour[1:-1]
print(f"Specialty set: {specialty_set}")

syrups = ["Vanilla", "Mocha", "Hazelnut", "Caramel"]
print(type(syrups))
print(syrups[1:3])

# Reversing a list using negative steps
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_numbers = numbers[::-1]
print(f"Reversed numbers: {reversed_numbers}")