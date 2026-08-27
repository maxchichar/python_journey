# Integer + Boolean = Integer
result = 5 + True
print(result)
print(type(result)) # <class 'int'>

# In python True is treated as 1 and False is treated as 0
# Count how many True values are in a list
data = [True, False, True, True, False, True]
true_count = sum(data)
print(true_count) # 4

value = int(True)
print(value) # 1

value = int(False)
print(value) # 0

# List to string
value = str([1,2,3])
print(value) # "[1,2,3]"

# Dictionary to string
value = str({"a": 1, "b": 2})
print(value) # {'a': 1, 'b': 2}

# None to string
value = str(None)
print(value) # "None"

def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(7,7))