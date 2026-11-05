"""
Nested for loops in Python.

This example demonstrates how an inner loop
executes completely for each outer-loop iteration.
"""

for row in range(1, 4):
    for column in range(1, 4):
        print(f"Row: {row}, Column: {column}")

    print("End of row\n")