"""
Continue statement in Python.

This example demonstrates how continue skips
the current iteration and proceeds to the next one.
"""

# Product inventory
products = [
    {"name": "Mouse", "stock": 10},
    {"name": "Keyboard", "stock": 0},
    {"name": "Monitor", "stock": 5},
    {"name": "Laptop", "stock": 0},
]

for product in products:
    # Skip products that are out of stock
    if product["stock"] == 0:
        continue

    print(f"{product['name']} - Stock: {product['stock']}")

print("Inventory check completed.")