# 10-6 write a program that adds two numbers the user inputs
print('This program will add the nubmers you type in')
try:
    value_1 = int(input('enter the first value please. '))
    value_2 = int(input('enter the second value please. '))
except ValueError:
    print('The value you enter has to be a number')
else:
    print(f'The sum of {value_1} and {value_2} is {value_1 + value_2}')