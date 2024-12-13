def double(list):
    #receive a list of integers
    #return a new list where the value are doubled

    #ex: [1,2] => [2, 4]
    #ex: [-3, 0, 3] => [-6, 0, 6]

    #initialize a new array
    #iterate through each value in the list
    #multiply the value by 2
    #add to the list
    #return the new list

    doubleList = []
    for ele in list:
        doubleNumber = ele *2
        doubleList.append(doubleNumber)
    return doubleList

    #list comprehension
    return [ele*2 for ele in list]

result = double([1,2])
print(result)