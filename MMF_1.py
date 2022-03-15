def check_blank(question):
    while True:
        response =  input(question)
        if response == "":
            print("You must enter something!")
        else: