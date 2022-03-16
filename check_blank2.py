def check_blank(question, error_msg):
    while True:
        response =  input(question)
        if not response.isalpha()
            print(error_msg)
        else:
            return response
