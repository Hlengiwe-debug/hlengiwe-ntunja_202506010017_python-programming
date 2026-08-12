def check_computers():
    """Check the status of all computers in the lab."""
    computers = []  # initial value
    num_computers = 5  # Number of computers to check
    
    print("\n--- COMPUTER STATUS CHECK ---")
    print("Enter status for each computer:")
    print("  A - Available")
    print("  U - Used") 
    print("  M - Maintenance\n")
    
    # iterate & check for 5 computer
    for i in range(num_computers):
        while True:
            status = input(f"Computer #{i+1} status (A/U/M): ").strip().upper()
            if status in ['A', 'U', 'M']:
                break
            print("Invalid! Please enter A, U, or M.")
        
        # prompt the user to classify each computer to either
        # A - Available, U - Used, M - Maintenance
        computers.append(status)
    
    return computers


def count_available(computers):
    """Count how many computers are available."""
    available = 0  # initial value
    
    for computer in computers:  # for ______ in ______:
        if computer == "A":     # if ______ == "A":
            available += 1
    
    return available