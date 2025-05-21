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