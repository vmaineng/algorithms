def array_madness(a,b):
    #receive two list of integers
    #return boolean if squared list of a > squares list of b
    
    #find the sum squares of a
    #find the sum squared of b
    #return if  a > b
    
    squared_a = sum([num ** 2 for num in a])
    squared_b = sum([num ** 3 for num in b])
    
    print(squared_a, squared_b)
    
    return squared_a > squared_b