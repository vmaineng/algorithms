def compress(s):
    # receive a string of lower and upper letters
    # return the compressed vversion of a string
    # ex: 'aaabba' => '4a2b'

    # create a list
    # push in count of letters seen
    # else start new and refresh count

    #brute force:
 
    if not s:
        return ""

    # result = []
    # count = 1

    # for i in range(len(s) - 1):

    #     if s[i] == s[i + 1]:
    #         count += 1
    #     else:
    #         result.append(f"{count}{s[i]}")
    #         count = 1
    # result.append(f"{count}{s[-1]}")

    # return "".join(result)

    s += '!'
    result = []
    i = 0
    j = 0

    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            if num == 1:
                result.append(s[i])
            else:
                result.append(str(num))
                result.append(s[i])
            i = j
    return ''.join(result)


print(compress('aaabb'))

class Solution:

    def encode(self, strs: List[str]) -> str:
        #shorter version of the string
        #"neet#code#love#you"
        #'4neet4code4love3you'
        
        #ex: ['hi', '3hi', 'bye']
        #=> '2hi33hi3bye'
        #=> '2hi#33hi#3bye'
        #.   i 
        #.      j
        # => ['hi',]
        #.      j
        #        i
        #            j
        #use substring from i to j ; (j - i) + 1 = length of what we need

    def decode(self, s: str) -> List[str]:
        #take shorter version and expand
        #['neet', 'code','love','you']
        #create a result array
        #iterate through string until reach '#'
        #everything before #, add to the array

def dna_to_rna(dna):
    #receive a string of chars
    #return a string where the T turns into a U
    
    #ex: 'CGTA' => 'CGUA'
    
    #for each letter, check if T
    #replace letter T for U
    
    return dna.replace('T', 'U')

    def bmi(weight, height):
    #receive two integers
    #return an output of word based on bmi
    
    #calc the bmi of weight / height^2
    #check if bmi is <= 18.5, return 'Underweight'
    #if bmi <= 18.5 and bmi <= 25, return "Normal"
    
    bmi = weight/height**2
    
    if bmi <= 18.5:
        return 'Underweight'
    elif bmi > 18.5 and bmi <= 25:
        return 'Normal'
    elif bmi >25 and bmi <= 30:
        return 'Overweight'
    else:
        return "Obese"

def DNA_strand(dna):
    # receive strings
    #return a new string where A have converted to T and C are converted to G
    
    #ex: 'GGG' => 'CCC'
    
    #check each char if it is G => turn to a C
    #check if each char is aT => turn to a A
    
    result = []
    
    for char in dna:
        if char == 'A':
            result.append('T')
        elif char == 'T':
            result.append('A')
        elif char == 'G':
            result.append('C')
        elif char == 'C':
            result.append('G')
        else:
            result.append(char)
    
    return ''.join(result)

    pairs = { 
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C':'G'
    }

    return ''.join([pairs[x] for x in dna])

    def rps(p1, p2):
    #receive a string of 'scisssors', 'paper', and 'rock'
    #return which player won or a draw
    #ex: rps('paper', 'paper') => draw
    #ex: rps('paper', 'rock') => 'paper'
    
    #brute force:
    #conditional checks:
    #if p1 == 'scissors' && p2 == 'paper'
    #return "Player 1 won!"
    
    #scissors > paper
    #paper > rock
    #rock > scissors
    
    if p1 == 'scissors' and p2 == 'paper':
        return 'Player 1 won!'
    elif p1 == 'paper' and p2 == 'rock':
        return 'Player 1 won!'
    elif p1 == 'rock' and p2 == 'scissors':
        return 'Player 1 won!'
    elif p2 == 'rock' and p1 == 'scissors':
        return 'Player 2 won!'
    elif p2 == 'paper' and p1 == 'rock':
        return 'Player 2 won!'
    elif p2 == 'scissors' and p1 == 'paper':
        return 'Player 2 won!'
    else:
        return 'Draw!'
    
#     if p1 == 'scissors'and p2 =='paper':
#         return 'Player 1 won!'
#     elif p1 == 'rock' and p2 == 'scissors':
#         return 'Player 1 won!'
#     elif p1 == 'scissors' and p2 == 'rock':
#         return 'Player 2 won!'
#     elif p1 == 'paper' and p2 == 'rock':
#         return 'Player 1 won!'
#     else:
#         return 'Draw!'
    
#     pairs = {
#         'scissors':'paper'
        
#     }