# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multiplier = 1):
    # receive a list of lists of numbers
    #return the total of all numbs together

    #[4[3,8]] => 4 + 2 * (8 +3) 4+ 22 => 26

    #iterate through each eelemnt of the list
    #check if it is a list
    #then add all the numbers, increase the multiplei
    #else, it's not a list, then add all the numbers together
    #add sum together

    total = 0
    if not array:
        return 0

    for element in array:
        if type(element) is list:
            total += productSum(element, multiplier + 1)
        else:
            total += element
    return total * multiplier
    
def staircaseTraversal(height, maxSteps):
    # receive integers for height and maxsteps
    #return max steps

    
    if height == 0:
        return 1

    numberOfWays = 0
    for step in range(1, min(maxSteps, height) + 1):
        if step <= height:
            numberOfWays += staircaseTraversal(height-step, maxSteps)
    return numberOfWays

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth = 1):
    # receive a list of integers
    #return the productSum from the special array

    #intiailize a total to 0
    #iterate through each num
    #check if it is an array
    #then iterate through it

    total = 0
    for num in array:
        if type(num) == list:
            total += productSum(num, depth + 1)
        else:
            total += num
    return total * depth

def getNthFib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFib(n-1) + getNthFib(n - 2)
    #time: O(2^n) and O(n) space

        def getNthFib(n, memoize={1:0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
        return memoize[n]

#time:O(n) and O(n) space
def getNthFib(n):
    lastTwo= [0,1]
    counter = 3
    while counter <=n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0]= lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]
#time:O(n) and space O(1)