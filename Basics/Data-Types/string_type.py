"""
Demonstrates Python strings.

Strings are sequences of characters enclosed in quotes.
They are commonly used to store and manipulate text.
"""

# --------------------------------------------------
# 1. Creating a String
# --------------------------------------------------

customer_name = "Alex"
message = "Your order has been shipped."

print("Customer Name:", customer_name)
print("Message:", message)
print("Type:", type(customer_name))


# --------------------------------------------------
# 2. String Length
# --------------------------------------------------

print("\nString Length:")
print("Number of characters:", len(message))


# --------------------------------------------------
# 3. String Indexing
# --------------------------------------------------

print("\nString Indexing:")
print("First character:", message[0])
print("Last character:", message[-1])


# --------------------------------------------------
# 4. String Slicing
# --------------------------------------------------

print("\nString Slicing:")
print("First five characters:", message[:5])
print("Last seven characters:", message[-7:])


# --------------------------------------------------
# 5. String Concatenation
# --------------------------------------------------

first_name = "Alex"
last_name = "Morgan"

full_name = first_name + " " + last_name

print("\nString Concatenation:")
print("Full Name:", full_name)


# --------------------------------------------------
# 6. Formatted Strings
# --------------------------------------------------

order_id = 1045
status = "Shipped"

order_message = f"Order #{order_id} is {status}."

print("\nFormatted String:")
print(order_message)


# --------------------------------------------------
# 7. Common String Methods
# --------------------------------------------------

text = "  Python Programming  "

print("\nString Methods:")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Stripped:", text.strip())
print("Replaced:", text.replace("Python", "Java"))


# --------------------------------------------------
# 8. Searching Within a String
# --------------------------------------------------

message = "Your order has been shipped."

print("\nSearching:")
print("Contains 'order':", "order" in message)
print("Contains 'cancelled':", "cancelled" in message)


# --------------------------------------------------
# 9. Splitting a String
# --------------------------------------------------

product_details = "Laptop,Electronics,79999"

details = product_details.split(",")

print("\nSplitting:")
print("Product Details:", details)


# --------------------------------------------------
# 10. Practical Example
# --------------------------------------------------

product_name = "Wireless Headphones"
quantity = 2

summary = f"You purchased {quantity} units of {product_name}."

print("\nOrder Summary:")
print(summary)