"""
Nested while loops in Python.

This example demonstrates nested iteration
using two while loops.
"""

row = 1

while row <= 3:
    column = 1

    while column <= 3:
        print(f"Row: {row}, Column: {column}")
        column += 1

    print()
    row += 1