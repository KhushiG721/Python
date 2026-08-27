"""
Demonstrates Python's None value.

None represents the absence of a value.
It is commonly used when a value is not available,
has not been assigned yet, or intentionally represents
"no value".
"""

# --------------------------------------------------
# 1. Assigning None
# --------------------------------------------------

booking_reference = None

print("Booking Reference:", booking_reference)
print("Type:", type(booking_reference))


# --------------------------------------------------
# 2. Checking for None
# --------------------------------------------------

if booking_reference is None:
    print("\nBooking reference is not available yet.")
else:
    print("\nBooking Reference:", booking_reference)


# --------------------------------------------------
# 3. Assigning a Value Later
# --------------------------------------------------

booking_reference = "HTL20260827"

print("\nUpdated Booking Reference:", booking_reference)


# --------------------------------------------------
# 4. None as an Optional Value
# --------------------------------------------------

special_request = None

if special_request is None:
    print("\nNo special request was added.")
else:
    print("\nSpecial Request:", special_request)


# --------------------------------------------------
# 5. Function Returning None
# --------------------------------------------------

def confirm_booking():
    print("\nBooking confirmed.")


result = confirm_booking()

print("Function Return Value:", result)
print("Return Type:", type(result))


# --------------------------------------------------
# 6. None vs Other Values
# --------------------------------------------------

value1 = None
value2 = 0
value3 = ""
value4 = False

print("\nDifferent Values:")
print("None:", value1)
print("Zero:", value2)
print("Empty String:", value3)
print("False:", value4)


# --------------------------------------------------
# 7. Checking None with is
# --------------------------------------------------

guest_note = None

print("\nNone Check:")

if guest_note is None:
    print("No guest note is available.")