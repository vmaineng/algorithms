# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# def goose_filter(birds):
    #receive a list of string of birds
    #return a filter list where all of the 'geese' animals are removed
    #ex: ['Pig', 'Pilgrim', 'Penguin'] => ['Pig', 'Penguin']
    
    #intitialize an empty list
    #iterate through all the bird names in the bird list,
    #check to see if their name is not in geese's list
    #add to empty list
    #return the list back
    
    #list comprehension
    #return nameofBird if bird is not in the geese list
    #return [name for name in birds if name not in geese]

#time: O(n)
#space: O(n)    

def stray(arr):
    #receive a list of integers
    #return an integer that is the odd one out
    #ex: [3,3,3,3, 2] => 2
    
    #initialize an empty dictionary
    #iterate through all the numbers in the list
    #increment the count that we see for each value
    #check which value has a count of 1 - it showed up once
    #return the num
    
    # dictionary = {}
    
    # for num in arr: 
    #     dictionary[num] = dictionary.get(num, 0) + 1
    
    # for [key, value] in dictionary.items():
    #     if dictionary[key] == 1:
    #         return key

    # for idx in range(1, len(arr)):
    #     if arr[idx] != arr[idx -1]:
    #         return arr[idx]
        
    #time: O(n) => n amount in list to traverse through
    #space: O(n) => n integers to be stored in the dictionary

    a = arr[0]
    b = None

    for idx in range(1, len(arr)):
        if arr[idx] != a:
            b = arr[idx]
    return b
    
print(stray([3,2,2,2]))
print(stray([2,2,2,3]))
         #  idx-1
         #    idx

#maxValue = first number; stray[0]
#traverse through
#keep track of the num I've seen
#if you are a new number, you are Odd one out
#return the num we are looking at

def persistence(n, count = 0):
    # receive an integer
    #return back an integer of the count of how many times to multiply the number until it becomes one
    #number
    
    #ex: 39 => 3 * 9 => 27 => 2 * 7 => 14 => 1 * 4 => 4 => return back 3
    
    #base case: 
    #if it's single digit
    #len == 1
    
    #recursive call
    #split the digits and multiply them together
    #keep track of count
    
#     count = 0
    
    if n < 10:
        return count
    
    total = 1
    for digit in str(n):
        total *= int(digit)
    return persistence(total, count + 1)
    
    
    def is_valid_walk(walk):
    #receive a list of lowercase letters representing directions
    #return boolean to see if we can walk in the meantime and return back to original position
    
    #ex: ['n','s','n','s','n','s','n','s','n','s'] = 0
    #1 letter= 1 min
    #return back to your original position
    
   #ex: ['w','e','w','e','w','e','w','e','w','e','w','e'] = 0
  #count:1.  -1  1   -1   1
    #total.  0    1    0
    
    #keep count of blocks ; initialize it to 0
    #once we move away, we add to count
    #if we come back, we minus from count
    #if we go N, add one
    #if we come back down south, - one
    #if we east, add one, if we go west -one
    
    if len(walk) > 10:
        return False
    
#     blocks = 0
#     currentPosition = 0
    
#     direction = { 
#         'n': 1,
#         's': -1, #n and s are opposite, 
#         'e': 1, #e and w are opposite
#         'w': -1
#     }
    
#     for char in walk:
#         if direction[char]:
#             blocks += direction[char]
#             print(blocks)
#     return blocks == currentPosition

    if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(walk) == 10:
        return True
    else:
        return False
    
    

def name_shuffler(str_):
    #receive a string of of two words
    #return the name swapped
    #ex: 'mary joe' => 'joe mary'
    
    splitName = str_.split(" ")
    return ' '.join(splitName[::-1])

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for char in s: #closing bracket
            if char in brackets:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack

     class Solution:
    def isValid(self, s: str) -> bool:
        #receive a string of opening and closing parens
        #return True if matching, else False
        #ex: ')()' => False

        #initialize an empty stack
        #iterate through char
        #check to see if it is a closing bracket
        #then check if stack's not empty and the last one is an opening that matches
        #then pop it off
        #else return False
        #else it is an opening, add to stack
        #return if stack's empty

        stack = []

        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in brackets:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
    def bestDigits(number, numDigits):
    # receive a string of integers
    #return the biggest number from the string of integers

    #ex: '342', 1 => '42'

    #iterate each num
    ##initialize a stack
    #check if the stack is not empty
    #and that the new number is greaterthan previous


    stack = []
    for num in number:
        while numDigits > 0 and len(stack) >0 and num > stack[len(stack) - 1]:
            numDigits -=1
            stack.pop()
        
        stack.append(num)

     while numDigits > 0:
        numDigits -=1
        stack.pop()
    return ''.join(stack)
def spiralTraverse(array):
    output = []

    startRows, endRows= 0, len(array)-1
    startCols, endCols = 0, len(array[0]) -1

    while startRows <= endRows and startCols <= endCols:
        for col in range(startCols, endCols + 1):
            output.append(array[startRows][col])
        startRows += 1

        for row in range(startRows, endRows + 1):
            output.append(array[row][endCols])
        endCols -= 1

        if startRows <= endRows:
            for col in range(endCols, startCols -1, -1):
                output.append(array[endRows][col])
            endRows -= 1

        if startCols <= endCols:
            for row in range(endRows, startRows -1, -1):
                output.append(array[row][startCols])
            startCols += 1

    return output

def sortStack(stack):
    # receive a list of integers
    #return the integers sorted using a stack

    #look at the top number
    #compare to the num i popped off
    #check if it's less

    #initialize a helperStack to hold values
    #stack keeps original sorted list

    helperStack = []

    while len(stack) > 0:
        temp = stack.pop()
        # helperStack.append(temp)

        while len(helperStack) > 0 and temp > helperStack[len(helperStack) -1]:
            stack.append(helperStack.pop())
    while len(helperStack) > 0:
        stack.append(helperStack.pop())
    return stack
    
def divisible_by(numbers, divisor):
    #receive a list of integers, and an integer
    #return a list where the num is divisible by the numbers in the list
    
    return [num for num in numbers if num % divisor == 0]

def solution(nums):
    #receive a list of integers
    #return the nums sorted in the list
    
    return sorted(nums) if nums else []

def pipe_fix(nums):
    #receive a list of integers
    #return a list where every num is included 
    
    return [num for num in range(nums[0], nums[-1] + 1)]

def arithmetic(a, b, operator):
    #receive integers
    #return the operation of a and b contingent on operator
    
    if operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a- b
    elif operator == 'multiply':
        return a * b
    else:
        return a/b
    
    def unique_in_order(sequence):
    #receive a string of integers or chars
    #return a list back where the same values are not next to it
    
    #intiialize an empty list
    #iterate through the sequence to check if the values are the same
    #then move the pointer if they are the same
    
    if not sequence:
        return []
    
    output = [sequence[0]]
    i = 0
    
    for item in range(1, len(sequence)):
        if sequence[item] != sequence[i]:
            output.append(sequence[item])
        i = item
    return output

def firstNonRepeatingCharacter(string):
    # receive a string of lowercase letters
    #return the index of first non-repeating char

    #ex: 'hello' => 0 'h'

    #iterate through the chars
    #kept track of how many chars seen
    #check to see if char has an occurence of 0

    dict = {}
    for char in string:
        dict[char] = dict.get(char, 0) + 1

    for i, char in enumerate(string):
        if dict[char] == 1:
            return i
    return -1

    # #set
    # #iterate through the string
    # #check if set already has char, 
    # #if so, delete, else add
    # #return the index position of what set has left

    # uniqueChar = set()
    # for char in string:
    #     if char not in uniqueChar:
    #         uniqueChar.add(char)
    #     else:
    #         uniqueChar.remove(char)
    # uniqueItem = string.index(uniqueChar[char])
    
