class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0,0)}
        x=y= 0
        for way in path:
            if way == 'N':
                y += 1
                
            elif way == 'E':
                x += 1
                
            elif way == 'S':
                y-= 1
                
            else:
                x-=1
               

            if (x,y) in visited:
                return True
            visited.add((x,y))
            
        return False
        
        def vowel_indices(word):
	#receive a string of letters
    #return vowels index in a list
    
    #ex: 
    
    result = []
    vowels = 'aeiouy'
    
    for i, char in enumerate(word.lower()):
        if char in vowels:
            result.append(i + 1)
    return result

def in_array(array1, array2):
    #receive a list of two lists of lowercase letters
    #return a list back that are substrings of the string in 2
    #ex: 
    
    #iterate through the list of strings
    #check if in a1 exists in a2
    #add to the result list
    #return result list sorted
    
    result = set()
    for word in array1:
        curr = word
        for word2 in array2:
            if curr in word2:
                result.add(curr)
                break
    return sorted(result)