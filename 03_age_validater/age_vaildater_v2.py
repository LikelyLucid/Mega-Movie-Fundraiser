def number_checker(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(question))
            if isinstance(number_to_check, int):
                return number_to_check
        except ValueError:
            print("\nPlease enter an integer (eg a whole number with no decimal)")
age = interger_checker("\nPlease enter age of ticker holder: ", 12, 110)
print(f"Age = {age}")