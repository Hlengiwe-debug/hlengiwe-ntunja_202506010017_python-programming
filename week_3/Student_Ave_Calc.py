choice = "y"

# Initialize the loop with "y" so it runs at least once
while choice.lower() == "y":

    # Ask the user for the three quiz marks
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    # Calculate the average of the three marks
    average = (quiz_1 + quiz_2 + quiz_3) / 3

    # Check if the average is 50 or above, then display Passed or Failed
    if average >= 50:
        print("Passed")
    else:
        print("Failed")

    # Ask the user if they want to run the program again
    choice = input("Continue? Select Y/N: ")

print("Program Ended")