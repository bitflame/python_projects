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
print("I  can only have two guests for dinner")
print("Dear  ",dinner_guests.pop(),"Hope to see you on a different occasion.")
print("Dear ",dinner_guests.pop(),"Hope to see you on a different occasion.")
print("Dear ",dinner_guests.pop(), "Hope to see you on a different occasion. and now ", len(dinner_guests),"guests are remaining in the list")
print("Dear ",dinner_guests.pop(),"Hope to see you on a different occasion.")
print("now I have", len(dinner_guests),"guests, and they are ", dinner_guests)
del(dinner_guests[0])
del(dinner_guests[0])
print("Now the list of dinner guests should be empty: ",dinner_guests)
# exercise on page 45
places_to_see = ['zurich','budapesht','amsterdam','brussels']
print(places_to_see)
print(sorted(places_to_see))
print(places_to_see)
print(sorted(places_to_see,reverse=True))
print(places_to_see)
# reverse does not return anything. It just permanently reverses the list
places_to_see.reverse()
print(places_to_see)
places_to_see.reverse()
print(places_to_see)
places_to_see.sort()
print(places_to_see)
places_to_see.sort(reverse=tuple)
print(places_to_see)
dinner_guests = ['suzzy oh','camron diaz', 'angelina jolie']
print("Should print the number three: ", len(dinner_guests))
cars = ['blazer', 'taho', 'jeep','subaru']
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars, reverse=True))
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print(cars[0].title())
print(len(cars))
cars.reverse()
print(cars)
print(cars[3].title())
arrayOne = [1,2]
arrayTwo = [3,4]
def medianOfSortedArrays(arr1, arr2):
    print(arr1)
    print(arr2)
    
medianOfSortedArrays(arrayOne, arrayTwo)