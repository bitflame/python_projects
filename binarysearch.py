def binary_search(arr, value):
    # set teh initial value
    first = 0
    last = len(arr)-1
    position = -1
    found = False
    # Search for the value 
    while not found and first <= last:
        #calculate the mid point
        middle = (first + last) / 2

        # If the value is found at the mid point...
        if arr[middle] == value:
            found = True
            position = middle
        # else if value is in the lower half...
        elif arr[middle]>value:
            last = middle -1
        # else if value is in the upper half...
        else:
            first = middle+1
    # Return the position of the item, or -1
    # if it was not found
    return position
names = ['ali', 'Habib', 'Fatima', 'Samad', 'Babak', 'charlie','david','edward']
binary_search(names,8)

