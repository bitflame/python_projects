from user import User

class Privilages():
    def __init__(self, privilages):
        self.privilages = privilages

class Admin(User):
    def __init__(self, first_name, last_name, age, privilages):
        super().__init__(first_name, last_name, age)
        self.privilages = Privilages(privilages)
    def show_privilages(self):
        print(self.privilages.privilages)
        '''The first privilages is an object. The second one if the actual list of privilages aka attribute'''
    def get_privilages(self):
        return self.privilages.privilages
user_2 = Admin('Morteza', 'Ansari', 53, ['Can create account', 'Can delete account', 'Can change permissions'])
user_2.show_privilages()