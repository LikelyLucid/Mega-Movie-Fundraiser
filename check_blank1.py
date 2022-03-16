def check_blank(question):
    while True: # repeat forever
        response =  input(question)
        if response == "": # if response is empty
            print("You must enter something!") # print error message
        else: 
            return response # exit the function and return the response
