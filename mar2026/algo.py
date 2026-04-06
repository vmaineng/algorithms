def array_madness(a,b):
    #receive two list of integers
    #return boolean if squared list of a > squares list of b
    
    #find the sum squares of a
    #find the sum squared of b
    #return if  a > b
    
    squared_a = sum([num ** 2 for num in a])
    squared_b = sum([num ** 3 for num in b])
    
    print(squared_a, squared_b)
    
    return squared_a > squared_b

def fizzbuzz(n):
    #receive an integer
    #return a list back
    #ex: 
    
    
    #initialize an empty list
    #iterate up to n
    #check if % 3 and 5 => FizzBuzz
    #check if 3 => Fizz
    #if 5, buzz
    #else add in num 
    
    result = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            result.append('FizzBuzz')
        elif num % 5 == 0:
            result.append('Buzz')
        elif num % 3 == 0: 
            result.append('Fizz')
        else:
            result.append(num)
    return result

def high(x):
    #receive a string of lowercase chars
    #return the highest scoring word
    #ex: 
    
    #initialize a max amount to 0
    #initialize an empty max string
    #split the words
    #iterate through the words
    #check the total of the word
    #if it's greater than max, update max
    #return word we'v eseen so far
    
    letters = { 
    'a': 1, 
    'b': 2,
    'c':3,
    'd': 4, 
    'e': 5, 
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9, 
    'j': 10,
    'k': 11, 
    'l': 12,
    'm': 13,
    'n':14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26    
    }

    max_total = 0
    max_word = ""
    
    for word in x.split():
        total = 0
        for char in word:
            total += letters[char]
            
        if total > max_total:
            max_total = total
            max_word = word
    return max_word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #receive a list of words all lowercase letters
        #return the the top k words back in a list
        #ex: ['hello','hi','joee','hi', 'jill'] ,  k = 1 => ['hi']


        #iterate through the words and keep count of the occurence of word
        #initialize a max_heap, enter in the frequent amount and item connected to it
        #iterate up to k times and push the word into the result


        counter= {}
        for word in words:
            counter[word] = counter.get(word, 0) + 1
        
        max_heap = []
        for item, value in counter.items():
            heapq.heappush(max_heap, (-value, item))

        result = []
        for num in range(k):
            value, item = heapq.heappop(max_heap)
            result.append(item)
        return result
    
    def row_weights(array):
    #receive a list of positive integers
    #return back to a (sum of weight 1, sum of weight 2)
    #ex: [ 34, 23, 67, 3] => = (101, 26)
    #ex: odd = [23, 3]  = 26
    #ex: even = [34, 67] = 101
    
    #iterate through by idx
    #check if its even, add to the even running total
    #check if it's odd, add to the odd running total
    
    evenTotal = 0
    oddTotal = 0
    for idx, num in enumerate(array):
        if idx % 2 == 0:
            evenTotal += num
        else:
            oddTotal += num
    return (evenTotal, oddTotal)
                
                def count(s):
    #receive a string of characters
    #return back the counting pattern of them
    #ex: 'hello' => 
    #{
    #  'h': 1,
    #.  'e':1,
    #.  'l': 2,
    #    'o': 1
    #}
    
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1
    
    return counter
    
    import heapq

def kth_largest(numbers, k):
  #sort numbers
  #return the k'th kth_largest
  # sortedNums = sorted(numbers)
  # return sortedNums[-k]


  #intiitalize a heap
  #iterate through nums and add in to heap
  #if length of heap > k: pop off
  #iterate through heap
  #add into the result


  heap = []

  for num in numbers:
    heapq.heappush(heap, num)
    if len(heap) > k:
      heapq.heappop(heap)
  return heapq.heappop(heap)

  # result = []
  # while len(heap) > 0:
  #   item = heapq.heappop(heap)
  #   result.append(item)
  # return result[0]
  
  from collections import Counter

def anagrams(s1, s2):
  #receive two lowercase strings
  #return boolean if they are using same amount of chars
  #ex: 'hello', 'fishing' => false

  #edge case: if length are not the same, return false

  #brute force: sort both and check if they are the same
  #time: Onlogn and space: O(n)


  # sorteds1 = sorted(s1)
  # sorteds2 = sorted(s2)
  # return sorteds1 == sorteds2


  if len(s1) != len(s2):
    return False

  return Counter(s1) == Counter(s2)

def pair_sum(numbers, target_sum):
  #receive a list of integers
  #return a tupe of index positions that match up to target
  #ex: 

  #iterate through the numbers and check if values == 
  #each other, return the first tuple found



  for i in range(0, len(numbers)-1):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == target_sum:
        return (i,j)
      
      #time: O(n ^ 2)
  #space: O(1)


  #create an object to store the position of the values we've seen

  counter = {}
  for idx, num in enumerate(numbers):
    difference = target_sum - num
    if difference in counter:
      return (counter[difference], idx)
    counter[num] = idx
  
  def pair_product(numbers, target_product):
  #receive a list of integers
  #return in tuple


  # for i in range(0, len(numbers) -1):
  #   for j in range(i + 1, len(numbers)):
  #     if numbers[i] * numbers[j] == target_product:
  #       return (i, j)

  counter = {}

  for idx, num in enumerate(numbers):
    difference = target_product / num
    if difference in counter:
      return (counter[difference], idx)
    counter[num] = idx

    def intersection(a, b):
  #receive two lists of integers
  #return a list back of existing lists
  #ex: 

  # result = []
  # for num in a:
  #   if num in b:
  #     result.append(num)
  # return result

  # result = []
  uniqueA = set(a)
  # for num in b:
  #   if num in uniqueA:
  #     result.append(num)
  # return result

  result = [num for num in b if num in uniqueA]
  return result
    
  