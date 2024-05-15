import display
from books import  favorite_book
from shirts import make_shirt as mk
import cities as ct
from albums_functions import *
from classes import restaurant
# I can import an instance of a class. Wow
print('Printing restaurant is now open from another file that imported only an instance of a class called Restaurant.')
restaurant.open_restaurant()

display.display_message()

#exercise 8-2 write a function that takes a paramter that is the title of yoru favorit book
print("Exercise 8-2")
favorite_book('Alice in Wonderland')    
# exercise 8-3 write a func that accepts a size and text of the message that goes on a shirt
print("Exercise 8-3")
mk('medium', "SemperFi")
mk(message="Always Loyal", size=45)
# exercise 8-4 modify make_shirt so shirt sizes are large by default
def make_shirt(size='large', message="I Love Python"):
    print(f"Shirt size is {size}, and the message on it is: {message}")
# make a large shirt and a medium shirt with the default message
make_shirt()
make_shirt(size='medium')
make_shirt(message="I love Las Vegas!")

# Exercise 8-5 write a function called describe_city() that accepts the name of a city and its country and prints them out
ct.describe_city('Tokyo','Japan')
ct.describe_city("Seoul", 'Korea')
ct.describe_city("New Yourk City")
# Exercise 8-6 City Names write a function called city_county() that takes in the name of a city and its country return a 
# combinted string
print('--------------------------------Exercise 8-6----------------------------')
def city_country(city, country):
    result = f"{city.title()}, {country.title()}"
    return result

answer = city_country('tokyo', 'japan')
print(answer)

answer = city_country('mexico city', 'mexico')
print(answer)

answer = city_country('los angeles', 'united states')
print(answer)
# Exercise 8-7 write a function called make_album() that builds a dictionary describing a music album

albums = []
albums.append(make_album('Prince', 'Purple Rain'))
albums.append(make_album('Pink Floyd', 'The Wall', 6))
albums.append(make_album('Bob Marley', 'Sun is shining'))
print('Here are all the albums:')
for album in albums:
    for key, value in album.items():
        if not value: continue
        print(f" {key} : {value} ")
    print('---------------------')
# clearing the albums list for the next exercise. Exercise 8-8
albums.clear()
while True:
    name = input("\n enter the name of an artist, or enter \'q\' to exit:")
    if name == 'q': break
    album_title = input("\n enter the title of their title, or enter \'q\' to quite:")
    if album_title == 'q': break
    albums.append(make_album(name, album_title))
if albums:
    print('Here are all the albums:')
    for album in albums:
        for key, value in album.items():
            if not value: continue
            print(f" {key} : {value} ")
        print('---------------------')

# Exercise 8-9 Make a list of short text messages and pass it to a function called show_messages() which prints them
messages = ['What\'s up?', 'How you doin?', 'Good Morning', 'See you later']
sent_messages =[]
def show_messages(messages):
    while messages: 
        current_message = messages.pop()
        sent_messages.append(current_message)
show_messages(messages)
print('\nPrinting the original list after passing it to show_messages() method: ')
for message in messages:
    print(message)
print('\nHere is the content of sent_messages list:')
for message in sent_messages:
    print(message)
# Exercise 8-9 start with the previous list.  Call the function with a copy of the list of messages. Then print both of your 
# lists
# reseting sent_messages, and messages list
sent_messages=[]
messages = ['What\'s up?', 'How you doin?', 'Good Morning', 'See you later']
show_messages(messages[:])
print('\nNow printing the original list again. This time using slice to copy the original list')
for message in messages:
    print(message)
print('\nHere is the content of sent_messages list:')
for message in sent_messages:
    print(message)
# exercise 8-12 write a function that accepts a list of items a person wants on a sandwich and it should print the ingridients
def make_sandwitch(*items):
    print(f'The sandwitch has {items}')

make_sandwitch('Chicken breast', 'Lettuce', 'Tomatos', 'Mayonaise')

def make_good_sandwitch(*items):
    for item in items:
        print(f"{item}")
make_good_sandwitch('Chicken breast', 'Lettuce', 'Tomatos', 'Mayonaise')
'''Exercise 8-13 User Profile build a profile of yourself using user_profile()'''
def user_profile (first_name, last_name, **user_info):
    user_info['first name']=first_name
    user_info['last name']= last_name
    for key, value in user_info.items():
        print(f"{key}: {value}")
        
user_profile('shahin', 'ansari', age = 54, status = 'single', weight = '220')
'''Exercise 8-14 write a function taht stores info abouta car in a dictionary, it should always receive a manufacturer and model
name followed by an arbiturary number of of keywords. Call it with two other attributes like color and optional feature'''
def make_car(make, model, **additional_options):
    additional_options['manufacturer']=make
    additional_options['model']=model
    return additional_options
car = make_car('subaru', 'outback', color = 'blue', tow_package=True)

for key, value in car.items():
    print(f"{key}: {value}")