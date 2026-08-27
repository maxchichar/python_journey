status = "active"

if status == "active":
    print("Account is active")
    print("You can proceed")
else:
    print("Account is not active")

print()
print("########################################################################")
print()

# and example
pin_correct = True
balance = 5000
amount = 3000

if pin_correct and amount <= balance:
    print("Transaction approved")
else:
    print("Transaction declined")

# or
payment_method = "transfer"

if payment_method == "cash" or payment_method == "transfer":
    print("Payment method accepted")
else:
    print("Unknown payment method")

# not
account_locked = False

if not account_locked:
    print("Account is open")
else:
    print("Account is locked")

print()
print("########################################################################")
print()

# Selecting an execution path
destination = "Abuja"

if destination == "Lagos":
    print("Send to local van")
elif destination == "Abuja":
    print("Send to interstate truck")
elif destination == "Accra":
    print("Send to international courier")
else:
    print("Route not found")


# Pos analogy
card_valid = True
pin_correct = False
amount = 4000
balance = 15000

if not card_valid:
    print("Card rejected")
elif not pin_correct:
    print("Incorrect PIN")
elif amount > balance:
    print("Insufficient balance")
else:
    print("Transaction successful")
