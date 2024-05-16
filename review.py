import json
from pathlib import Path
'''This is the code for exercise 10-11 and 10-12'''


path = Path('review.json')
if path.exists():
    # read the same content form review.json
    read_content = path.read_text()
    read_text_content = json.loads(read_content)
    print(read_text_content)
else:
    favorite_numbers = []
    while(True):
        num = input('enter a number or q to stop. ')
        if num == 'q': break
        try:
            favorite_numbers.append(int(num))
        except ValueError:
            print('You can only enter numbers or lowercase letter q to quit')
    if len(favorite_numbers)>0:
        content = json.dumps(favorite_numbers)
        path.write_text(content)

