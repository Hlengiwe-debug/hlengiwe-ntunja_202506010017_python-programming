"""
utils.py – Business logic for the café billing system.
"""

# Constants for item prices
COFFEE_PRICE = 8.50
TEA_PRICE = 6.00
SANDWICH_PRICE = 12.00


def calculate_total(coffee: int, tea: int, sandwich: int) -> float:
    """
    Calculate the total bill for the given quantities.

    Args:
        coffee (int): Number of coffees.
        tea (int): Number of teas.
        sandwich (int): Number of sandwiches.

    Returns:
        float: Total amount in RM.
    """
    return (coffee * COFFEE_PRICE +
            tea * TEA_PRICE +
            sandwich * SANDWICH_PRICE)


def print_receipt(customer: str, coffee: int, tea: int, sandwich: int, total: float) -> None:
    """
    Print a formatted receipt.

    Args:
        customer (str): Customer name.
        coffee (int): Number of coffees.
        tea (int): Number of teas.
        sandwich (int): Number of sandwiches.
        total (float): Total bill amount.
    """
    print("======== RECEIPT ========")
    print(f"Customer: {customer}")
    print(f"Coffee: {coffee}")
    print(f"Tea: {tea}")
    print(f"Sandwich: {sandwich}")
    print(f"Total = RM {total:.2f}")