#friend or foe
#filters a list of strings

#if name has 4 letters == friend, else foe

#input = a list of strings
#output = a list of strings that are friends that has a length of 4
#ex: ['Mai', 'Kyle', 'Eric', 'Amanda'] => [ 'Kyle', 'Eric' ]

#[] => []
#[34, ] => always be strings only
#['Mai']
#with names longer than 4=> []

#initalize an empty list
#iterate through the input string
#check the length of name == 4
#add it to our empty list
#return the result list of names == 4

def friendOrFoe(array):
    result = []
    for name in array:
        if len(name) == 4:
            result.append(name)
    return result

# print(friendOrFoe(['Mai', 'Kyle', 'Eric', 'Amanda']))
# print(friendOrFoe(['Mai', 'Kye', 'Ric', 'Amanda']))

def sheepCount(array):
    # count = 0
    # for sheep in array:
    #     if sheep == True:
    #         count += 1
    # return count 
    return sum(sheep is True for sheep in array)

# print(sheepCount([True, False, False]))

def moveZeros(array):
    #receive a list of integers, false, and 0
    #return the list back where 0's move at the end
    #ex: 

    #create two pointers and i at beginning and j at the end

    i = 0 
    j = len(array) - 1

    while i < j:
        if array[i] == 0 and array[j] != 0:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -=1
        elif array[j] == 0:
            j -= 1
        else:
            i += 1
    return array

# print(moveZeros([False,1,0,1,2,0,1,3,"a"]))


#receive a list of integers that has all odds, and one even
#or all even and one odd
#takes an array and receive an outlier

def findOutlier(numbers):
    #iterate through the list of arrays
    #keep track of how many odds or evens found

    evenCount = 0
    oddCount = 0 

    for num in numbers:
        if num % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1

    if evenCount > oddCount:
        for num in numbers:
            if num % 2 != 0:
                return num
    else:
        for num in numbers:
            if num % 2 == 0:
                return num

   
print(findOutlier([3,5,2,7,9]))
