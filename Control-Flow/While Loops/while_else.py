"""
While-else statement in Python.

This example demonstrates how the else block executes
after normal loop completion but is skipped after break.
"""

# Example 1: Normal loop completion
count = 1

print("Example 1: Normal completion")

while count <= 3:
    print(count)
    count += 1
else:
    print("Loop completed normally.")


# Example 2: Loop terminated using break
count = 1

print("\nExample 2: Loop terminated with break")

while count <= 5:
    if count == 3:
        print("Stopping the loop.")
        break

    print(count)
    count += 1
else:
    print("Loop completed normally.")