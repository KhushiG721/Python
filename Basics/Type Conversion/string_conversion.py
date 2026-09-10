"""
Demonstrates conversion of different data types into strings.
"""

# Integer to string
product_id = 501
product_id_text = str(product_id)

print("Product ID:", product_id_text)
print("Type:", type(product_id_text))


# Float to string
price = 299.50
price_text = str(price)

print("\nPrice:", price_text)
print("Type:", type(price_text))


# Boolean to string
is_available = True
availability_text = str(is_available)

print("\nAvailability:", availability_text)
print("Type:", type(availability_text))


# Combining converted values with strings
quantity = 3

message = "Quantity selected: " + str(quantity)

print("\n" + message)