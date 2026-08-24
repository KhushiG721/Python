"""
Demonstrates Python lists.

Lists are ordered and mutable collections.
They can store multiple values and can contain
duplicate elements.
"""

# --------------------------------------------------
# 1. Creating a List
# --------------------------------------------------

watchlist = ["Inception", "Interstellar", "The Matrix"]

print("Watchlist:", watchlist)
print("Type:", type(watchlist))


# --------------------------------------------------
# 2. Accessing Elements
# --------------------------------------------------

print("\nAccessing Elements:")
print("First Movie:", watchlist[0])
print("Last Movie:", watchlist[-1])


# --------------------------------------------------
# 3. List Length
# --------------------------------------------------

print("\nList Length:")
print("Number of Movies:", len(watchlist))


# --------------------------------------------------
# 4. Adding an Element
# --------------------------------------------------

watchlist.append("The Dark Knight")

print("\nAfter Adding a Movie:")
print(watchlist)


# --------------------------------------------------
# 5. Inserting an Element
# --------------------------------------------------

watchlist.insert(1, "Avatar")

print("\nAfter Inserting a Movie:")
print(watchlist)


# --------------------------------------------------
# 6. Updating an Element
# --------------------------------------------------

watchlist[2] = "Dune"

print("\nAfter Updating a Movie:")
print(watchlist)


# --------------------------------------------------
# 7. Removing an Element
# --------------------------------------------------

watchlist.remove("Avatar")

print("\nAfter Removing a Movie:")
print(watchlist)


# --------------------------------------------------
# 8. Removing an Element by Position
# --------------------------------------------------

removed_movie = watchlist.pop(1)

print("\nAfter Using pop():")
print("Removed Movie:", removed_movie)
print("Updated Watchlist:", watchlist)


# --------------------------------------------------
# 9. List Slicing
# --------------------------------------------------

movies = ["Inception", "Dune", "Avatar", "Titanic", "Gladiator"]

print("\nList Slicing:")
print("First Three Movies:", movies[:3])
print("Last Two Movies:", movies[-2:])


# --------------------------------------------------
# 10. Checking Membership
# --------------------------------------------------

print("\nMembership Check:")
print("Is 'Dune' in the list?", "Dune" in movies)
print("Is 'Joker' in the list?", "Joker" in movies)


# --------------------------------------------------
# 11. Lists Allow Duplicate Values
# --------------------------------------------------

ratings = [5, 4, 5, 3, 5]

print("\nDuplicate Values:")
print("Ratings:", ratings)
print("Number of 5-star ratings:", ratings.count(5))