# Fix Greeting Bug
def fix_greeting(name):
    return f"Hello, {name}."

print(fix_greeting("Maxwell"))

# Fix Age Math
def next_age(age_text):
    age = int(age_text)
    next_year = age + 1
    return next_year

print(next_age("18"))

# Fix Safe Divide
def safe_divide(a, b):
    return round(a/b, 2) if b != 0 else "Cannot divide by zero"

print(safe_divide(8/2))