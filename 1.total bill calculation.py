items = [
    {"name": "Apple", "price": 10, "quantity": 5},
    {"name": "Banana", "price": 5, "quantity": 10},
    {"name": "Milk", "price": 25, "quantity": 2}
]

total_cost = 0
for item in items:
    total_cost += item["price"] * item["quantity"]

print("Total Bill Amount:", total_cost)
