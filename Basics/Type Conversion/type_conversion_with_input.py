"""
Demonstrates type conversion when working with user input.
"""

# Input returns a string
quantity = input("Enter quantity: ")

print("\nBefore conversion:")
print("Value:", quantity)
print("Type:", type(quantity))


# Convert string to integer
quantity = int(quantity)

print("\nAfter conversion:")
print("Value:", quantity)
print("Type:", type(quantity))


# Another example
price = input("\nEnter product price: ")

price = float(price)

print("Price:", price)
print("Type:", type(price))


# Calculate total
total = quantity * price

print("\nTotal:", total)
print("Type:", type(total))