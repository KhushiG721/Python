"""
Demonstrates implicit type conversion in Python.

Python automatically converts a value to a compatible
type when required during certain operations.
"""

# Integer and float
items = 4
price = 125.50

total = items * price

print("Items:", items)
print("Price:", price)
print("Total:", total)
print("Type of total:", type(total))


# Integer and float addition
whole_number = 10
decimal_number = 5.5

result = whole_number + decimal_number

print("\nResult:", result)
print("Type of result:", type(result))