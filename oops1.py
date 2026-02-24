class Employee: 
    def __init__(self): 
        self.name = "Rahul"
        self.salary = "736374673"

    def travel(self,country):
        print(f"{self.name} go to {country}") 
       
e1 = Employee()
e1.travel("newyork")