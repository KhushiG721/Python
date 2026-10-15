"""
Pass statement in Python.

This example demonstrates how pass acts as a placeholder
without changing the normal flow of execution.
"""

# Example 1: pass inside a loop
for number in range(1, 4):
    if number == 2:
        pass

    print(f"Number: {number}")


# Example 2: pass in an unfinished function
def calculate_shipping():
    pass


print("Program completed.")