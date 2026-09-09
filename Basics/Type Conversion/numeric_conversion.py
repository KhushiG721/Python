"""
Demonstrates conversion between numeric data types.
"""

# Integer
number = 25

# Integer to float
decimal_number = float(number)

# Integer to complex
complex_number = complex(number)

print("Original value:", number)
print("Original type:", type(number))

print("\nFloat value:", decimal_number)
print("Float type:", type(decimal_number))

print("\nComplex value:", complex_number)
print("Complex type:", type(complex_number))


# Float to integer
price = 99.75
whole_price = int(price)

print("\nOriginal price:", price)
print("Converted price:", whole_price)