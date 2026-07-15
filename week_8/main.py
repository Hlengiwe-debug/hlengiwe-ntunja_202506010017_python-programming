import customer
import receipt

def main():
    # Get customer data
    name, food, quantity, price, delivery_charges = customer.get_customer()
    
    # Print receipt
    receipt.print_receipt(name, food, quantity, price, delivery_charges)

if __name__ == "__main__":
    main()