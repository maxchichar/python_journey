def test_score():
    secret_recipe = "Vanilla Syrup"
    print(secret_recipe)

test_score()

# The global scope variable
shop_name = "Espresso Cart"
def print_shop():
    print("Welcome to " + shop_name)

print_shop()

# The global keyword
count = 0
def increment():
    global count
    count = count + 1
    print(count)

increment()
increment()

# Variable Lifetime(Birth and death of variable)
global_sales = 0
def make_drink():
    local_count = 0
    global global_sales

    local_count = local_count + 1
    global_sales += 1
    print(f"Local: {local_count}, Global: {global_sales}")

make_drink()
make_drink()

# The nonlocal keyword (modifying enclosing scopes)
def outer():
    x = "original"
    def inner():
        nonlocal x # This makes the inner variable read as same with the outer variable
        x = "modified"
    inner()
    print(x)

outer()

# The LEGB Rule
"""
1. Local: inside the current function.
2. Enclosing: Inside any parent nested functions.
3. Global: Outside all functions at the top level of the file.
4. Built-in: Python's pre-installed names (like `print` or `len`).
"""

"""
Global Scope (whiteboard)
    └── Outer Function Scope (assistant's notebook)
        └── Inner Function Scope (your napkin note)
"""

# Python variable lookup LEGB rule built-in scope example

# 1. Global Scope
# There is no 'len' variable defined out here.

def outer_function():
    # 2. Enclosing Scope
    # There is no 'len' variable defined here.

    def inner_function():
        # 3. Local Scope
        # There is no 'len' variable defined here either.
        
        my_list = [1, 2, 3]
        
        # Python evaluates 'len':
        # - Not in Local? Correct.
        # - Not in Enclosing? Correct.
        # - Not in Global? Correct.
        # - Found in Built-in! Executing built-in len().
        return len(my_list)

    return inner_function()

print(outer_function())  # Output: 3
