def createTree(str):
    #receive an integer, return a level tree with * 
    #return a string with the tree
    #n = 3
    #[ ' *  ', ' *** ', '*****' ]

    #result
    #add in a string

    result = []

    for i in range(1, str+1):
        row = ' ' * (str - i) + '*' * (2 * i - 1) + ' ' * (str - i)
        result.append(row)
    return result

# print(createTree(3))

#given a string of wrods, 
#return highest scoring words as a string
#each letter corresponds points in alphabet
#a = 1
#b= 2

#receive a string of words (lowercase), no extra special chars
#return the string of max highest score word
#ex: 'ab bab' => 3, 5 => 'bab' 
#ex: 'bob bob' => 'bob'

#length > 1

# initialize a count, an empty string to hold the longest word 
# iterate through each word
#count the score for each character
#chr('a') - 97 = 1 or ord() 
#keep track of the longest score seen
#then update the longest word and we will return the longest word

def highest_score(str):
    longest_word = ''
    longest_count = 0

    words = str.split(" ") #['bab', 'ab']

    for word in words: #'bab', 'ab'
        count = 0
        for char in word: #'b', 'a', 'b' , 'a', 'b'
            count += ord(char) - 97 #2 + 1 + 2 => 5; 1 + 2 => 3
        if count > longest_count: # 5 > 0, 
            longest_count = count # 5
            longest_word = word #'bab'

    return longest_word #'bab'

print(highest_score('ab bab'))
print(highest_score('bob bob'))
print(highest_score('ab bab ab'))

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #receive a list of integers
        #return the weight of the last remaining stone
        #ex: 

        #implement a max heap of the stones
        #pop off the top two
        #add in the new weight
        #until len of heap is 1 or none

        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            new_weight = first - second
            if new_weight < 0 :
                heapq.heappush(stones, new_weight)

        return -stones[0] if len(stones) > 0 else 0

