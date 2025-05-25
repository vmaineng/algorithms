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