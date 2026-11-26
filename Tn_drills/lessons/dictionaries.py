inventory = {"cups": 100, "lids": 150}
print(type(inventory))

menu = {
    "Latte": 4.50,
    "Espresso": 3.50
}

# Look up Espresso price
espresso_price = menu["Espresso"]
print(espresso_price, "USD")

stock = {
    "cups": 100,
    "lids": 150
}

print(stock["cups"])

kiosk = {"status": "OFF"}
kiosk["status"] = "ON" # Updating exisiting dictionary
kiosk["operator"] = "Robot" # Add new dicitonary to the existing one
print(kiosk)

menu = {"Latte": 3.40}
print(menu.get("Chai"))
print(menu.get("Chai", 3.00))
print(menu.get("Latte"))