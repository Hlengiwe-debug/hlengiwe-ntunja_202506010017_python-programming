"""
main.py – Main entry point for the café billing system.
"""

from utils import calculate_total, print_receipt


def get_positive_int(prompt: str) -> int:
    """
    Helper function to get a non-negative integer from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Quantity cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main() -> None:
    """Run the café billing program."""
    print("Welcome to the Cafe Billing System\n")

    customer = input("Enter customer name: ").strip()
    if not customer:
        customer = "Unknown"  # fallback

    coffee = get_positive_int("Enter number of coffee: ")
    tea = get_positive_int("Enter number of tea: ")
    sandwich = get_positive_int("Enter number of sandwich: ")

    total = calculate_total(coffee, tea, sandwich)

    print("\n")  # spacing
    print_receipt(customer, coffee, tea, sandwich, total)


if __name__ == "__main__":
    main()