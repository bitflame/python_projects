def duplicateCount(text):
    #I need to use a dictionary or an array with the size of 256
    text = text.lower()
    counter, sum = 0,0
    while (counter  < len(text)-1):
        if (text[counter]==text[counter+1]): 
            sum=sum+1
        counter+=1
    return sum
    

text = 'Aabbcde'
print(duplicateCount(text))

text = 'abcdeaB'
print(duplicateCount(text))
    