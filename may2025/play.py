def caesarCipherEncryptor(string, key):
    # receive a string of lowercase letters, and an integer
    #return a new string for the new letter
    #ex: 'abc', 3 => 'def'

    #create a string of lowercase abc's
    #iterate through to find the index
    #add the key to the char
    #return new string

    alpha = ['a','b','c','d','e','f','g']
    output = []

    for char in string:
        newIdx = alpha.index(char) + key
        output.append(alpha[newIdx])
    return output
print(caesarCipherEncryptor('abc', 3))

def divisors(integer):
    #receive an integer
    #return the divisors that can get to the integer
    #ex: 9 => [3,3]
    
    #initialize a list output
    #take the integer mod every num up to it
    #starting at 2, since we can't include 1
    #if it has no remainder, add to the list
    #return list
    
    output = []
    for num in range(2, integer):
        if integer % num == 0:
            output.append(num)
    if not output:    
        return f"{integer} is prime"
    return output

        def duplicate_encode(word):
    #receive a string of lower and uppercase letters
    #return a string with '(' if new char else ')' for dupes
    #ex: 'new' => '((('
    
    #initialize a list
    #create a set
    #iterate through each char
    #check if set has it
    #if so, add a ')' else, add a '('
    #then add char to set
    #return the string back
    
#     output = []
#     uniqueChar = set(word.lower())

#     for char in word.lower():
#         if char not in uniqueChar:
#             output.append(')') #duplicate
#         else:
#             output.append('(') #unique
#         print(char, output, uniqueChar)
#     return ''.join(output)
    output = []
    dict = {}
    
    for char in word.lower():
        dict[char] = dict.get(char, 0) + 1
        
    for char in word.lower():
        if dict[char] > 1:
            output.append(')')
        else:
            output.append("(")
    return ''.join(output)

def remove_smallest(numbers):
    #receive a list of postivie integers
    #return a list back where the min element has been removed from earliest index
    #ex: [3, 2, 4, 5, 2] => [3, 4, 5, 2]
    #.  [ 2, 2,3, 4, 5] =>
    
    #initialize an empty list
    #find the min in numbers list
    #iterate through numbers to check if it is the number we are looking for
    #then don't add it to the list
    #otherwise, add the num into the numbers list
    #return the list
    
    if not numbers:
        return []
    
#     output = []
#     minNum = min(numbers)
#     for num in numbers:
#         if num != minNum:
#             output.append(num)
            
#     return output

    minNum = min(numbers)
    minIdx = numbers.index(minNum)
    return numbers[:minIdx] + numbers[minIdx+1:]
    
    def remove_smallest(numbers):
    copyNum = numbers[:]
    if copyNum:
        copyNum.remove(min(numbers))
    return copyNum

def sortStack(stack):
    # receive a list of elements
    #return a list of elements where it's sorted

    #create an empty list
    #iterate through the stack
    #add to list, sort it
    #then add it back to the empty list

    output = []
    for ele in stack:
        output.append(ele)

    output.sort()

    sorted_ele = []
    for ele in output:
        sorted_ele.append(ele)
    return sorted_ele

#time: O(n log n)
#space: O(n)

def sunsetViews(buildings, direction):
    # receive a list of integers of height and a string of uppercase letters
    #return the list of buildings that can see the sunset

    #if east, it can look right to see if sunset
    #else if west, it can look left to see if sunset

    #for east, start at the end, and look at next one below
    #check if it's greater than current one
    #if yes, append value
    #reverse it

    output = []
    maxApt = 0

    if direction == "EAST":
        for apt in range(len(buildings) -1, -1, -1):
            if buildings[apt] > maxApt:
                maxApt = buildings[apt]
                output.append(apt)
        return output[::-1]
    elif direction == "WEST":
        for apt in range(len(buildings)):
            if buildings[apt] > maxApt:
                maxApt = buildings[apt]
                output.append(apt)
        return output
    
def xor(a,b):
    #receive booleans
    #return True if one of the two expressions are true, else return False
    
    #ex: 'false', 'true' => 'true'
    #ex: 'true', 'true' => 'false'
    
#     if a == True and b == False:
#         return True
#     elif a == False and b ==True:
#         return True
#     else:
#         return False

    return False if a == b else True
return a !== b

def number(lines):
    #receive a list of items
    #return a list back wehre it's numbered
    
    #ex: [4,3, 2] => [1:4, 2: 3, 3: 2]
    
    #list comprehension
    #iterate through each element and add a to the index and the value 
    #return the list
    
    return [f"{idx + 1}: {ele}" for idx, ele in enumerate(lines)]

def alphabet_position(text):
    #receive a text of chars and symbols
    #return the position of alphabet n the char
    #ex: 'hello' => 
    
    #initialize an alphabet
    #lowercase the text
    #if text exists, add in the index value
    
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n', 'o','p','q','r','s','t','u','v','w','x','y','z']
    
#     output = []
#     for char in text.lower():
#         if char.isalpha():
#             output.append(str(alphabet.index(char) + 1))
#     return ' '.join(output)

    return ' '.join([str(alphabet.index(char) + 1) for char in text.lower() if char.isalpha()])

        
    def get_real_floor(n):
    # receive an integer (positive)
    #return an integer that represents the floor in the european system
    
    #ex: 1 => 0
    #ex: 2 => 2
    
    #ex:14 => 12
    #floors that are omitted = 1st, and 13th floor
    
    #anything less than 13 and greater than 0: floor - 1
    #6th -1 => 5th 
    #n > 13, take the total of n - 2
    
    #n = 8 => 7
    
    if n == 0:
        return 0
    elif n >= 1 and n < 13:
        return n -1
    elif n > 13:
        return n - 2
    
    #time: O(1)
    #space: O(1)
    
    
    def divisors(n):
    #receive an integer (represents the total)
    #return the count of how many numbers can divide into this integer 
    
    #ex: 3 => 2 => 1 and 3
    
    #initialize a count to 0
    #iterate up to n
    #check if each num % total is equal to 0
    #increment the count
    #return count
    
    if n == 0:
        return 0
    
    count = 0
    for num in range(1, n+1):
        if n % num == 0:
            count +=1
    return count
    
    #time:O(n)
    #space:O(1)
    
    #optimized solution: O(sqrt(n))
    #ex: 4
    #ex: sqroot of 4 = 2
    #ex: 12 => 
    #closest sqroot is 9, 3 (anything after 3 counts)