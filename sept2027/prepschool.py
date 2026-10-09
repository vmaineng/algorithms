#splits a string into strings of two chars into array
#if string contains odd, missing second char will have an underscore it

#parameter:can be lowercase or uppercase characters, no spaces
#return: a list of two chars, but if it's odd, then the second char will have underscore
#ex: 'hello' => ['he', 'll', 'o_']
#ex: 'star' => ['st', 'ar']
#ex: ''=> []

#at least one character

#iterate word
#calc even or odd for the string,
#concat '_' at the end of the last digit if odd
#create an empty string; slice up to two characters at the same time
#add in two characters at a time
#push in the pair in the final result

# if len(word) % 2 == 0
#'a'

def splitPairs(word): 
    result = []

    if len(word) % 2 != 0:
        word = word + '_'

    for idx in range(0, len(word), 2): #hello_
        pair = word[idx: idx+2] #'he', 'll', 'o_'
        result.append(pair) #['he', 'll', 'o_']

    return result

print(splitPairs('hello'))
print(splitPairs('star'))
        
