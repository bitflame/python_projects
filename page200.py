from pathlib import Path
# 10-6 write a program that adds two numbers the user inputs
print('This program will add the nubmers you type in')
response = 'y'
while response=='y':
    try:
        value_1 = int(input('enter the first value please.'))
        value_2 = int(input('enter the second value please. '))
    except ValueError:
        print('The value you enter has to be a number')
    else:
        print(f'The sum of {value_1} and {value_2} is {value_1 + value_2}')
        response = input('another round? (y/n) ')
path = Path('cats.txt')
try:
    content = path.read_text().splitlines()
except FileNotFoundError:
    pass
print('Here is a list of cat names: ')
for line in content:
    print(line)
path = Path('dogs.txt')
try:
    content = path.read_text().splitlines()
except FileNotFoundError:
    pass
print('Here is a list of dog names: ')
for line in content:
    print(line)