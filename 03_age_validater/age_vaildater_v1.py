def interger_checker(question, low_num, high_num):
    error = f"Please enter an integer between {low_num} and {high_num}."
    valid = False
    while not valid:
        try:
            number_to_check = int(input(question))
            if low_num <= number_to_check <= high_num:
                return number_to_check
            else:
                print(error)
        except ValueError:
            print("\nPlease enter an integer (eg a whole number with no decimal")
age = interger_checker("\nPlease enter age of ticker holder: ", 12, 110)