"""
Iterating through collections using for loops.

This example demonstrates how for loops can be used
with lists, tuples, sets, and dictionaries.
"""

# List
products = ["Laptop", "Mouse", "Keyboard"]

print("Products:")

for product in products:
    print(product)


# Tuple
colors = ("Red", "Green", "Blue")

print("\nColors:")

for color in colors:
    print(color)


# Set
categories = {"Books", "Music", "Movies"}

print("\nCategories:")

for category in categories:
    print(category)


# Dictionary
product = {
    "name": "Laptop",
    "price": 75000,
    "stock": 10
}

print("\nProduct details:")

for key, value in product.items():
    print(f"{key}: {value}")