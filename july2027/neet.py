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