# Definite iteration
customers = ["Amaka", "Tunde", "Fatima"]

for customer in customers:
    print("Serving", customer)

# Indefinite iteration
count = 5

while count > 0:
    print("Countdown:", count)
    count = count - 1


balance = 1000
withdrawal = 300

while balance >= withdrawal:
    balance = balance - withdrawal
    print(f"Withdrew {withdrawal}, new balance: {balance}")

# For loop
for amount in [100, 250, 75, 400]:
    print("Transaction: ", amount)

print()
print("########################################################################")
print()

transactions = [500, 1200, 300, 800]
total = 0

for amount in transactions:
    total = total + amount

print("Total: ", total)

print()
print("########################################################################")
print()

# for + range()
for i in range(5):
    print("Processing step", i)

# st