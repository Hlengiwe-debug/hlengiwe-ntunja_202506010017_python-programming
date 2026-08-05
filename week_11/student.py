def get_student():
    print("Computer Lab Access ")
    # Get student and lab details
    name = input("Student Name : ")
    student_id = input("Student ID : ")
    registered = input("Registered for today's lab? (Y/N): ")
    open_lab = input("Is the lab open? (Y/N): ")
    comp_avail = input("Computer Available? (Y/N): ")
    return name, student_id, registered, open_lab, comp_avail
