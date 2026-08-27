# Truncation is what happens when you convert float to integer
print(int(3.14)) # 3

# Calculating how many full hours you can work without taking a break
total_minutes = 135
full_hours = int(total_minutes / 60) # 135/60 = 2.25, truncated to 2
print(f"Full hours: {full_hours}") # Output: 2

# The difference between truncation and rounding
"""
Truncation: Cuts off the decimal part (moves towards zero)
Rounding: Finds the nearest integer (up or down depending on the decimal)
"""

print(f"int(3.6): {int(3.6)}")
print(f"round(3.6): {round(3.6)}")