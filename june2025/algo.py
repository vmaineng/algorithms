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