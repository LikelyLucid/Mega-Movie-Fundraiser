def check_blank(question, error_msg): # define function
    while True: 
        response =  input(question)
        if not response.isalpha():
            print(error_msg)
        else:
            return response
