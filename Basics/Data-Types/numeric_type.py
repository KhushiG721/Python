"""
Demonstrates Python's built-in numeric data types.

Numeric types covered:
- int
- float
- complex
"""

# --------------------------------------------------
# 1. Integer (int)
# --------------------------------------------------

number_of_items = 4

print("Number of items:", number_of_items)
print("Type:", type(number_of_items))


# --------------------------------------------------
# 2. Floating-point Number (float)
# --------------------------------------------------

item_price = 149.50

print("\nItem Price:", item_price)
print("Type:", type(item_price))


# --------------------------------------------------
# 3. Complex Number (complex)
# --------------------------------------------------

signal_value = 3 + 4j

print("\nComplex Value:", signal_value)
print("Type:", type(signal_value))


# --------------------------------------------------
# 4. Arithmetic Operations
# --------------------------------------------------

price = 250
quantity = 3

total_price = price * quantity

print("\nArithmetic Operations:")
print("Price:", price)
print("Quantity:", quantity)
print("Total Price:", total_price)


# --------------------------------------------------
# 5. Division
# --------------------------------------------------

total_amount = 500
number_of_people = 4

amount_per_person = total_amount / number_of_people

print("\nDivision:")
print("Total Amount:", total_amount)
print("Number of People:", number_of_people)
print("Amount per Person:", amount_per_person)


# --------------------------------------------------
# 6. Floor Division
# --------------------------------------------------

total_items = 17
boxes = 5

items_per_box = total_items // boxes

print("\nFloor Division:")
print("Items:", total_items)
print("Boxes:", boxes)
print("Items per Box:", items_per_box)


# --------------------------------------------------
# 7. Modulus
# --------------------------------------------------

remaining_items = total_items % boxes

print("\nModulus:")
print("Remaining Items:", remaining_items)


# --------------------------------------------------
# 8. Exponentiation
# --------------------------------------------------

base = 2
power = 3

result = base ** power

print("\nExponentiation:")
print("Base:", base)
print("Power:", power)
print("Result:", result)