def check_blank(question, error_msg): # define function
    while True: # repeat forever
        response =  input(question) # get input
        if not response.isalpha(): # if response is not alpha
            print(error_msg)
        else:
            return response
