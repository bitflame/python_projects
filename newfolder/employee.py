class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary) 
    
    def give_raise(self, different_amount=0):
        if different_amount == 0:
           self.annual_salary = self.annual_salary + 5000
        else:
            self.annual_salary = self.annual_salary + different_amount
        return self.annual_salary
            
