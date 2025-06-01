geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
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
    return [name for name in birds if name not in geese]

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
    
    dictionary = {}
    
    for num in arr: 
        dictionary[num] = dictionary.get(num, 0) + 1
    
    for [key, value] in dictionary.items():
        if dictionary[key] == 1:
            return key
        
    #time: O(n) => n amount in list to traverse through
    #space: O(n) => n integers to be stored in the dictionary
    
    