MIN_AGE = 12
MAX_AGE = 110

def number_checker(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("\nPlease enter an integer (eg a whole number with no decimal)")

age = number_checker("\nPlease enter age of ticker holder: ")
if age < MIN_AGE:
    print(f"\nSorry, you must be at least {MIN_AGE} years old to buy a ticket")
else:
    