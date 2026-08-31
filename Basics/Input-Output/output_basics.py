"""
Demonstrates Python output using print().
"""

# --------------------------------------------------
# 1. Basic Output
# --------------------------------------------------

print("Welcome to the Movie Booking System")


# --------------------------------------------------
# 2. Printing Multiple Values
# --------------------------------------------------

movie = "Inception"
tickets = 2

print("Movie:", movie, "Tickets:", tickets)


# --------------------------------------------------
# 3. Using sep
# --------------------------------------------------

date = "2026-08-31"
time = "7:30 PM"

print(date, time, sep=" | ")


# --------------------------------------------------
# 4. Using end
# --------------------------------------------------

print("Booking", end=" ")
print("confirmed.")


# --------------------------------------------------
# 5. Printing Different Data Types
# --------------------------------------------------

movie_price = 350.50
number_of_tickets = 2
booking_confirmed = True

print("\nMovie Price:", movie_price)
print("Number of Tickets:", number_of_tickets)
print("Booking Confirmed:", booking_confirmed)