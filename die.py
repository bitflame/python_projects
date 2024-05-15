'''Exercise 9-13 write class called Die and roll the dice 10 times. User randint()'''
from random import randint, choice, sample
class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)
my_dice = Die()
for i in range(1, 11):
    print(f"round: {i} {my_dice.roll_die()}")
'''Mike a list or tupple of 10 numbers and 5 letters and randomly select four of them'''
my_data = (1 , 2 , 3, 4, 5, 6, 7, 8, 9, 10, 's', 'e', 'i', 'o')
winning_ticket = []
for i in range(1, 5):
    winning_ticket.append(choice(my_data))
    
print(f'The winning_ticket is: {winning_ticket}')
''''write a loop that tells you how many times it ran before your ticket won'''
ticket_1 = [1,1,1,1]
ticket_2 = [1,1,1,1]
print(ticket_1==ticket_2)
my_ticket = ['s', 'o', 4, 10]
winning_ticket = []
counter = 0
while (my_ticket!=winning_ticket):
    counter += 1
    winning_ticket = sample(my_data, 4)
print(f'Took {counter} many times for your ticket to win')