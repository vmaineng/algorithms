#function that filters out string, returns list of friends name in it
#if name has 4 letters, name is friend otherwise they are not

#receive a list of strings
#return back a list of our friends whose length is only 4
#'Mark'
#receive only alphabetical letters
#array will never be empty

#ex: ['Mai', 'Mark', 'Amanda'] => ['Mark]

#initialize an empty array that will hold the answer
#iterate through all of names
#check the length == 4, add the name to the list
#return result

#time: O(n) #n 
#space: O(n)

def findFriends(array):
    result = []
    for name in array:
        if len(name) == 4 or len(name) == 6:
            result.append(name)
    return result

# print(findFriends(['Mai', 'Mark', 'Amanda']))

def addList(array): 
    result = []
    for idx, item in enumerate(array):
        result.append(f"{idx + 1}")
        result.append(":" + item)
    return result
# print(addList(['a','b','d']))


def findPangram(string):
    #pangram is a sentence that contains every letter at least once
    #receive a letter of string
    #return True or False

    #ex: The quick brown fox jumps over the lazy dog
    
    #iterate through sentence
    #join them all together as one
    #check if chars exist in my counterChars object where it has one of the chars

    joinSentence = ''.join(string.split()).lower()

    counter = {}
    for char in joinSentence:
        counter[char] = counter.get(char, 0) + 1

    charCounter = { 
        'a': 1,
        'b':1,
        'c': 1,
        'd': 1,
        'e': 1,
        'f': 1,
        'g': 1,
        'h': 1,
        'i': 1,
        'j':1,
        'k':1,
        'l': 1,
        'm': 1,
        'n': 1,
        'o': 1,
        'p': 1,
        'q': 1,
        'r':1,
        's': 1,
        't': 1,
        'u': 1,
        'v': 1,
        'w':1,
        'x': 1,
        'y': 1,
        'z': 1

    }
    
    # for char in charCounter:
    #     if char not in counter:
    #         return False
    # return True

    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(joinSentence.lower()))
    
    

# print(findPangram('hello world'))
# print(findPangram('The quick brown fox jumps over the lazy dog'))

def findJadenCase(string):
    #receive a string
    #return the first letter of char in every word
    #ex: 'hello world' => 'Hello World'

    result = []

    for word in string.split():
        newWord = word[0].capitalize() + word[1:]
        result.append(newWord)
        result.append(" ")
    return ''.join(result)

# print(findJadenCase('hello world'))


def squareNum(n):
    #receive an integer
    #returned an integer where it's the squared products from num
    #ex: 142 => 184

    #intiailize a result array
    #iterate through string versions of them
    #flip them into integers and square it
    #add it to the result
    #return an int of the result

    result = []

    for num in str(n):
        squared = int(num) ** 2
        result.append(str(squared))
    return int(''.join(result))

# print(squareNum(9119))


#posting decimal values from 0 to 255
#outside of range must be rounded to the nearest valid number
#should be 6 chars long

# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"

def strogagrammatic(number):
    #receive an integer
    #return boolean if it is strobogrammatic (inverse)
    #ex: 69189 => 96186 =. False

    #iterate through it 
    #check if the number is the opposite of it
    #return false if any
    #otherwise, check all, return true

    inverse = { 
        '0': '0',
        '1':'1', 
        '6':'9',
        '8':'8',
        '9':'6'
    }

    strNum = str(number)
    left = 0
    right = len(strNum) - 1

    while left < right:
        print(inverse[strNum[left]])
        if strNum[left] not in inverse or strNum[right] not in inverse:
            return False
        if inverse[strNum[left]] != strNum[right]:
            return False
        left += 1
        right -=1 
    return True

    # invStr = []

    # for num in str(number):
    #     if num in inverse:
    #         invStr.append(int(inverse[num]))
    #     else:
    #         invStr.append(num)

    # left = 0
    # right = len(invStr) - 1

    # while left < right:
    #     if invStr[left] != invStr[right]:
    #         print(invStr[left], invStr[right])
    #         return False
    #     left += 1
    #     right -= 1
    # return True
# print(strogagrammatic(69189))
# print(strogagrammatic(6889))
        
def binSum(num):
    #receive an integer
    #return the sum of the binary representation of the number
    #ex: 10 => 2 (1010 => 1) longest 0
    binary = bin(num)[2:]
    max_gap = 0
    current_gap = 0

    for bit in binary:
        if bit == '0':
            current_gap += 1
        else:
            max_gap = max(max_gap, current_gap)
            current_gap = 0

    return max_gap

print(binSum(9))
print(binSum(529))

def is_digit(s):
    #receive an input
    #return a boolean if it is single whole number or a floating number
    #ex: 'h234' => False
    #ex: '3' => True
    #ex: '4.2' => True
    
    #convert what we have in S to be an integer
    #return true if single whole integer or else a floating number,
    #return False
    
    try:
        float(s)
        return True
    except ValueError:
        return False
    

    def show_sequence(n):
    #receive an integer (whole number)
    #return the sum of all numbers starting from 0 to n (inclusivee)
    #ex: 3 => 0 + 1 + 2 + 3 => 6
    #ex: -8 => 0
    
    #loop up to n
    #keep a running total and return the total
    
    if n < 0:
        return f"{n}<0"
    
    if n == 0:
        return "0=0"
    
    total = 0
    output = ''
    for num in range(0, n):
        output += str(num) + '+'
        total += num #0, 1, 3, 6
    return output + str(n) + ' = ' + str(total + n)
        
    
