def check_access(registered, open_lab, comp_avail):
    # Check if all conditions are met
    if registered == 'Y' and open_lab == 'Y' and comp_avail == 'Y':
        return True
    else:
        return False

def get_reason(registered, open_lab, comp_avail):
    # Determine the reason based on the conditions
    if registered != 'Y':
        return "Student is not registered"
    elif open_lab != 'Y':
        return "Computer lab is closed"
    elif comp_avail != 'Y':
        return "No available computer"
    else:
        return "Welcome to the lab"

