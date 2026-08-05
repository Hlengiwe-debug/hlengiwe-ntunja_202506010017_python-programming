from student import get_student
from access import check_access, get_reason
from display import print_result

def main():
    # 1. Get all user inputs
    name, student_id, registered, open_lab, comp_avail = get_student()

    # 2. Check access rules
    is_allowed = check_access(registered, open_lab, comp_avail)

    # 3. Determine status text
    if is_allowed == True:
        status = "Access Granted"
    else:
        status = "Access Denied"

    # 4. Get the reason for the result
    reason = get_reason(registered, open_lab, comp_avail)

    # 5. Display the result
    print_result(name, student_id, status, reason)

if __name__ == "__main__":
    main()