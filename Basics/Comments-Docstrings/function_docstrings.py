"""
Demonstrates documenting functions using docstrings.
"""


def calculate_discount(price, discount_percentage):
    """
    Calculate the discounted price.

    Args:
        price: Original price of the product.
        discount_percentage: Discount percentage to apply.

    Returns:
        Price after applying the discount.
    """
    discount = price * discount_percentage / 100
    return price - discount


def format_order_summary(product_name, quantity, total_price):
    """
    Create a formatted order summary.

    Args:
        product_name: Name of the product.
        quantity: Number of items ordered.
        total_price: Total price of the order.

    Returns:
        A formatted order summary string.
    """
    return (
        f"Product: {product_name}\n"
        f"Quantity: {quantity}\n"
        f"Total: ₹{total_price:.2f}"
    )


price = 1000
discount_percentage = 10
quantity = 2

discounted_price = calculate_discount(
    price,
    discount_percentage
)

total_price = discounted_price * quantity

print(format_order_summary(
    "Backpack",
    quantity,
    total_price
))