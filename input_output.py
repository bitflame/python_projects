# Exercise 7-10 Dream vacation. Write a program that polls users about their dream vacation. Write a prompt similar to If you could 
# visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
dream_vacation_list = []
prompt = "If you could go anywhere in the world, where would you go? "
active = True
while active: 
    response = input(prompt)
    if response == "": active=False
    else: 
        dream_vacation_list.append(response)    
for location in dream_vacation_list:
    print(location)
    
#Exercise 7-1
desired_car = input("Tell me what kind of car you like: ")
print(f"Let me see if I can find a {desired_car}")
number_0f_guests=input("How many people are in your dinner group? ")
if int(number_0f_guests)>8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")
num = input("Please enter a number: ")
if int(num)/10 == 0:
    print(f"{num} is a multiple of 10")
else: print(f"{num} is not a multiple of 10.")
#Exercise 7-4
prompt = ("enter what pizza tapings you like one at a time." +
          "when you are done please enter the word\'done\'. ")
topping = ''
while (topping!='done'):
    topping = input(prompt)
    if topping=='done':
        continue
    print(f"I will add {topping} to your pizza")    

# Exercise 7-5
prompt = "How old are you please? "
answer = "do you need tickets?(y/n)"
response = 'y'
age = " "
while(response=='y'):
    age = input(prompt)
    if int(age) <=3 : 
        print("No charge")
    elif int(age) <= 12:
        print("please pay $10.")
    else: print("please pay $15.")
    response = input(answer)
    
# Exercise 7 -6 Three exits version 1
prompt = "How old are you please? (enter 0 to stop) "
age = int(input(prompt))
while(age > 0):
    if age <=3 : 
        print("No charge")
    elif age <= 12:
        print("please pay $10.")
    else: 
        print("please pay $15.")
    age = int(input(prompt))


# Exercise 7 -6 Three exits version 2
prompt = "How old are you please? "
age = ""
active = True
while(active):
    age = input(prompt)
    if age == '' : active= False
    elif int(age) <=3 : 
        print("No charge")
    elif int(age) <= 12:
        print("please pay $10.")
    else: print("please pay $15.")

# Exercise 7 -6 Three exits version 3
prompt = "How old are you please? (type in quit to stop the program)"
age = ""
active = True
while(active):
    age = input(prompt)
    if age == 'quit' : 
        break
    elif int(age) <=3 : 
        print("No charge")
    elif int(age) <= 12:
        print("please pay $10.")
    else: print("please pay $15.")
    
# Excersise 7-8 make a list with sandwitch orders and copy it to finished_sandwiches
sandwitch_orders = ['tuna', 'egg_salad', 'blt', 'turkey', 'chicken_breast', 'meat_loaf']
finished_sandwitches = []
for sandwitch in sandwitch_orders:
    print(f"I made your {sandwitch} sandwitch order.")
    finished_sandwitches.append(sandwitch)
print("Here are all the sandwitches that are ready: ")
for sandwitch in finished_sandwitches:
    print(f"{sandwitch} sandwitch.")

# Excersise 7-9 make sure pastarami appears at least three times. Add code near the beginning of your code to print a message
# saying dthe deli has run out of pastrami, and then use a while loop to remove all the occurances of pastami from sandwich_orders
# make sure no pastrami sandwiche end up in the finished_sandwitches 
sandwitch_orders = ['tuna', 'egg_salad', 'pastrami', 'pastrami', 'pastrami', 'blt', 'turkey', 'chicken_breast', 'meat_loaf']
finished_sandwitches = []
for sandwitch in sandwitch_orders:
    while('pastrami' in sandwitch_orders): # this block is so neat, powerful, and different from Java
        print('deli has run out of pastrami')
        sandwitch_orders.remove('pastrami')
    print(f"I made your {sandwitch} sandwitch order.")
    finished_sandwitches.append(sandwitch)
print("Here are all the sandwitches that are ready: ")
for sandwitch in finished_sandwitches:
    print(f"{sandwitch} sandwitch.")
    
