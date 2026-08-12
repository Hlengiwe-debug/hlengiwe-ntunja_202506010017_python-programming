def display_status(computers, available):
    """Display the lab status."""
    print("\n========== LAB STATUS ===========")
    
    for number in range(len(computers)):  # for number in range ______:
        print(f"Computer #{number + 1}: {computers[number]}")  # fill in the blanks
    
    print("-------------------------------")
    print(f"Available Computers: {available}")  # fill in the blank
    print("================================")