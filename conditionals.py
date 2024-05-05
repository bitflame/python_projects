vehicle = 'toyota'
print('Testing to see if vehicle is ford. I predict false')
vehicle == 'ford'
print('Testing to see if vehicle is toyota. I predict true')
vehicle == 'toyota'
vehicle = 'subaru'
print('testing to see if vehicle is blazer; predict false')
vehicle == 'blazer'
print('Testing to see if vehicle is subaru; predict true')
vehicle == 'subaru'
vehicle = 'audi'
print('Testing to see if vehicle is ford; I predict false')
vehicle == 'ford'
print('Testing to see if vehicle is audi; I predict True')
vehicle == 'audi'
vehicle = 'saab'
print('Testing to see if vehicle is pontiac; predict false')
vehicle == 'pontiac'
print('Test 8 - Testing to see if vehicle is saab; predict True')
vehicle == 'saab'
vehicle = 'jeep'
print('Testing to see if vehicle is a Hummer; predict false')
vehicle == 'hummer'
print('Testing to see if vehicle is a jeep; predict True')
vehicle == 'jeep'
vehicle.title() == 'jeep'.title() 
vehicle.lower() == 'jeep'.lower()
'jeep' > 'alpharomeo'
2 > 1
2 < 0
2 < 4 and 1 > 0
pizzas = ['cheese', 'peproni', 'vegeterian','mushroom']
'cheese' in pizzas
'pinapple' not in pizzas
var_1 = 22
var_2 = 12 
var_1 < var_2
var_1 >= var_2
2 == 2.0
var_1 != var_2
var_1 < 50 and var_2 > 10
var_1 > 60 or var_2 > 9
'anchovies' not in pizzas
alian_color = 'green'
if alian_color == 'green':
    print('You earned 5 points')
    
alian_color = 'red'
if alian_color == 'green':
    print('You earned five points.')

alian_color = 'yellow'
if alian_color == 'green':
    print('You earned five points')
else:
    print('change the alien color to something else')    
    
for value in range(1, 100):
    print(value)
    
for value in 1, 101:
    print("Hello")

alian_color = 'green'
if alian_color == 'green':
    print('You earned five points. Because alian color was green')
else: 
    print('You earned 10 points')
    
alian_color = 'red'
if alian_color == 'green':
    print('You earned five points because alien color was green.')
else:
    print('You earned 10 points because the alien color was red.')
# Exercise 5-5  
print ('********************************Exercise 5-5*********************************')
alian_color = 'green'
if alian_color == 'green':
    print('You earned five points')
elif alian_color == 'yellow':
    print('You earned 10 points because the alien color was yellow.')
elif alian_color == 'red':
    print('You earned 15 points because the alien color was red')

alian_color = 'red'
if alian_color == 'green':
    print('You earned five points')
elif alian_color == 'yellow':
    print('You earned 10 points because the alien color was yellow.')
elif alian_color == 'red':
    print('You earned 15 points because the alien color was red')

alian_color = 'yellow'
if alian_color == 'green':
    print('You earned five points')
elif alian_color == 'yellow':
    print('You earned 10 points because the alien color was yellow.')
elif alian_color == 'red':
    print('You earned 15 points because the alien color was red')

alian_color = 'blue'
if alian_color == 'green':
    print('You earned five points')
elif alian_color == 'yellow':
    print('You earned 10 points because the alien color was yellow.')
elif alian_color == 'red':
    print('You earned 15 points because the alien color was red')
else:
    print('This color alien has never been seen')
    
# 5-6 
print('*******************************Exercise 5-6***************************')
age = 1
if age < 2: 
    print('You are a baby:)')
elif age >= 2 and age <4:
    print('You are a toddler:)')
elif age >= 4 and age < 13:
    print('You are a kid:)')
elif age >= 13 and age < 20:
    print('You are a teenager:)')
elif age >= 20 and age < 65: 
    print('You are an adult:)')
else: print('You are an elder.:)')

age = 2
if age < 2: 
    print('You are a baby:)')
elif age >= 2 and age <4:
    print('You are a toddler:)')
elif age >= 4 and age < 13:
    print('You are a kid:)')
elif age >= 13 and age < 20:
    print('You are a teenager:)')
elif age >= 20 and age < 65: 
    print('You are an adult:)')
else: print('You are an elder.:)')


age = 4
if age < 2: 
    print('You are a baby:)')
elif age >= 2 and age <4:
    print('You are a toddler:)')
elif age >= 4 and age < 13:
    print('You are a kid:)')
elif age >= 13 and age < 20:
    print('You are a teenager:)')
elif age >= 20 and age < 65: 
    print('You are an adult:)')
else: print('You are an elder.:)')

age = 13
if age < 2: 
    print('You are a baby:)')
elif age >= 2 and age <4:
    print('You are a toddler:)')
elif age >= 4 and age < 13:
    print('You are a kid:)')
elif age >= 13 and age < 20:
    print('You are a teenager:)')
elif age >= 20 and age < 65: 
    print('You are an adult:)')
else: print('You are an elder.:)')

age = 20
if age < 2: 
    print('You are a baby:)')
elif age >= 2 and age <4:
    print('You are a toddler:)')
elif age >= 4 and age < 13:
    print('You are a kid:)')
elif age >= 13 and age < 20:
    print('You are a teenager:)')
elif age >= 20 and age < 65: 
    print('You are an adult:)')
else: print('You are an elder.:)')

age = 65
if age < 2: 
    print('You are a baby:)')
elif age >= 2 and age <4:
    print('You are a toddler:)')
elif age >= 4 and age < 13:
    print('You are a kid:)')
elif age >= 13 and age < 20:
    print('You are a teenager:)')
elif age >= 20 and age < 65: 
    print('You are an adult:)')
else: print('You are an elder.:)')