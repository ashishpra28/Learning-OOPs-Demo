class Chatbook: 

    # statis method 
    __user_id = 0
    def __init__(self):
        self.id = Chatbook.__user_id
        Chatbook.__user_id += 1 
        self.__user1 = "BKL"
        self.username = ''
        self.password = ''
        self.loggedin = ''
        # self.menu()

    @staticmethod
    def get_id():
        return Chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        Chatbook.__user_id = val 

    def getter(self):
        return self.__user1
    
    def setter(self, val):
        self.__user1 = val

    def menu(self): 
        user_input = input("""1. for signup
                          2. for signin
                          3. for write as post
                          4. for message 
                          5. press f keys to log out
                          
                          
                          -->""")
        
        if user_input == '1':
            self.signup() 
        elif user_input == '2':
            self.singin()
        elif user_input=='3':
            self.mssg()
        elif user_input == '4':
            self.send_mssg()
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

    def mssg(self):
        if self.loggedin == True:
            print("mssg daal chl")
            with open("msg.txt",'a') as f:
                f.write(input()+"\n")
        else:
            print("bhnklode teri gaand tod dunga signin krle")
        self.menu()
    def send_mssg(self):
        if self.loggedin == True: 
            friend = input("friend ka naam bta")
            print(f"{friend} isko mssg likh chl")
            filename = f"{friend}.txt"
            with open(filename, 'a') as f:
                f.write(input()+"\n") 
        else:
            print("bhnklode teri gaand tod dunga signin krle")
        print("or agr bahar jana chahta h to F key press kr")
        self.menu()
        print("byby lodu")

user = Chatbook()