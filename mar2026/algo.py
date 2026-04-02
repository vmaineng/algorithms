def array_madness(a,b):
    #receive two list of integers
    #return boolean if squared list of a > squares list of b
    
    #find the sum squares of a
    #find the sum squared of b
    #return if  a > b
    
    squared_a = sum([num ** 2 for num in a])
    squared_b = sum([num ** 3 for num in b])
    
    print(squared_a, squared_b)
    
    return squared_a > squared_b

def fizzbuzz(n):
    #receive an integer
    #return a list back
    #ex: 
    
    
    #initialize an empty list
    #iterate up to n
    #check if % 3 and 5 => FizzBuzz
    #check if 3 => Fizz
    #if 5, buzz
    #else add in num 
    
    result = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            result.append('FizzBuzz')
        elif num % 5 == 0:
            result.append('Buzz')
        elif num % 3 == 0: 
            result.append('Fizz')
        else:
            result.append(num)
    return result

def high(x):
    #receive a string of lowercase chars
    #return the highest scoring word
    #ex: 
    
    #initialize a max amount to 0
    #initialize an empty max string
    #split the words
    #iterate through the words
    #check the total of the word
    #if it's greater than max, update max
    #return word we'v eseen so far
    
    letters = { 
    'a': 1, 
    'b': 2,
    'c':3,
    'd': 4, 
    'e': 5, 
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9, 
    'j': 10,
    'k': 11, 
    'l': 12,
    'm': 13,
    'n':14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26    
    }

    max_total = 0
    max_word = ""
    
    for word in x.split():
        total = 0
        for char in word:
            total += letters[char]
            
        if total > max_total:
            max_total = total
            max_word = word
    return max_word