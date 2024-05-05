
my_favorite_pazzas = ['peperoni', 'white', 'cheese']
for pizza in my_favorite_pazzas:
    print("I like",pizza.title(),"Pizza")
print("Pizza is a neutritious delicious food that is not too difficult to make, and it does not take too long " +
      "the cheese provides protein and calcium and the tomato sauce has vitamins like vitamin C. The crust provides" +
      "carbs for energy. I just love pizzas and you can not go wrong with them.")

mamals = ['wolf', 'dog', 'cat']
for animal in mamals:
    print("A",animal," is a mamal.")
    
# a for loop that counts from 1 to 20 
for i in range(1, 21):
    print(i)

myNumbers = list(range(1, 1000001))
print(min(myNumbers))
print(max(myNumbers))
print(sum(myNumbers))

odd_numbers = list(range(1, 21, 2))
print("Here are odd numbers printed out:")
for value in odd_numbers:
    print(value)

every_three = list(range(3, 31, 3))
for value in every_three: 
    print(value)
print("Here is a list of cubed values from 1 to 10")
for value in range(1, 11):
    print(value**3)
    
print("Here is cubed values using list comprehensions")    
cubed = [value ** 3 for value in range(1, 11)]
print(cubed)

print("The first three items in the linst are: ", cubed[:3])
print("Three items from the middle of the list are:", cubed[3:6])
print("The last three items are: ", cubed[-3:])
print("The last three items are also: ", cubed[7:])
pizzas = ['peperoni', 'white', 'cheese']
friend_pizzas = pizzas[:]
pizzas.append("vegeterian")
friend_pizzas.append("pinapple")
print("My favorite pizzas are:")
for pizza in pizzas: 
    print(pizza)
print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
    

buffet = ('hamburger','fried chicken','steak', 'pizza')
print("Here is what the buffet serves: ")
for entre in buffet:
    print(entre)

# buffet[2]='mashed potatos' <- Trying to change an item in tupple gives an error message
print("Changing the content of buffet items. Now it contains: ")
buffet = ('hamburder', 'hotdog', 'fries', 'chicken fajitas')
for item in buffet:
    print(item)
count = 0
while count < 10: 
    print("Count = ", count)
    count=count+1