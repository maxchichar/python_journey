items = {"Cocoa", "Cocoa", "Vanilla"}
print(items)
print(type(items))
print(len(items))

empty_set = set()
print(empty_set)

toppings = {"Cinnamon", "Cocoa"}
print("Cinnamon" in toppings) # True
print("Nutmeg" not in toppings) # True
print("Orange" in toppings) # False

set_a = {"Vanilla", "Mocha"}
set_b = {"Mocha", "Mint"}
print(set_a | set_b)
print(set_a & set_b) # Keeps Items that are in both trays or object's

my_tray = {"Vanilla", "Caramel", "Mocha"}
assistant_tray = {"Cocoa", "Nutmeg", "Caramel"}
unique_to_me = {} # This is an empty dictionary not set
unique_to_me = my_tray - assistant_tray
print(unique_to_me)


# Write a line of code that adds a single new bottle "G-Wagon 63" to your specials set using .add().
special_set = {"Porsche", "Ferrari", "Rolls Royce"}
special_set.add("G-Wagon 63")
print(special_set)

# Write a line of code that merges a list of new backup items ["BYD", "Xiaomi"] into your set using .update().
special_set.update(["BYD", "Xiaomi"])
print(special_set)