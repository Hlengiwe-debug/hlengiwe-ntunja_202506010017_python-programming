# display.py
def display_ticket(ticket):
    # Printing the output based on the expected format in the tutorial image
    print("*** IT Helpdesk Ticket ***")
    print("==========================")
    print(f"Student Name : {ticket['name']}")
    print(f"Student ID   : {ticket['id']}")
    print(f"Issue        : {ticket['issue']}")
    print(f"Location     : {ticket['location']}")
    print(f"Priority     : {ticket['priority']}")
    
    print("==========================")
    print("HELPDESK TICKET")
    print("==========================")
    print(f"Student Name : {ticket['name']}")
    print(f"Student ID   : {ticket['id']}")
    print(f"Issue        : {ticket['issue']}")
    print(f"Location     : {ticket['location']}")
    print(f"Priority     : {ticket['priority']}")
    print(f"Technician   : {ticket['technician']}")
    print(f"Status       : {ticket['status']}")
    print("==========================")