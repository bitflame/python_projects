def duplicateCount(text):
    #Counts the number of characters of the same kind next to each other 
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
    