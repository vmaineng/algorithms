#DNA

#DNA strings = A & T => complements of each other
#C & G complements of each other

#receive a string 
#return the other side
#it's never empty, or no DNA at all

#length of DNA will be at least 2
#ex: 'ATTCG'=> 'TAAGC'
#all in uppercase

#INTIIALIZE KEY OBJECT: A: T, T:A, C : G, G:
#iterate the string, find key, retrieve the value
#add the result string, and be able to return the result string

def complementDNA(text):
    key = { 
        'A': 'T',
        'T':'A',
        'C':'G',
        'G':"C"
    }

    result = ''
    for char in text:
        if char in key:
            result += key[char]
    return result
print(complementDNA('ATTCG'))