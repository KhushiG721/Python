"""
Demonstrates basic input validation.

User input is validated before being processed.
"""

# --------------------------------------------------
# 1. Age Validation
# --------------------------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("Age verification successful.")
else:
    print("Age requirement not met.")


# --------------------------------------------------
# 2. Positive Number Validation
# --------------------------------------------------

quantity = int(input("\nEnter quantity: "))

if quantity > 0:
    print("Valid quantity.")
else:
    print("Quantity must be greater than zero.")


# --------------------------------------------------
# 3. Simple Choice Validation
# --------------------------------------------------

choice = input("\nDo you want to continue? (yes/no): ")

if choice.lower() == "yes":
    print("Continuing...")
elif choice.lower() == "no":
    print("Exiting...")
else:
    print("Invalid choice.")