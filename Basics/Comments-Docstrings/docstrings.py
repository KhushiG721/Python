"""
Demonstrates module, function, and class docstrings.
"""


def calculate_total(price, quantity):
    """
    Calculate the total cost of a product.

    Args:
        price: Price of one item.
        quantity: Number of items.

    Returns:
        Total cost of the items.
    """
    return price * quantity


print(calculate_total(250, 3))