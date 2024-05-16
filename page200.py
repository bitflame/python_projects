from pathlib import Path
import json
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
        '''Exercises 10-8 and 10-9'''
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
'''Exercise 10-10'''
try:
    path = Path('pg65903.txt')
except FileNotFoundError:
    pass
lines = path.read_text(encoding='utf-8').splitlines()
result = 0
for line in lines:
    result += line.lower().count('row')
print(f"The number of the word row in Carl Jung's Psychology of the Unconsicious is {result}")

numbers = [1,2,3,4,5]
path = Path('json_numbers.json')
content = json.dumps(numbers)
path.write_text(content)