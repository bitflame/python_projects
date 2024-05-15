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

class Privilages():
    def __init__(self, priv):
        self.privilages = priv
    def show_privilags(self):
        return self.privilages.privilages

'''Extends User and uses Privilages class as one of its attributes''' 
class Admin(User):
    def __init__(self, first_name, last_name, age, education, position, priv):
        super().__init__(first_name, last_name, age, education, position)   
        self.privilages = Privilages(priv)
admin_privilages = Privilages(['can add post', 'can delete post', 'can ban user']) 
shahins_account = Admin('Shahin', 'Ansari', 53, 'Masters in Telecommunication', 'Instructor', admin_privilages)
print('printing privilages for Updated Account class')
print(shahins_account.privilages.show_privilags())