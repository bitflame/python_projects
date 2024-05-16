import json
from pathlib import Path

path = Path('json_numbers.json')
content = path.read_text()
numbers = json.loads(content)
print(numbers)

path = Path('username.json')
if path.exists():
    print('username.json exists.')
else:
    print('username.json does not exist. We have to create it.')