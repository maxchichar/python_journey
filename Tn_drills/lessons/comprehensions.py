# Step 1: List Comprehensions (Transforming Lists)
prices = [3.00, 4.00, 5.00]
taxed_prices = [p * 1.10 for p in prices]
print(taxed_prices)

# Step 2: Filtering Inside List Comprehensions
volumes = [8, 12, 16, 20]
large_volumes = [v for v in volumes if v >= 16]
print(large_volumes)

# Step 3: Dictionary Comprehensions
stock = {"cups": 100, "lids": 150}
doubled_stock = {item: count * 2 for item, count in stock.items()}
print(doubled_stock)

# Step 4: Set Comprehensions
messy_names = ["LATTE", "latte", "espresso", "latte"]
unique_clean = {name.strip().lower() for name in messy_names}
print(unique_clean)

# Write a comprehension that converts a list of sizes: any "large" becomes "Premium", and any other size becomes "Regular".

items = [1, 2, 3, 11, 32, 82, 31, 16, 12, 13, 9, 10, 7, 4, 6, 5, 8, 15, 14]
diff_sizes = ["Premium" if size >= 15 else "Regular" for size in items]
print(diff_sizes)

# AI said better approach

# List of sizes as strings
items = ["small", "large", "medium", "large", "small", "large"]

# Map "large" -> "Premium", all other sizes -> "Regular"
diff_sizes = ["Premium" if size == "large" else "Regular" for size in items]

print(diff_sizes)