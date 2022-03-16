def check_blank(question, error_msg): # define function
    while True: # repeat forever
        response =  input(question) # get input
        if not response.isalpha():
            print(error_msg)
        else:
            return response
