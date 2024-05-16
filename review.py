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
# exercise 10-13
path = Path('user_credentials.json')
if path.exists():
    new_credentials = path.read_text()
    converted_new_credentials = json.loads(new_credentials)
    answer = input(f"Is {converted_new_credentials['username']} your username? (y/n) ")
    if answer=='y':
        new_credentials = path.read_text()
        converted_new_credentials = json.loads(new_credentials)
        print(f"Welcome Mr. {converted_new_credentials['username']}")
        for key, val in converted_new_credentials.items():
            print(f"{key}:{val}")
    else:
        user_credentials = {}
        user_name = input('Please enter your username: ')
        user_credentials['username'] = user_name
        pass_wd = input('Please enter the password you would like: ')
        user_credentials['password'] = pass_wd
        user_age = input('Please enter how old you are: ')
        user_credentials['age'] = user_age
        json_content = json.dumps(user_credentials)
        path.write_text(json_content)