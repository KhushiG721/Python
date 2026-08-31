"""
Demonstrates formatted output using f-strings.
"""

# --------------------------------------------------
# 1. Basic f-string
# --------------------------------------------------

product = "Laptop"
price = 54999

print(f"Product: {product}")
print(f"Price: ₹{price}")


# --------------------------------------------------
# 2. Multiple Variables
# --------------------------------------------------

customer = "Alex"
quantity = 2

print(f"{customer} purchased {quantity} units.")


# --------------------------------------------------
# 3. Calculated Values
# --------------------------------------------------

price_per_item = 750
quantity = 3

total_price = price_per_item * quantity

print(f"Price per item: ₹{price_per_item}")
print(f"Quantity: {quantity}")
print(f"Total price: ₹{total_price}")


# --------------------------------------------------
# 4. Floating-Point Formatting
# --------------------------------------------------

amount = 1250.5678

print(f"\nAmount: ₹{amount:.2f}")


# --------------------------------------------------
# 5. Practical Output
# --------------------------------------------------

item = "Wireless Headphones"
price = 2499.99
quantity = 2

total = price * quantity

print("\n--- Order Summary ---")
print(f"Item     : {item}")
print(f"Price    : ₹{price:.2f}")
print(f"Quantity : {quantity}")
print(f"Total    : ₹{total:.2f}")