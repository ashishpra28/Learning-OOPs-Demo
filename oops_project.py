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
            self.signup() 
        elif user_input == '2':
            self.singin()
        elif user_input=='3':
            pass
        elif user_input == '4':
            pass 
        else:
            pass 

    def signup(self):
        email = input("enter email")
        password  = input("enter pass")

        self.username = email
        self.password = password
        print("wow signed up succesfully")
        print("\n")
        self.menu()

    def singin(self):
        if self.username == '' and self.password =='':
            print("bsdk phle signup krle teri mkc")
        else:
            new_user = input("la username bta")
            new_pass = input("la pass bta")
            if self.username == new_user and self.password == new_pass:
                print("chl bdiua signup hogya")
                self.loggedin = True
                print(" ab bta kya krna chahega - \n")
                print(self.menu())
            else:
                print("bsdk shi shi dalde")

ram = Chatbook()