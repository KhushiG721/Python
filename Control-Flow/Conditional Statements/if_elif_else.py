"""
if-elif-else statement in Python.

This example demonstrates how multiple conditions
can be checked in sequence.
"""

# Customer's purchase amount
purchase_amount = 3200

# Determine the discount based on the purchase amount
if purchase_amount >= 5000:
    discount = 20
elif purchase_amount >= 3000:
    discount = 15
elif purchase_amount >= 1000:
    discount = 10
else:
    discount = 0

print(f"Purchase amount: ₹{purchase_amount}")
print(f"Discount: {discount}%")