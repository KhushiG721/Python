"""
Nested if statements in Python.

This example demonstrates how one condition can be
checked only after another condition is satisfied.
"""

# Event access information
age = 21
has_ticket = True

# First check the age requirement
if age >= 18:

    # Check ticket availability only if the age requirement is met
    if has_ticket:
        print("Entry allowed.")
    else:
        print("A valid ticket is required.")

else:
    print("Entry is restricted to adults.")