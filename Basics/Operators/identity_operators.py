"""
Demonstrates Python identity operators.

Identity operators check whether two variables refer
to the same object in memory.

Operators:
- is
- is not
"""

# --------------------------------------------------
# 1. Equality vs Identity
# --------------------------------------------------

list_a = ["Python", "Java"]
list_b = ["Python", "Java"]

print("Equality Check:")
print("list_a == list_b:", list_a == list_b)

print("\nIdentity Check:")
print("list_a is list_b:", list_a is list_b)


# --------------------------------------------------
# 2. Same Object Reference
# --------------------------------------------------

list_c = list_a

print("\nSame Object Reference:")
print("list_a == list_c:", list_a == list_c)
print("list_a is list_c:", list_a is list_c)


# --------------------------------------------------
# 3. Identity with None
# --------------------------------------------------

delivery_date = None

print("\nNone Identity Check:")
print("delivery_date is None:", delivery_date is None)
print("delivery_date is not None:", delivery_date is not None)