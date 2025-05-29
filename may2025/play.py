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
    
