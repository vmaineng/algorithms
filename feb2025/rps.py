def rps(p1,p2):
    #
    pairs = { 
        'scissors': 'paper', 
        'paper': 'rock',
        'rock': 'scissors'
    }
    #return 'Player 2 won!' if pairs[p1] == p2 elif 'Player 1 won!' else 'Draw!'

#scissors > paper, paper > rock, rock > scissors 

    if pairs[p1] == p2: #scissors == 'rock'
        return 'Player 2'
    elif pairs[p2] == p1: #rock == scissors
        return 'Player 1'
    else:
        return 'Draw!'

print (rps('paper','scissors'))
#            p1,   p2

#output: scissors > paper => p2

#time: O(1)
#space: O(1)