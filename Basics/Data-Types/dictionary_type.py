"""
Demonstrates Python dictionaries.

Dictionaries store data as key-value pairs.
Each key must be unique and is used to access
its corresponding value.
"""

# --------------------------------------------------
# 1. Creating a Dictionary
# --------------------------------------------------

book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "year": 1988,
    "available": True
}

print("Book:", book)
print("Type:", type(book))


# --------------------------------------------------
# 2. Accessing Values
# --------------------------------------------------

print("\nAccessing Values:")
print("Title:", book["title"])
print("Author:", book["author"])
print("Available:", book["available"])


# --------------------------------------------------
# 3. Accessing a Value Using get()
# --------------------------------------------------

print("\nUsing get():")
print("Publication Year:", book.get("year"))
print("Publisher:", book.get("publisher"))


# --------------------------------------------------
# 4. Adding a New Key-Value Pair
# --------------------------------------------------

book["category"] = "Fiction"

print("\nAfter Adding Category:")
print(book)


# --------------------------------------------------
# 5. Updating an Existing Value
# --------------------------------------------------

book["available"] = False

print("\nAfter Updating Availability:")
print(book)


# --------------------------------------------------
# 6. Checking Whether a Key Exists
# --------------------------------------------------

print("\nKey Checking:")
print("Is 'author' present?", "author" in book)
print("Is 'price' present?", "price" in book)


# --------------------------------------------------
# 7. Getting All Keys
# --------------------------------------------------

print("\nKeys:")
print(book.keys())


# --------------------------------------------------
# 8. Getting All Values
# --------------------------------------------------

print("\nValues:")
print(book.values())


# --------------------------------------------------
# 9. Getting Key-Value Pairs
# --------------------------------------------------

print("\nKey-Value Pairs:")

for key, value in book.items():
    print(key, ":", value)


# --------------------------------------------------
# 10. Removing a Key-Value Pair
# --------------------------------------------------

removed_value = book.pop("category")

print("\nAfter Removing Category:")
print(book)
print("Removed Value:", removed_value)


# --------------------------------------------------
# 11. Dictionary Length
# --------------------------------------------------

print("\nNumber of Entries:", len(book))