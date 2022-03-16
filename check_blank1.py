def check_blank(question, error_msg):
    while True:
        response =  input(question)
        if response == "":
            print("You must enter something!")
        else:
            return response
