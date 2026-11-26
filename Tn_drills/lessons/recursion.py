def wash_mugs(stack_size):
    # 1. Base case (The stop switch)
    if stack_size == 0:
        print("All mugs are washed! Drying hands.")
        return # Stops the function completely

    # 2. Recursive case (Action + Shrink)
    print(f"Washing mug number {stack_size}")

    # Call ourselves with one less mug!
    wash_mugs(stack_size - 1)

print(wash_mugs(7))

def count_down(cups):
    if cups <= 0:
        print("Cups finished")
        return
    print(f"Cup number {cups}")
    count_down(cups - 2)

print(count_down(8))

# This commented code returns a RecursionError
"""
def count_down(cups):
    # if cups <= 0:
    #     print("Cups finished")
    #     return
    print(f"Cup number {cups}")
    count_down(cups - 2)
    return

print(count_down(8))
"""

"""
In recursion the base case must be written first inside the function body. the base case is the stop switch like a protection before we get an infinite loop which later returns a `RecursionError: maximum recursion depth exceeded`.
"""

def sum_stack(mugs):
    if mugs <= 0:
        return 0
    return mugs + sum_stack(mugs - 1)

print(sum_stack(4))