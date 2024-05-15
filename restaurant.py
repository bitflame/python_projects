# Exercise 9-1 
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} restaurant has {self.cuisine_type} type of cuisine.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is now open")
        
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, todays_clients):
        self.number_served += todays_clients
                
restaurant = Restaurant("Food for Thought", "Gluten Free cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()
#Exercise 9-2 Create three different instances of the type Restaurant and call describe_restaurant() on each of them
restaurant_one = Restaurant("Beer and Bacon", "Comfort Food")
restaurant_two = Restaurant("Stewie", "Heart Healthy Stews and Curries")
restaurant_three = Restaurant('Aowsome Salads', 'Live food')

restaurant_one.describe_restaurant()
restaurant_two.describe_restaurant()
restaurant_three.describe_restaurant()
# exercise 9-4 create a new restaurant, print the number of customers it served, then change it and print it again
new_restaurant = Restaurant('Happy Belly', 'Sandwitches')
print(f'{new_restaurant.restaurant_name} has served {new_restaurant.number_served} clients. ')
new_restaurant.number_served = 45
print(f'{new_restaurant.restaurant_name} has served {new_restaurant.number_served} clients. ')
# now add a method called set_number_served() that lets you set teh nubmer of ccustomers 
new_restaurant.set_number_served(79)
print(f'{new_restaurant.restaurant_name} has served {new_restaurant.number_served} clients. ')
# add a method called increment_number_served()
new_restaurant.increment_number_served(9)
print(f'{new_restaurant.restaurant_name} has served {new_restaurant.number_served} clients. ')