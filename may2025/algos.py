def anagrams(s1, s2):
  #receive two strings
  #return True if anagrams if each other, else false
  #ex: 'hello', 'fish' => false
  #ex: 'elbow', 'below' => True

  #brute force: split, sort and compare if they are equal to each other
  # return sorted(list(s1)) == sorted(list(s2))
  #return sorted(s1) == sorted(s2)

  #create a dictionary for first string
  #iterate through the second string
  #subtract the values seen
  #if dictionary is empty, return True
  #else return false

  dict = {}
  for char in s1:
    if char not in dict:
      dict[char] = 0
    dict[char] += 1

  for char in s2:
    print(dict)
    if char not in dict:
      return False
    dict[char] -=1
    if dict[char] < 0:
      return False
  return True
    
print(anagrams('paper', 'reapa'))

def most_frequent_char(s):
  #receive a string of lowercase chars
  #return the most frequent letter most_frequent_ch
  #ex: 'hello' =>> 'l'

  #keep track of letters seend
  #if value is > max
  #update letter 

  letter = ''
  maxSeen = 0
  dict = {}
  for char in s:
    dict[char] = dict.get(char, 0) + 1
  for key,value in dict.items():
    if value > maxSeen:
      maxSeen = value
      letter = key
  return letter

def pair_product(numbers, target_product):
  dict = {}
  for idx, num in enumerate(numbers):
    divisor = target_product// num
    if divisor in dict:
      return (idx, dict[divisor])
    dict[num] = idx

    def intersection(a, b):
  #receive two lists
  #return a list that contain elements that exits in both lists
  #ex: [3,4,5,2], [6,7,2,1] => [2]

  #sort the elements in the lists
  #then have two pointers
  #time: O n log n
  #space: O(n)

  #create a dictionary
  #iterate through first list
  #add to dictionary
  #iterate through second list
  #check if it exists
  #add to list
  #then return the list

  dict = {}
  for char in a:
    dict[char] = dict.get(char, 0)

  result = []
  for char in b:
    if char in dict:
      result.append(char)
  return result

def intersection(a, b):
  #create a set for a
  #then check if the num exists in b
  result = []
  a_set = set(a)
  
  for num in b:
    if num in a_set:
      result.append(num)
  return result

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #receive a list of integers
        #return the length of longest increasing subsequence

        #ex: [0, 3, 4,6,7,8,] => [3,4,6,7,8]

        #sort the list of array
        #initialize a count
        #iterate through the second numbs
        #check if prev nums = -1
        
        maxCount = 0
        sortList = sorted(nums)

        for i in range(1, len(nums) -1):
            if nums[i - 1] == nums[i] + 1:
                maxCount += 1
        return maxCount
      
      class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = []

        def binary_search(result, n):
            left = 0
            right = len(result) - 1
            while left <= right:
                middle = (left + right) // 2
                if result[middle] == n:
                    return middle
                elif result[middle] > n:
                    right = middle - 1
                else:
                    left = middle + 1
            return left
            
        for n in nums:
            if not result or result[-1] < n:
                result.append(n)
            else:
                idx = binary_search(result, n)
                result[idx] = n
        return len(result)
    
    def people_with_age_drink(age):
    #receive an integer
    #return a string of what they can drink
    #ex: 3 => "drink toddy"
    #ex: 14 => "drink coke"
    
    if age < 14:
        return "drink toddy"
    elif age >= 14 and age < 18:
        return "drink coke"
    elif age >= 18 and age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    
    def binary_array_to_number(arr):
  #receive an array of integers
#return the binary number of number

#ex join the digits together
#convert it using bin function

    binNum = [str(ele) for ele in arr]
    binStr = ''.join(binNum)
#     print(binStr)
    return int(binStr, 2)

def solution(a, b):
    #receive two strings of upper, lower, and numbers, and chars
    #return a string - that holds short form and long form
    #ex: 'yo', 'sa8' => 'yosa8yo'
    
    #find the smaller length of a and b
    #add it to the result array
    #then add in the other string
    # or vice versa
    
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

def number(bus_stops):
    # receive a list of lists of [get on bus, get off bus]
    #return num of people who left on bus
    
    #initialize a count
    #destructure out people who get on and people who get off bus
    #subtract and add from total
    #return total
    count = 0
    for stop in bus_stops:
        peopleOn, peopleOff = stop
        count += peopleOn
        count-= peopleOff
    return count
    
    return sum([stop[0] - stop[1] for stop in bus_stops])

def spin_words(sentence):
    #receive a sentence of uppercase and lowercase chars
    #return a string back that if the word has 5 or more letters, it needs to be reversed back in string
    #ex: 'apples are my favorite' => 'selppa are my etirovaf'
    
    #initialize an array
    #split the sentence by words
    #check the length of the word
    #if len > 5, reverse it, then add it to the array
    #else add word to the array
    #join it back
    
    result = []
    splitWords = sentence.split(" ")
    for word in splitWords:
        if len(word) >4:
            result.append(word[::-1])
        else:
            result.append(word)
    return ' '.join(result)

#time: O(n)
#space:O(n)

    return ' '.join([word[::-1] if len(word) >4 else word for word in sentence.split("")])

return list(range(integer, limit+1, integer))

def find_multiples(integer, limit):
    #receive an integer, and another integer
    #return a list of multiples up to limit
    #ex: 3, 6 => [3, 6]
    
    #initialize an empty list
    #iterate up to limit, starting at n
    #check if the currentNum mod integer == 0, add it the list
    
    return [num for num in range(integer, limit + 1) if num % integer == 0]

#find the next multiple

def odd_or_even(arr):
    #receive a list of integers
    #return string of 'odd' if total is odd, or 'even'
    #ex: [0,2,3] => 5 => 'odd'
    
    #add up the total of integers
    #check if total % 2 == 0, return even, else odd
    
    return 'odd' if sum(arr) % 2 == 1 else 'even'

def move_zeros(lst):
    #receive a list of integers
    #return the same list back with 0's move to the end of the array
    #ex: [1,0, 2, 3,0] => [1,2,3,0,0]
         #l
           #r
    
    
    #[1, 2, 1, 1, 0, 1, 0, 3, 0, 0]
                            # l
                         #.r
    #two pointers
    #start on first one
    #start on second, check if they are a 0
    #return list
    
#     left = len(lst) - 1
#     right = len(lst) - 1
    
#     while right >= 0:
#         if lst[right] != 0:
#             right -= 1
#         else:
#             lst[left], lst[right] = lst[right], lst[left]
#             left = right
#             right -= 1
#     return lst

#     left = 0
#     right = len(lst) -1
    
#     while left < right:
#         while left < right and lst[right] == 0:
#             right -= 1
#         if lst[left] == 0:
#             lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#     return lst

def fix_the_meerkat(arr):
    #receive a list of of values of tail, body, and head
    #return the correct order of head, body, and tail back in list
    return arr[::-1]

def series_sum(n):
    # receive an integer
    # return the n-th term of the seequence added
    
    #series: 1/7 = .14 + the previous number
    #recursively
    #if n: return couunt
    #keep adding 1/7 + 1/10
    
    if n == 0:
        return "0.00"
    
    
    total = 0.00
    denominator = 1
    
    for i in range(1, n + 1):
        total += 1 / denominator
        denominator += 3
    return f"{total:.2f}"

def count_bits(n):
    #receive an integer
    #return the 1's in the binary #
    
    #convert the n to a binary number
    #iterate through the binary number
    #check if it is a 1
    #return count
    
    binNum = bin(n)[2:]
    lstNum = list(binNum)
    count= 0
    
    for num in lstNum:
        if num == '1':
            count += 1
    return count

'Oay emporatay oay oresmay !ay' should equal 
'Oay emporatay oay oresmay !'

def pig_it(text):
    ##receive a string of texts with uppper and lowercase chars
    #return the pig lating version of the words
    
    #ex: 'hello world' => 'ellohay orldway'
    
    #split on spaces of the word
    #take each word
    #split out starting from first index
    #add the first letter at the end of word + 'ay'
    #add it back together in an list
    #return the list back join
    
    output = []
    newWord = ""
    
    splitStrings = text.split(" ")
    for word in splitStrings:
        if word.isalpha():
            newWord = word[1:] + word[0] + 'ay'
            output.append(newWord)
        else:
            output.append(word)
    return ' '.join(output)

    
    def spiralTraverse(array):
    #receive a 2D list
    #return the spiral shape of the 2D

    #initialize an output array
    #iterate through rows, right, bottom, left

    output = []
    rows, endRows = 0, len(array) -1
    cols, endCols = 0, len(array[0]) -1

    while endRows <= endCols and rows < cols:
        for col in range(row, array[cols]):
            output.append(array[row][col])
        rows +=1

        for row in range(cols, endCols):
            output.append(array[row][col])
        endCols -=1

        for row in range(endCols, cols, -1):
            output.append(array[row][col])
        endRows += 1

        for row in range(col, rows):
            output.append(array[row][cols])
        col += 1

     
def caesarCipherEncryptor(string, key):
    # receive a string of lowercase letters, and an integer
    #return a new string for the new letter
    #ex: 'abc', 3 => 'def'

    #create a string of lowercase abc's
    #iterate through to find the index
    #add the key to the char
    #return new string

    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    output = []

    for char in string:
        newIdx = (alpha.index(char) + key) %26
        output.append(alpha[newIdx])
    return ''.join(output)