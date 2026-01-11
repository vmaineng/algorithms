def uncompress(s):
    #receive a string
    #return a string back with the count of occurrences for each character
    #ex: '3a2b' => 'aaabb'
    #.    i
    #.     j

    #using two pointers, i && j
    #i stays on the number, and j will increment and find the char
    #iterate through the string
    #if j is not a number
    #add in the amount of letters into the list
    #increment j
    #increment i pointer to where j
    #return the result

    i = 0
    j = 0
    result = []
    numbers = '0123456789'

    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(num * s[j])
            j+=1
            i = j
    return ''.join(result)

# print(uncompress('3a2b'))

#time: O(n)
#space:O(n)

def compress(s):
    #receive a string of lowercase letters
    #return the compressed version with the count of letters next to the character
    #ex: 'aaabbb!' => '3a3b'
    #     i
    #.       j
    #.    012345

    #i and j starting at 0
    #j keeps incrementing until a new letter has been found
    #take the j index - i index * old letter on i
    #move i to j's position 
    
    s += '!'
    i = 0
    j = 0
    result = []

    while j < len(s):
        if s[j] == s[i]:
            j += 1
        else:
            count = j - i
        
            result.append(f"{count}" + s[i])
            i = j

        # if s[j] != s[i]:
        #     count = j - i
        #     result.append(f"{count}" + s[i])
        #     j += 1
        #     i = j
        # else:
        #     j += 1

    return ''.join(result)

print(compress('aaabbb'))

#time: O(n)
#space: O(n)







