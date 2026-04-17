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

print(findJadenCase('hello world'))