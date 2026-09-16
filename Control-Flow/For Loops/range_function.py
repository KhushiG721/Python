"""
The range() function with for loops.

This example demonstrates the different ways
range() can generate a sequence of numbers.
"""

# range(stop)
print("Numbers from 0 to 4:")

for number in range(5):
    print(number)

# range(start, stop)
print("\nNumbers from 1 to 5:")

for number in range(1, 6):
    print(number)

# range(start, stop, step)
print("\nEven numbers from 2 to 10:")

for number in range(2, 11, 2):
    print(number)

# Negative step
print("\nCountdown:")

for number in range(5, 0, -1):
    print(number)