from pathlib import Path
path=Path('alice.txt')
def count_words(path):
    try:
       content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f'{path} does not exist')
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} wrods.")
        
file_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'] 
for file_name in file_names:
    path = Path(file_name)
    count_words(path)
