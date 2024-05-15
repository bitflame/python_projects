'''read in the file learning_python.txt, and replace the word Python with Java'''
from pathlib import Path


path = Path('learning_python.txt')
content = path.read_text()

entire_content = ''
for line in content.splitlines(): 
    line = line.replace('Python', 'Java')
    entire_content+=line
print(entire_content)
'''exercise 10-4 write user's name to a file'''
name = input('What is your name buddy? ')
path_2 = Path('output_file.txt')
path_2.write_text(name)
''''write a bunch of names to a file called guest_book.txt. Write each name to a different line'''
path_3 = Path('guest_book.txt')
response = ''
content = ''
while(response!='q'):
    response=input('Type in the next name please. type \'q\' to stop')
    if (response!='q'): 
        content+= response
        content+='\n'
    
path_3.write_text(content)