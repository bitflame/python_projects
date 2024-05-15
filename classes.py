from restaurant import Restaurant
class User:
    def __init__(self, first_name, last_name, age, education, position):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.education = education
        self.position = position
        self.login_attempts = 0
    def increment_login_attempts(self, current_login_attempts):
        self.login_attempts += current_login_attempts
    def reset_login_attempts(self):
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old, has a {self.education}, and is {self.age} years old and is currently working as a {self.position}")
        
    def greet_user(self):
        print(f'Dear Mr./Mrs. {self.first_name} {self.last_name} nice to meet you.')
    
user_1 = User('Shahin', 'Ansari', '54', 'Masters in Telecommunication', 'Instructor')
user_2 = User('Amy', 'Hamilton', '45', 'BS in Accouting', 'Accountant')
user_3 = User('Bill', 'Bason', '51', 'Doctorate in Law', 'Attorney')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()


# Exercise 9-5 add two methods to User class called increment_login_attempts() and reset_login_attempts(). Then create an instance 
# and call increment_login_attempts() a few times and print it each time and then call reset_login_attempts()
user_4 = User('Shane', 'Murphy', 44, 'B.S. of Electrical Engineering', 'Engineer')
print(f'{user_4.first_name} {user_4.last_name} has logged in {user_4.login_attempts} times so far.')
user_4.increment_login_attempts(3)
print(f'{user_4.first_name} {user_4.last_name} has logged in {user_4.login_attempts} times so far.')
user_4.increment_login_attempts(2)
print(f'{user_4.first_name} {user_4.last_name} has logged in {user_4.login_attempts} times so far.')
print(f'now resetting {user_4.first_name} {user_4.last_name}\'s loging attempts....')
user_4.reset_login_attempts()
print(f'{user_4.first_name} {user_4.last_name} has logged in {user_4.login_attempts} times so far.')
'''Exercise 9 - 6 Ice cream stand - write a class called IceCreamStand that inherits from Restaurant. Add an attribute called 
flavors and write a method that displays these flavors. Create an instance of it and call it'''
'''Exercise 9 - 10 The following code also demonstrates what this question asked for which was to import Restaurant class from 
another file'''
class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['Strawberry', 'Coffee', 'Mellon', 'Vanilla']
    def list_flavors(self):
        print(self.flavors)
        
icecream_shop = IceCreamStand("Sugar'n Spice", "deserts")
# if I do not add ()'s to the method below, python does not say anything. No error is generated. It just won't do what is in the methond
print("Here is a list of the flavors in the icecream shop")
icecream_shop.list_flavors()
print('Here is restaurant\'s dscription:')
icecream_shop.describe_restaurant()
'''Exercise 9-7 write a class called admin that inherits from the user class'''
class Admin(User):
    def __init__(self, first_name, last_name, age, education, position, privilages):
        super().__init__(first_name, last_name, age, education, position)
        self.privilages = privilages
    def show_privilages(self):
        return self.privilages
priv = ['can add post', 'can delete post', 'can ban user']
administrator = Admin('Shahin', 'Ansari', '53', 'Masters in Telecommunication','Instructor', priv)
administrator.describe_user()
print(f'His privilages are {administrator.show_privilages()}')
'''Exercise 9-8 Write a class called Privilages with an attribute called privilages that stores a list of strigns as described in 
the previous exercise, then create a new instance of admin - maybe called UpdatedAdmin and use the Privilages calss in it'''
class Privilages():
    def __init__(self, priv):
        self.privilages = priv
    def show_privilags(self):
        return priv
    
class UpdatedAdmin(User):
    def __init__(self, first_name, last_name, age, education, position, priv):
        super().__init__(first_name, last_name, age, education, position)   
        self.priv = Privilages(priv)
admin_privilages = Privilages(['can add post', 'can delete post', 'can ban user']) 
shahins_account = UpdatedAdmin('Shahin', 'Ansari', 53, 'Masters in Telecommunication', 'Instructor', admin_privilages)
print('printing privilages for Updated Account class')
print(shahins_account.priv.show_privilags())
