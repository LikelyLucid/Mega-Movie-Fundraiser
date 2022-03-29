def interger_checker(question, low_num, high_num):
    error = f"Please enter an integer between {low_num} and {high_num}."
    valid = False
    while not valid:
        try:
            