from pathlib import Path


path = Path('text_files/my_text.txt')
content = path.read_text().rstrip()
print(content)
