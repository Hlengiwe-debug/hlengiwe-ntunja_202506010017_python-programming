from food_order import calculate_total

def main():
    # Get price (keep asking if invalid)
    while True:
        try:
            price = float(input("Price (RM): "))
            break
        except ValueError:
            print("Invalid price. Please enter a number.")

    # Get quantity (keep asking if invalid)
    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except ValueError:
            print("Invalid quantity. Please enter an integer.")

    # Calculate (may return an error string)
    total = calculate_total(price, quantity)

    # Show result or error
    if isinstance(total, str):
        print(total)
    else:
        print(f"Total Payment = RM {total:.2f}")

if __name__ == "__main__":
    main()