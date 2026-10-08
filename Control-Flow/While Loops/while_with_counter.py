"""
While loop with a counter.

This example demonstrates counting iterations
and calculating a running total.
"""

# Initialize variables
counter = 1
total = 0

# Calculate the sum of numbers from 1 to 5
while counter <= 5:
    total += counter
    print(f"Number: {counter}, Running total: {total}")
    counter += 1

print(f"Final total: {total}")