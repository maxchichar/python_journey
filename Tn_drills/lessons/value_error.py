"""
# This will raise a ValueError
value = int("not a number")
print(value)

# Decimal point in int()
user_input = "3.14"
value = int(user_input)
print(value)
"""

user_input = input("Input a number: ")
try:
    # Code that might raise an error
    value = int(user_input)
    print(f"Successfully converted to: {value}")
except ValueError:
    # Code to run if the error happens
    print("That's not a Valid number!")

print()
print("######################################################################################")
print()

def safe_convert_to_int(user_input):
    """Safely convert a string to an integer, handling ValueError"""
    try:
        value = int(user_input)
        print(f"Successfully converted to: {value}")
        return value
    except ValueError:
        print(f"Error: '{user_input}' is not as valid integer")
        return None

safe_convert_to_int("23")  # Successfully converted to: 23
safe_convert_to_int("3.14") # Error: '3.14' is not as valid integer
safe_convert_to_int("") # Error: '' is not as valid integer
safe_convert_to_int("hello") # Error: 'hello' is not as valid integer
safe_convert_to_int(" 42 ") # Successfully converted to: 42

print()
print("######################################################################################")
print()

def parse_number_safely(user_input):
    """
    Parse a number from a string, handling common formatting issues.
    Returnd a tuple: (parsed_value, error_message)
    """

    #Check for empty input
    if not user_input or user_input.strip() == "":
        return None, "Empty input provided."

    # Clean the input: remove spaces and commas
    cleaned = user_input.replace(",", "").strip()
    cleaned = cleaned.replace("₦", "")

    # Try to convert to float first (handles integers too)
    try:
        return float(cleaned), None
    except ValueError:
        return None, f"'{user_input}' is not a valid number"

# Test the function
test_input = ["22", "3.14", "2,500.50", "₦1500", "hello", "", " 100 "]
for inpt in test_input:
    value, error = parse_number_safely(inpt)
    if error:
        print(f"❌ input: '{inpt}' -> Error: {error}")
    else:
        print(f"✅ input: '{inpt}' -> Value: {value}")

print()
print("######################################################################################")
print()

"""
In a real world program when your user enters invalid input, my program should be able to do the following below:
1. Tell the user what's wrong (with a helpful message)
2. Allow them to correct their input (in an interactive program)
3. Handle the error gracefully (in production code)
"""

def get_valid_age():
    """Keep asking for age until user enters a valid number."""
    while True:
        user_input = input("Please enter your age: ")
        user_input = user_input.strip() # Remove any whitespaces in user input

        if user_input == "":
            print("Please enter something. Age cannot be empty.")
            continue
        # Error Handling for unexpected user input
        try:
            age = int(user_input)
            if age < 0:
                print("Please enter a positive number.")
                continue
            if age > 150:
                print("That seems unlikely. Please enter a realistic age.")
                continue
            return age
        except ValueError:
            print(f"Sorry, '{user_input}' is not a valid age. Please enter a number.")

age = get_valid_age(-90)
print(f"Your age is: {age}")