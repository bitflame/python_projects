from pathlib import Path

path=Path('reading_from_a_file/learning_python.txt')
lines = path.read_text().splitlines()
print(lines)
content = ''
for line in lines:
    content += line
print(content)
print(content.replace('Python', 'java'))

