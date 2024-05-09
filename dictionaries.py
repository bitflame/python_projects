# use a dictionary to store information about a person
person_1 = {
    'first_name':'jim',
    'last_name':'beam',
    'age': 47,
    'city': 'chicago',
}

print(person_1['first_name'])
print(person_1['last_name'])
print(person_1['age'])
print(person_1['city'])
print(person_1.get('school','No information about their school is available'))
#use a dictionary to store people's favorit numbers
peoples_favorite_numbers = {
    'sarah':22,
    'steve':31,
    'shane':14,
    'bob':39,
    'jane':20,
} 
print(f"Sarah's favorite number is: {peoples_favorite_numbers['sarah']}")
print(f"Bob's favorite number is: {peoples_favorite_numbers['bob']}")
print(f"Jane's favorite number is: {peoples_favorite_numbers['jane']}")
print(f"Shane's favorite number is: {peoples_favorite_numbers['shane']}")
print(f"Steve's favorite number is: {peoples_favorite_numbers['steve']}")

#Think of five programming words you learned and store them along with their meaning
glossary = {
    'conditional':'Expression with outcome of true or false',
    'list':'Name of a collection that python supports',
    'interpreter':'python\'s prompt',
    'boolean':'Native type of true or false',
    'variable':'Native type to store data',
    'loop' : 'Language constructs that does one or more tasks again and again',
    'Dictioanry':'A data structure supported in different high level languages that has a key/value pair mapping',
    'array' : 'A collection data structure supported by different languages',
    'set':'A collection that does not allow redundant items',
    'compiler':'A software that translates a file into machine readable version',
}    
print("A boolean is",glossary['boolean'])
print("A list is",glossary['list'])
print("A conditional is an",glossary['conditional'])
print("An interpreter is",glossary['interpreter'])
print("A variable is", glossary['variable'])

#write  a loop that prints the content of glossary - Exercise 6-5
print("\nThe following are key/value pairs in the glossary...")
for term, termDef in glossary.items():
    print(f"{term}'s meaning is {termDef}")

print("\nThe following are just the keys in glossary")   
for term in glossary.keys():
    print(term)
    
print("\nThe following are just the values: ")
for termDef in glossary.values():
    print(f"{termDef}")

# Exercise 6-5 Make a dictionary containing three major rivers and the county eache river runs through
major_rivers = {
    'Potomac':'United States',
    'Ural':'Russia',
    'Nile': 'Egypt',
}
print("\nHere are all the rivers and their associated countries: ")
for river, country in major_rivers.items():
    print(f"The {river} is in {country}")
print("\nHere is just the names...")
for river in major_rivers.keys():
    print(river)
    
print("\nHere are the countries they are in: ")
for country in major_rivers.values():
    print(country)

favorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}
should_take_pol = ['bob', 'jen', 'steve', 'phil', 'sam']

for name in should_take_pol:
    if name in favorite_languages:
        print(f"Dear {name}, thank you for taking the poll.")
    else: print(f"Dear {name}, would you please take the poll.")

#Excersise 6-7 add to the program you wrote for 6-1 by creating a couple of more dictionaries, and store all of them into a list 
# called people and print everything using loops
person_2 = {
    'first_name':'Robert',
    'last_name':'boyd',
    'age':'23',
    'city': 'miniapolice',
}
person_3 = {
    'first_name':'Henry',
    'last_name':'Jackson',
    'age': '34',
    'city':'Roseville',
}
people = [person_1, person_2,person_3]
# print(people)
for person in people:
    for infoType, infoContent in person.items(): 
        print(f"{infoType}: {infoContent}")
#Exercise 6-8 - create a list of dictionaries which are pets
creature_1 = {
    'kind': 'hamster',
    'owner': 'bill bilachec',
}
creature_2 = {
    'kind':'dog',
    'owner':'janet yellen',
}
creature_3 = {
    'kind': 'cat',
    'owner':'sam soulisack',
}

#for infoCategory, infoContent in creature_1.items():
#   print(f"{infoCategory}:{infoContent}")

pets = [creature_1, creature_2, creature_3]

for pet in pets:
    for info in pet.keys():
        print(f"{info} {pet[info]}")
        
        
for pet in pets:
    print(f"This is a {pet['kind']}, and its owner is: {pet['owner']}")