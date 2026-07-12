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