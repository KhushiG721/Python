"""
Demonstrates Python membership operators.

Membership operators check whether a value exists
inside a collection.
"""

products = ["Laptop", "Keyboard", "Mouse", "Monitor"]


# --------------------------------------------------
# 1. Using in
# --------------------------------------------------

print("Membership Checks:")

print("Is Laptop available?", "Laptop" in products)

print("Is Camera available?", "Camera" in products)


# --------------------------------------------------
# 2. Using not in
# --------------------------------------------------

print("\nNegative Membership Checks:")

print("Is Camera not available?", "Camera" not in products)

print("Is Mouse not available?", "Mouse" not in products)


# --------------------------------------------------
# 3. Membership in a String
# --------------------------------------------------

product_name = "Wireless Mouse"

print("\nString Membership:")

print("Is 'Mouse' present?", "Mouse" in product_name)
print("Is 'Keyboard' present?", "Keyboard" in product_name)