"""
Break statement in Python.

This example demonstrates how break terminates
a loop when a specified condition is satisfied.
"""

# Available products
products = ["Mouse", "Keyboard", "Monitor", "Laptop"]

# Product to search for
target_product = "Monitor"

for product in products:
    print(f"Checking: {product}")

    if product == target_product:
        print(f"{target_product} found!")
        break

print("Search completed.")