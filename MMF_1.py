def check_blank(question):
    valid = ""
    while not valid:
        valid = input(question)
        if valid.strip():
            return valid
        else:
            print("Please enter a value.")