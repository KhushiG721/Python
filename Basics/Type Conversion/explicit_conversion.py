"""
Demonstrates explicit type conversion in Python.

Explicit conversion is performed manually using
built-in conversion functions.
"""

# String to integer
age_text = "25"
age = int(age_text)

print("Age:", age)
print("Type:", type(age))


# Integer to float
quantity = 5
quantity_decimal = float(quantity)

print("\nQuantity:", quantity_decimal)
print("Type:", type(quantity_decimal))


# Number to string
order_id = 1025
order_text = str(order_id)

print("\nOrder ID:", order_text)
print("Type:", type(order_text))


# Integer to Boolean
available_count = 1
is_available = bool(available_count)

print("\nAvailable:", is_available)
print("Type:", type(is_available))