#friend or foe
#filters a list of strings

#if name has 4 letters == friend, else foe

#input = a list of strings
#output = a list of strings that are friends that has a length of 4
#ex: ['Mai', 'Kyle', 'Eric', 'Amanda'] => [ 'Kyle', 'Eric' ]

#[] => []
#[34, ] => always be strings only
#['Mai']
#with names longer than 4=> []

#initalize an empty list
#iterate through the input string
#check the length of name == 4
#add it to our empty list
#return the result list of names == 4

def friendOrFoe(array):
    result = []
    for name in array:
        if len(name) == 4:
            result.append(name)
    return result

# print(friendOrFoe(['Mai', 'Kyle', 'Eric', 'Amanda']))
# print(friendOrFoe(['Mai', 'Kye', 'Ric', 'Amanda']))

def sheepCount(array):
    # count = 0
    # for sheep in array:
    #     if sheep == True:
    #         count += 1
    # return count 
    return sum(sheep is True for sheep in array)

# print(sheepCount([True, False, False]))

def moveZeros(array):
    #receive a list of integers, false, and 0
    #return the list back where 0's move at the end
    #ex: 

    #create two pointers and i at beginning and j at the end

    i = 0 
    j = len(array) - 1

    while i < j:
        if array[i] == 0 and array[j] != 0:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -=1
        elif array[j] == 0:
            j -= 1
        else:
            i += 1
    return array

# print(moveZeros([False,1,0,1,2,0,1,3,"a"]))


#receive a list of integers that has all odds, and one even
#or all even and one odd
#takes an array and receive an outlier

def findOutlier(numbers):
    #iterate through the list of arrays
    #keep track of how many odds or evens found

    evenCount = 0
    oddCount = 0 

    for num in numbers:
        if num % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1

    if evenCount > oddCount:
        for num in numbers:
            if num % 2 != 0:
                return num
    else:
        for num in numbers:
            if num % 2 == 0:
                return num

   
print(findOutlier([3,5,2,7,9]))

def reverse_some_chars(s, chars):
  # left = 0
  # right = len(s) - 1

  # while left <= right:
  #   if s[left] in chars and s[right] in chars:
  #     s[left],s[right] = s[right], s[left]
  #     left += 1
  #     right -=1 
  #   elif s[left] not in chars:
  #     left += 1
  #   else:
  #     right -= 1

  # return s

  stack = []
  result = []

  for char in s:
    if char in chars:
      stack.append(char)


  for char in s:
    if char in chars:
      prev_char = stack.pop()
      result.append(prev_char)
    else:
      result.append(char)

  return ''.join(result)
  
  def paired_parentheses(string):
  #receive a pair of paired_parentheses
  #return true if parens are equal to each other
  #ex: (()) => true

  #iterate through the stack
  #check if opening
  #add to the stack
  #if it's a closed, check prev item on stack and pop it off


  stack = []
  for char in string:
    if char == '(':
      stack.append(char)
    elif char == ')':
      print(stack)
      if len(stack) < 1:
        return False
      else:
        stack.pop()
  return len(stack) == 0 

def befitting_brackets(string):
  #receive a string of brackets 
  #return boolean , True if matching brackets, else False
  #ex: '({}' => False

  brackets = {
    '(': ')',
    '[': ']',
    '{': '}'
  }

  stack = []

  for char in string:
    if char in brackets:
      stack.append(char)
    else:
      if len(stack) == 0:
        return False
      else:
        prev_char = stack.pop()
        if char != brackets[prev_char]:
          return False
  
  return len(stack) == 0

import math
from decimal import Decimal

def am_i_wilson(n):
    #receive a whole and positive integers
    #return boolean - where true if n! of n else False
    
    #ex: 0 => False
    #ex: 5 => True
    
    #ex: (5 - 1)! + 1
    # / 5 * 5
    #(4)! + 1
    #/ 25
    #(4* 3 * 2 *1) + 1 = 25
    # / 25
    # == 1 = True
    
#     if n == 0:
#         return False
    
#     new_num = n - 1
#     result = math.factorial(new_num) + 1
#     divider = n * n
#     answer = Decimal(result)/Decimal(divider)
    
#     return True if answer == 1 else False

    return n in (5, 13, 563)

def decompress_braces(string):
  #receive a string of numbers and integers
  #return a string back where number is in front of integers
  #ex: 

  #keep two pointers
  #i stays on integers
  #j goes until it finds end } 
  #then do i * j 
  #add to result 

  result = []
  stack = []
  numbers = '123456789'

  for char in string:
    if char in numbers:
      stack.append(int(char))
    else:
      if char == '}':
        segment = ''
        while not isinstance(stack[-1], int):
          popped = stack.pop()
          segment = popped + segment
        num = stack.pop()
        stack.append(num * segment)

      elif char != '{':
        stack.append(char)

  return ''.join(stack)
          

      
          
def nesting_score(string):
  #receive a string of chars 
  #return an integer of nesting_score
  #ex: 

  #use a stack
  #add the parenthesis of opening
  #if closing, 
  #att total point
  #if another closing, multiply it 
  #return total

  stack = [0]

  for char in string:
    if char == "[":
      stack.append(0)
    else:
      popped = stack.pop()
      if popped == 0:
        stack[-1] += 1
      else:
        stack[-1] += popped * 2
  return stack[0]
      

      
      
      
  return ''.join(result)

from collections import deque

def knight_attack(n, kr, kc, pr, pc):
  moves = [
    (-2, -1), (-2,1),
    (2, -1), (2, 1), 
    (1, -2), (-1, 2),
    (1, 2), (-1, -2)
  ]

  queue = deque([(kr, kc, 0)])
  visited = set((kr,kc))

  while queue:
    row, col, dst = queue.popleft()

    if (row,col) == (pr, pc):
      return dst

    for nr, nc in moves:
      new_row = row + nr
      new_col = col + nc
      row_inbounds = 0 <= new_row < n
      col_inbounds = 0  <= new_col < n
      pos = (new_row, new_col)
      if row_inbounds and col_inbounds and pos not in visited:
        visited.add(pos)
        queue.append((new_row, new_col, dst + 1))
  return None

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #receive a list of strings of lowercase letters
        #return the longest string of starting letters
        #ex: 

        #initialize an empty list
        #iterate through each string
        #check if the beginning letters match for all
        #if true, add to empty list, else, return ""


        result = []

        for i in range(len(strs[0])):
            letter = strs[0][i]
            for word in strs:
                if i >= len(word) or word[i] != letter:
                    return ''.join(result)
            result.append(letter)

        return result
        

        class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #receive a list of strings
        #return similar strings back together
        #ex: 

        #iterate through each word
        #sort them
        #check if it exists in the object,
        #if it does, add it specific key
        #else, create a new key for it
        #return the result list back from values


        anagrams = {}

        for word in strs:
            ana = ''.join(sorted(word))
            if ana in anagrams:
                anagrams[ana].append(word)
            else:
                anagrams[ana] = [word]
        
        return list(anagrams.values())
    
    class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #receive a list of strings
        #return similar strings back together
        #ex: 

        #iterate through each word
        #sort them
        #check if it exists in the object,
        #if it does, add it specific key
        #else, create a new key for it
        #return the result list back from values


        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return list(result.values())

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #receive a list of integers
        #return a list back sorted without using .sort or any sorted function
        #ex: 

        #create an empty list
        #iterate through checking if nums is smaller than previous
        #return list

        #could do bubble sort => O(n^2)

        # for i in range(0, len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < nums[i]:
        #             nums[i], nums[j] = nums[j], nums[i]
        # return nums

        #4, 3, 5
        #.  j
        #.  i
        #.  curr
        #i
        #curr

        for j in range(1, len(nums)):
            i = j
            curr = nums[i]
            while i > 0 and curr < nums[i - 1]:
                nums[i] = nums[i - 1]
                i -=1
            nums[i] = curr
        return nums


  

