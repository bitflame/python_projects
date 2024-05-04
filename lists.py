cars = ['fiat', 'peykan', 'toyota', 'jeep']
cars
print (cars)
# line below demonstrates that I do not have to put a variable inside {}s in order to print
print("Here is the 2nd item in the list:", cars[1].title())
# like this...
print(f"Here is the 3rd item in the list: {cars[2].title()}")
print("The last car I owned was a ", cars[-1].title())
cars[0]='pontiac'
print(cars[0].title())
cars.append('ferari')
print(cars[-1].title())
print(cars)
cars.insert(1,'chevy')
print('Aded chevy to the list',cars)
dinner_guests = ['suzzy oh','camron diaz', 'angelina jolie']
print('Dear Mrs.',dinner_guests[0].title(),'I like to invite you for dinner')
print('Dear Mrs.',dinner_guests[1].title(),'I like to invite you for dinner')
print('Dear Mrs.',dinner_guests[2].title(),'I like to invite you for dinner')
print('Here is the original dinner list: ', dinner_guests)
dinner_guests.remove('angelina jolie')
dinner_guests.insert(2, 'lucy liu')
print('Here is the updated dinner list: ',dinner_guests)
dinner_guests.append('Jennifer Lawrence')
dinner_guests.append('dua lipa')
dinner_guests.append('Kate Beckinsale')
print('Updated list of dinner guests is:', dinner_guests)