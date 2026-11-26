# Note all classes are written in PascalCase
class KioskMachine:
    pass

print(KioskMachine) # <class '__main__.KioskMachine'>

class Cup:
    pass

my_cup = Cup()
print(my_cup) # <__main__.Cup object at 0x794485dfe3f0>

"""
The special method __init__ short for initialize is a first parameter of __init__ that must always be self which represent the specific object or call it cup being manufactured.
"""

class Cup:
    def __init__(self, color):
        self.color = color

blue_cup = Cup("blue")
print(blue_cup.color)

# Accessing and Modifying Attributes
 
class Cup:
    def __init__(self):
        self.contents = "empty"

my_cup = Cup()
my_cup.contents = "Espresso"
print(my_cup.contents)

# Write a __str__ method inside your CardboardCup class that automatically prints a beautiful, human-readable receipt description when you run print(cup) instead of displaying a cryptic memory address.
class CardboardCup:
    def __init__(self, cup):
        self.cup = cup

    def __str__(self):
        return f"{self.cup}"

cup = CardboardCup("cup")
print(cup)

# AI correction
class CardboardCup:
    def __init__(self, size, drink):
        self.size = size
        self.drink = drink

    def __str__(self):
        return f"--- ITEM RECEIPT ---\nItem: {self.size} {self.drink}\nContainer: Recyclable Cardboard Cup\n--------------------"

cup = CardboardCup("Large", "Fanta")
print(cup)