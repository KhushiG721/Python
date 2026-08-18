"""
Demonstrates Python's Boolean data type.

Boolean values represent one of two states:
- True
- False

Booleans are commonly used for comparisons,
conditions, validation, and decision-making.
"""

# --------------------------------------------------
# 1. Basic Boolean Values
# --------------------------------------------------

is_order_confirmed = True
is_payment_pending = False

print("Order Confirmed:", is_order_confirmed)
print("Payment Pending:", is_payment_pending)
print("Type:", type(is_order_confirmed))


# --------------------------------------------------
# 2. Boolean Values from Comparisons
# --------------------------------------------------

order_amount = 1500
minimum_order_amount = 500

is_order_eligible = order_amount >= minimum_order_amount

print("\nOrder Amount:", order_amount)
print("Minimum Order Amount:", minimum_order_amount)
print("Order Eligible:", is_order_eligible)


# --------------------------------------------------
# 3. Comparison Operators
# --------------------------------------------------

quantity = 3

print("\nComparison Results:")
print("Quantity > 0:", quantity > 0)
print("Quantity == 3:", quantity == 3)
print("Quantity < 2:", quantity < 2)
print("Quantity != 5:", quantity != 5)


# --------------------------------------------------
# 4. Logical AND
# --------------------------------------------------

has_stock = True
payment_completed = True

can_process_order = has_stock and payment_completed

print("\nAND Operation:")
print("Can Process Order:", can_process_order)


# --------------------------------------------------
# 5. Logical OR
# --------------------------------------------------

has_coupon = False
has_membership = True

gets_discount = has_coupon or has_membership

print("\nOR Operation:")
print("Gets Discount:", gets_discount)


# --------------------------------------------------
# 6. Logical NOT
# --------------------------------------------------

is_cancelled = False

print("\nNOT Operation:")
print("Is Cancelled:", is_cancelled)
print("Is Not Cancelled:", not is_cancelled)


# --------------------------------------------------
# 7. Boolean in a Conditional Statement
# --------------------------------------------------

payment_completed = True

print("\nPayment Status:")

if payment_completed:
    print("Payment successful.")
else:
    print("Payment failed.")


# --------------------------------------------------
# 8. Practical Example
# --------------------------------------------------

has_stock = True
payment_completed = True
delivery_address_available = True

can_place_order = (
    has_stock
    and payment_completed
    and delivery_address_available
)

print("\nOrder Validation:")
print("Can Place Order:", can_place_order)