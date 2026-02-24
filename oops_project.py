class Chatbook: 
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = ''
        self.menu()

    
    def menu(self): 
        user_input = input("""1. for signup
                          2. for signin
                          3. for write as post
                          4. for message 
                          5. press other keys to log out""")
        
        if user_input == '1':
            pass 
        elif user_input == '2':
            pass 
        elif user_input=='3':
            pass
        elif user_input == '4':
            pass 
        else:
            pass 
ram = Chatbook()