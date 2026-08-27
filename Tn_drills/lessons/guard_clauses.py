"""
A guard clause is a condition placed at the beginning of a block to handle an invalid or exceptional case early.
"""
balance = 12000
account_locked = False
amount = 3000

if balance <= 0:
    print("Balance is zero")
elif account_locked:
    print("Account locked")
elif amount > balance:
    print("Insufficient balance")
else:
    print("Processing withdrawal")

"""The idea of a guard clause is to handle the bad cases first, the continue with the good cases"""

# Flat guard version

customer_address = "Lagos"
rider_available = True
route_accessible = True
payment_confirmed = False

if not customer_address:
    print("Address is required")
elif not rider_available:
    print("No rider available")
elif not route_accessible:
    print("Route is in accessible")
elif not payment_confirmed:
    print("Payment not confirmed")
else:
    print("Booking confirmed")

# Guard clauses and early exits
def process_withdrawal(balance, amount):
    if amount <= 0:
        return "Invalid amount"
    elif amount > balance:
        return "Insufficient balance"
    else:
        return "Successful"

print(process_withdrawal(1000000, 7000))