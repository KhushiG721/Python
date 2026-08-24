"""
Demonstrates Python tuples.

Tuples are ordered and immutable collections.
They are useful for storing a fixed group of related values.
"""

# --------------------------------------------------
# 1. Creating a Tuple
# --------------------------------------------------

rgb_color = (255, 128, 0)

print("RGB Color:", rgb_color)
print("Type:", type(rgb_color))


# --------------------------------------------------
# 2. Accessing Elements
# --------------------------------------------------

print("\nAccessing Elements:")
print("Red:", rgb_color[0])
print("Green:", rgb_color[1])
print("Blue:", rgb_color[2])


# --------------------------------------------------
# 3. Negative Indexing
# --------------------------------------------------

print("\nNegative Indexing:")
print("Last Value:", rgb_color[-1])
print("Second Last Value:", rgb_color[-2])


# --------------------------------------------------
# 4. Tuple Length
# --------------------------------------------------

print("\nTuple Length:")
print("Number of Values:", len(rgb_color))


# --------------------------------------------------
# 5. Tuple Slicing
# --------------------------------------------------

print("\nTuple Slicing:")
print("First Two Values:", rgb_color[:2])
print("Last Two Values:", rgb_color[-2:])


# --------------------------------------------------
# 6. Checking Membership
# --------------------------------------------------

print("\nMembership Check:")
print("Is 255 present?", 255 in rgb_color)
print("Is 100 present?", 100 in rgb_color)


# --------------------------------------------------
# 7. Tuple Unpacking
# --------------------------------------------------

red, green, blue = rgb_color

print("\nTuple Unpacking:")
print("Red:", red)
print("Green:", green)
print("Blue:", blue)


# --------------------------------------------------
# 8. Counting Values
# --------------------------------------------------

color_values = (255, 128, 255, 64, 255)

print("\nCounting Values:")
print("Number of times 255 appears:", color_values.count(255))


# --------------------------------------------------
# 9. Finding the Position of a Value
# --------------------------------------------------

print("\nFinding Position:")
print("Position of 128:", color_values.index(128))


# --------------------------------------------------
# 10. Immutability
# --------------------------------------------------

# Tuples cannot be modified after creation.
# Uncommenting the following line will raise a TypeError:

# rgb_color[0] = 100