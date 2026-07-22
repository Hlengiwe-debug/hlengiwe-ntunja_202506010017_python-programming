# ticket.py
def create_ticket():
    print("=== IT Helpdesk Ticket ===")
    
    # Collecting user input
    name = input("Enter Student Name: ")
    student_id = input("Enter Student ID: ")
    issue = input("Describe the Issue: ")
    location = input("Enter Location: ")
    
    # Missing input logic for priority and technician assignment
    priority = input("Enter Priority (High/Medium/Low): ").capitalize()
    
    if priority == "High":
        technician = "Ahmad"
    elif priority == "Medium":
        technician = "Siti"
    else:
        technician = "Ali"  # Assumes 'Low' or any other input defaults to Ali
    
    # Creating a dictionary to return to the main program
    return {
        "name": name,
        "id": student_id,
        "issue": issue,
        "location": location,
        "priority": priority,
        "technician": technician,
        "status": "Pending"
    }