"""
While loop with user input.

This example demonstrates how a sentinel value
can control the termination of a loop.
"""

# Initialize the command
command = ""

# Continue until the user enters "exit"
while command != "exit":
    command = input("Enter a command (or 'exit' to stop): ").strip().lower()

    if command == "exit":
        print("Exiting the program.")
    else:
        print(f"Command received: {command}")