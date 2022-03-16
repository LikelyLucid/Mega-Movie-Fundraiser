def check_blank(question, error_msg): # define function
    while True: # repeat forever
        response =  input(question) # get input
        if not response.isalpha(): # if response does not contain letters
            print(error_msg) # print error message
        else:
            return response 
