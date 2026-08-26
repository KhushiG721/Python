"""
Demonstrates Python sets.

Sets are mutable collections of unique elements.
They are useful for removing duplicates, checking
membership, and performing mathematical set operations.
"""

# --------------------------------------------------
# 1. Creating a Set
# --------------------------------------------------

registered_users = {"Alice", "Bob", "Charlie", "Alice"}

print("Registered Users:", registered_users)
print("Type:", type(registered_users))


# --------------------------------------------------
# 2. Duplicate Values
# --------------------------------------------------

print("\nUnique Users:")
print("Number of Unique Users:", len(registered_users))


# --------------------------------------------------
# 3. Adding an Element
# --------------------------------------------------

registered_users.add("David")

print("\nAfter Adding David:")
print(registered_users)


# --------------------------------------------------
# 4. Removing an Element
# --------------------------------------------------

registered_users.remove("Bob")

print("\nAfter Removing Bob:")
print(registered_users)


# --------------------------------------------------
# 5. Checking Membership
# --------------------------------------------------

print("\nMembership Check:")
print("Is Alice registered?", "Alice" in registered_users)
print("Is Bob registered?", "Bob" in registered_users)


# --------------------------------------------------
# 6. Set Union
# --------------------------------------------------

morning_session = {"Alice", "Charlie", "David"}
evening_session = {"Charlie", "David", "Emma"}

all_attendees = morning_session | evening_session

print("\nUnion:")
print("All Attendees:", all_attendees)


# --------------------------------------------------
# 7. Set Intersection
# --------------------------------------------------

common_attendees = morning_session & evening_session

print("\nIntersection:")
print("Attending Both Sessions:", common_attendees)


# --------------------------------------------------
# 8. Set Difference
# --------------------------------------------------

morning_only = morning_session - evening_session

print("\nDifference:")
print("Morning Session Only:", morning_only)


# --------------------------------------------------
# 9. Symmetric Difference
# --------------------------------------------------

one_session_only = morning_session ^ evening_session

print("\nSymmetric Difference:")
print("Attending Only One Session:", one_session_only)


# --------------------------------------------------
# 10. Adding Multiple Elements
# --------------------------------------------------

registered_users.update({"Emma", "Frank", "Grace"})

print("\nAfter Adding Multiple Users:")
print(registered_users)