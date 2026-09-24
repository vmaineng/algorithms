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

    """
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)


        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]
            if prev.end > curr.start:
                return False
        return True

def correct_polish_letters(st): 
    #receive a string of upper and lowercase chars
    #return the string baack with no diacritics
    #ex: 'Jóe Mąry' => 'Joe Mary'

    diacritics = { "ą": "a",
"ć": "c",
"ę": "e",
"ł":"l",
"ń":"n",
"ó":"o",
"ś":"s",
"ź":"z",
"ż":"z"
    }
    
    #iterate through the string
    #find the char that is diacritics
    #replace it with the Engnlish char
    #return the string back
    
    result = []
    for char in st: #J, o, e
        if char in diacritics:
            result.append(diacritics[char]) #['J', 'o']
        else:
            result.append(char) #['J'], #['J', 'o', 'e']
    return ''.join(result) #'Joe'
    
def most_frequent_item_count(collection):
    #receive a list of integers
    #return the max freqeuent element seen (an integer)
    #ex: [1,3,2,2,4,6] => 2
    
    #create a hash map
    #iterate through each integer
    #if the key is not in here, we are going to create key, and incrment it one
    #iterate through the object later
    #check the values to see which one is the max, we will return the key
    
    if not collection:
        return 0
    
    seen_val = {}
    
    for num in collection:
        seen_val[num] = seen_val.get(num, 0)+ 1
        
    max_count = 0
    frequent_int = 0
    
    for key,val in seen_val.items():
        if val > max_count:
            max_count = val
            frequent_int = key
    return max_count
            
def highest_rank(arr):
    #receive a list of integers
    #return back an integer of the highest occurences or if tie, return highest number
    #ex: [3,3,3,4,4,4,5,2] => 3, 4 => 4 
    #ex: [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]), 12)
    #{10: 2}
    #{12, 2} => 
    
    seen_val = {}
    for num in arr:
        seen_val[num] = seen_val.get(num, 0) + 1
        
    max_count = 0
    max_val = 0
    
    for key,val in seen_val.items():
        if val > max_count:
            max_count = val
            max_val = key
        elif val >= max_count:
            max_count = val
            max_val = max(key, max_val)
    return max_val

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #receive a class of in list of (start, end)
        #return boolean
        #ex: 

        intervals.sort(key=lambda x:x.start)

        for i in range(1, len(intervals)):
            curr = intervals[i]
            prev = intervals[i- 1]
            if prev.end > curr.start:
                return False
        return True


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #receive a list of intervals
        #return the list where the newInterval is added in
        #ex: 

        #sort by start
        #check if prev.end > curr.start
        #merge them in together, update the end time to curr.end
        #add to the list of result

        intervals.sort(key=lambda x:x[0])

        result = []

        for i in range(len(intervals)): 
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        result.append(newInterval)
        return result

def reverse_number(n):
    #receive an integer
    #return an integer back where the numbers are reversed
    #ex: -54 => -45, 4 => 4
    #ex: 100 => 1
    
    #conver integer into string
    #iterate through the string
    #reverse them
    #add them back together
    #if the integer starts with 0, don't add in
    #if negative, leave negative in the beginning
    
    if len(str(n)) == 1:
        return n
    
    result = []
    strNum = str(abs(n))
    
    for item in range(len(strNum)-1, -1, -1):
        if strNum[item] == '0':
            continue
        else:
            result.append(strNum[item])
    
    strOutput = ''.join(result)
    
    if n < 0:
        return int('-'+ strOutput)
    else:
        return int(strOutput)

            class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0]> intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval=[
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        result.append(newInterval)
        return result
        
        def wave(people):
    #receive a word
    #return back the word where the items are uppercase
    #ex;
    
    #create a result
    #iterate through
    #uppercase the letter at idx
    #iterate add in the rest of the letter
    #add to result
    
    result = []
    
    for i in range(len(people)):
        if people[i] == " ":
            continue
        word = ''
        for j in range(len(people)):
            if i == j:
                word += people[j].upper()
            else:
                word += people[j]
        result.append(word)
    return result

                def incrementer(nums):
    #receive a list of integers
    #return a list where each integer is added by the index position in their role
    #ex: [2,3] =>[2+ 1, 3+2] => [3,5]
    
    result = []
    for num, idx in enumerate(nums):
        pos = num + (idx + 1)
        if pos > 9:
            new_pos = pos % 10
            result.append(new_pos)
        else:
            result.append(pos)
    return result

def stock_list(stocklist, categories):
    #receive a stock list of strings
    #return a string of categories and amount associated with it
    
    #ex:
    
    #iterate through the bookseller's stocklist starting at the first letter
    #split stocklist = [name, amount]
    #iterate through the categories
    #check the first lietter in stocklist
    #find the total
    #add total together
    
    result = []
    
    for category in categories:
        total = 0
        for item in stocklist:
            name, quantity = item.split()
            if category == name[0]:
                total += int(quantity)
        result.append( f"({category} : {total})" )
    return ' - '.join(result)

            import math

def dating_range(age):
    #receive an integer
    #return a range of string of integers
    #ex: 
    
    if age <= 14:
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    else:
        min_age = math.floor(age /2) + 7
        max_age = math.floor(2 * (age - 7))
    
    return f"{min_age}-{max_age}"

def vaporcode(s):
    #receive a string of letters and spaces
    #return a new string where chars are all uppercases and two spaces between
    #ex: "hello" => 'H  E  L  L  O'
    
    #intialize a result list
    #iterate through the string
    #capitalize the letter
    #add it to the result along with two spaces
    #if its a space, continue
    #return list as string
    
    result = []
    
    for char in s:
        if char == ' ':
            continue
        else:
            new_char = char.upper()
            result.append(new_char)
    return '  '.join(result)

return "  ".join(char.upper() for char in s if char != ' ' )

def multiplication_table(size):
    #receive an int of size
    #return a mxn grid
    #ex: 2 => 
    #[1, 2] X1, starts with 1
    #[2, 4] X 2 starts with 2
    
    #start row and col starting from 1 up to the integer
    #then iterate through the integer until we reach 2
    #multiply them by 2
    
    result = []
    
    for row in range(1, size + 1):
        new_result = []
        for col in range(1, size + 1):
            val = row * col
            new_result.append(val)
        result.append(new_result)
    return result
            
        
        
        
    