def check_blank(question):
    while True: #forever
        response =  input(question)
        if response == "":
            print("You must enter something!")
        else:
            return response
