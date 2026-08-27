"""
Demonstrates type checking in Python.

Python provides built-in functions for inspecting
and checking the data type of values.

Functions covered:
- type()
- isinstance()
"""

# --------------------------------------------------
# 1. Using type()
# --------------------------------------------------

product_name = "Wireless Keyboard"
price = 1299.50
quantity = 2
is_available = True

print("Using type():")
print("Product Name:", type(product_name))
print("Price:", type(price))
print("Quantity:", type(quantity))
print("Available:", type(is_available))


# --------------------------------------------------
# 2. Using isinstance()
# --------------------------------------------------

print("\nUsing isinstance():")

print("Is product name a string?",
      isinstance(product_name, str))

print("Is price a float?",
      isinstance(price, float))

print("Is quantity an integer?",
      isinstance(quantity, int))

print("Is product available a Boolean?",
      isinstance(is_available, bool))


# --------------------------------------------------
# 3. Checking Multiple Possible Types
# --------------------------------------------------

product_code = 101

is_valid_code = isinstance(product_code, (int, str))

print("\nMultiple Type Checking:")
print("Is product code an integer or string?", is_valid_code)


# --------------------------------------------------
# 4. Practical Type Validation
# --------------------------------------------------

customer_quantity = 5

print("\nQuantity Validation:")

if isinstance(customer_quantity, int):
    print("Quantity is valid.")
else:
    print("Quantity must be an integer.")


# --------------------------------------------------
# 5. Type Checking Before an Operation
# --------------------------------------------------

discount = "10"

print("\nDiscount Validation:")

if isinstance(discount, (int, float)):
    final_discount = discount / 100
    print("Discount:", final_discount)
else:
    print("Discount must be a number.")


# --------------------------------------------------
# 6. Checking None
# --------------------------------------------------

delivery_date = None

print("\nNone Checking:")

if delivery_date is None:
    print("Delivery date is not available.")
else:
    print("Delivery date:", delivery_date)