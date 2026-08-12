import computer_utils
import display_utils

def main():
    """Main program with loop to continue monitoring."""
    print("===== COMPUTER LAB MONITORING SYSTEM =====")
    print("Welcome to the Lab Monitoring System!\n")
    
    # Add a loop to prompt the user to either continue monitoring or not
    while True:
        # Check all computers
        computers = computer_utils.check_computers()
        
        # Count available
        available = computer_utils.count_available(computers)
        
        # Display status
        display_utils.display_status(computers, available)
        
        # Ask to continue
        choice = input("\nPerform another monitoring cycle? (Y/N): ").strip().upper()
        
        if choice != 'Y':
            print("\nExiting Lab Monitoring System. Goodbye!")
            break

if __name__ == "__main__":
    main()