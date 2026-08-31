
"""
Demonstrates basic user input in Python.

The input() function is used to receive information
from the user.
"""

# --------------------------------------------------
# 1. Basic Input
# --------------------------------------------------

movie_name = input("Enter movie name: ")

print("\nMovie Name:", movie_name)


# --------------------------------------------------
# 2. Multiple Inputs
# --------------------------------------------------

customer_name = input("Enter customer name: ")
city = input("Enter city: ")

print("\nBooking Details:")
print("Customer:", customer_name)
print("City:", city)


# --------------------------------------------------
# 3. Input Returns a String
# --------------------------------------------------

ticket_count = input("Enter number of tickets: ")

print("\nTicket Count:", ticket_count)
print("Type:", type(ticket_count))


# --------------------------------------------------
# 4. Converting Input to Integer
# --------------------------------------------------

ticket_count = int(input("Enter number of tickets: "))

print("\nTicket Count:", ticket_count)
print("Type:", type(ticket_count))