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

        
