"""
Basic while loop in Python.

This example demonstrates how a while loop repeatedly
executes a block of code while a condition is True.
"""

# Number of items to process
remaining_items = 3

# Process items until none remain
while remaining_items > 0:
    print(f"Processing item {remaining_items}")
    remaining_items -= 1

print("All items processed.")