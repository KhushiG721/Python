"""
Demonstrates Python arithmetic operators.

Arithmetic operators are used to perform mathematical
calculations on numeric values.
"""

# --------------------------------------------------
# 1. Addition
# --------------------------------------------------

price = 500
delivery_charge = 50

total = price + delivery_charge

print("Addition:")
print("Total:", total)


# --------------------------------------------------
# 2. Subtraction
# --------------------------------------------------

amount_paid = 1000
purchase_amount = 750

balance = amount_paid - purchase_amount

print("\nSubtraction:")
print("Balance:", balance)


# --------------------------------------------------
# 3. Multiplication
# --------------------------------------------------

price_per_item = 250
quantity = 4

total_price = price_per_item * quantity

print("\nMultiplication:")
print("Total Price:", total_price)


# --------------------------------------------------
# 4. Division
# --------------------------------------------------

total_amount = 1000
number_of_people = 4

amount_per_person = total_amount / number_of_people

print("\nDivision:")
print("Amount per Person:", amount_per_person)


# --------------------------------------------------
# 5. Floor Division
# --------------------------------------------------

total_items = 17
boxes = 5

items_per_box = total_items // boxes

print("\nFloor Division:")
print("Items per Box:", items_per_box)


# --------------------------------------------------
# 6. Modulus
# --------------------------------------------------

remaining_items = total_items % boxes

print("\nModulus:")
print("Remaining Items:", remaining_items)


# --------------------------------------------------
# 7. Exponentiation
# --------------------------------------------------

base = 2
power = 3

result = base ** power

print("\nExponentiation:")
print("Result:", result)