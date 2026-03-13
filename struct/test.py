def jadenSmith(tweet):
    #receive a string
    #return a string back where first char is capitalize
    #ex: 'hi how are you?' => 'Hi How Are You?'

    #split string
    #captialize the first letter of string
    #add them together
    #and add them back together as one
    words = tweet.split()
    phrase = []
    for word in words:
        # word[0] = word[0].upper()
        newWord = word[0].upper() + word[1:]
        phrase.append(newWord)
    return ' '.join(phrase)

# print(jadenSmith('hi how are you?'))

#time: O(N), space: O(n)

#receive an array of numbers
#return sum of positive numbers
#if there's nothing is sum, return 0

def returnSum(array):
    #receive an array of integers (pos and negative), 
    # could be no numbers, and only whole integers
    #return an integer
    #ex: [2] => 2
    #ex: [-3] => 0
    #ex: [3, 2, -23, 0, 10] => 3 + 2+ 10 => 15

    #initialize a total starting at 0
    #iterate through each num in the array
    #check to see if the number is > 0
    #add the number to total (keep track of the running total)
    #return the total

    total = 0
    for num in array:
        if num > 0:
            total += num
    return total

# print(returnSum([-3]))

# def returnStr(str):
    #return each letter increasing 1 more time
    #ex: a - bb- ccc

    #iterate through each number and multiply by their idx + 1
    

#string is an isogram

def isogram(str):
    #receive a string of lowercase letters
    #return boolean?

    #iterate through each str
    #increment count in an object
    #if all values are one, return True, else false

    obj = {}

    for char in str.lower():
        if char not in obj:
            obj[char] = 1
        else:
            obj[char] += 1

    # print(obj)
    for char in obj:
        if obj[char] > 1:
            return False
        
    return True

# print(isogram('Ii'))

def multiple(num):
    #receive a positive integer
    #return num of times you multiply them unti lyou reach single digit
    #ex: 1 =. 0
    #ex: 23 => 2 * 3 = 6 = receive it 1 time

    #if length of num is 0 => return 0

    #

    #iterate through each num
    #keep a running total
    #if the integer is less than 10,
    #return the count

    if num < 10:
        return 0
    
    count = 0

    while num >= 10:
        total = 1
        for char in str(num):
            total *= int(char)
        num = total 
        count += 1
    return count

print(multiple(39))
print(multiple(1))
