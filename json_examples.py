import json
from pathlib import Path
numbers =[]
while (True):
    response = input('next number please - enter q to stop')
    if response == 'q': break
    numbers.append(int(response))
path = Path('favorite_numbers.json')