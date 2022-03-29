def number_checker(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(question))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("\nPlease enter an integer (eg a whole number with no decimal)")

age = number_checker("\nPlease enter age of ticker holder: ")
while not 12 <= age <= 110:
    age = number_checker("\nPlease enter interger between 12 and 110: ")