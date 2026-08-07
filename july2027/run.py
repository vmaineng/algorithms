def findNums(array):
    #receive a list of non-negative int and strings
    #return int only

    return [num for num in array if isinstance(num, int)]

print(findNums([2, "2"]))