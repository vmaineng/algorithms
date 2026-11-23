def sumInt(array):
    #receive a list of nested lists
    #return the sum of all integers only
    #ex: 

    #iterate through the list
    #check if it is an int
    #add to sum , else ignore it

    if not array:
        return 0

    count = 0
    count += checkType(array)
    return count

def checkType(array):
    count = 0
    
    for item in array:
        if isinstance(item, int):
            count += item
        elif isinstance(item, list):
            count += checkType(item)
    return count

print(sumInt([[3,4], 3]))

