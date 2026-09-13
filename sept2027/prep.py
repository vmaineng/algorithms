def createTree(str):
    #receive an integer, return a level tree with * 
    #return a string with the tree
    #n = 3
    #[ ' *  ', ' *** ', '*****' ]

    #result
    #add in a string

    result = []

    for i in range(1, str+1):
        row = ' ' * (str - i) + '*' * (2 * i - 1) + ' ' * (str - i)
        result.append(row)
    return result

print(createTree(3))