"""
Multiplication tables using nested for loops.

This example generates multiplication tables
for numbers from 1 to 5.
"""

for number in range(1, 6):
    print(f"Multiplication table of {number}")

    for multiplier in range(1, 11):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")

    print()