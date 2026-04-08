def addTree(root):
    if not root:
        return 0
    
    return root.value + addTree(root.left) + addTree(root.right)
def intersection(a, b):
  #receive a two list o fintegers
  #return a list back of items that exist in both

  #iterate through each item in the list
  #check if it's in second list
  #add to the result
  #return result

  # result = []
  # for item in a:
  #   if item in b:
  #     result.append(item) 
  # return result

  #time: O(n * m)
  #space:O(min(n,m))

  #create a unique set of a
  #iterate through b
  #check if set has it
  #return item sin a result

  result = []
  uniqueA = set(a)
  for item in b:
    if item in uniqueA:
      result.append(item)
  return result

  #time: O(n +m)

  def exclusive_items(a, b):
  #receive two list of integers
  #return a list back of integers that do not exist in other

  #ex: 

  #initialize a result
  #iterate through a
  #check if it's not in b
  #add in list

  # result = []
  # for item in a:
  #   if item not in b:
  #     result.append(item)

  # for item in b:
  #   if item not in a:
  #     result.append(item)
  # return result

  #time: O(n * m)
  #space:O(n + m)

  #create a set of both
  uniqueA = set(a)
  uniqueB = set(b)

  result = []
  for num in a:
    if num not in uniqueB:
      result.append(num)

  for num in b:
    if num not in uniqueA:
      result.append(num)
  return result


def all_unique(items):
  #create a set
  #iterate through
  #check if letters exist in the items

  uniqueA = set(items)
  if len(uniqueA) == len(items):
    return True
  else:
    return False
  
  def intersection_with_dupes(a, b):
  #receive two list of integers
  #return a list back of same duplicate amounts found

  #create a pointer in longest list
  #check if the letters are same, return in result


  #keep track of char count
  #iterate through second list
  #check if char is the same and how many amounts there are
  #add the char to the list


  charA = {}
  charB = {}

  for char in a:
    charA[char] = charA.get(char, 0) + 1

  for char in b:
    charB[char] = charB.get(char, 0) + 1

  result = []

  for char in charA:
    if char in charB:
      count = min(charA[char], charB[char])
      result.extend([char] * count)
   
  return result
      

      class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowerS = ''.join(char for char in s.lower() if char.isalnum())
        # return lowerS == lowerS[::-1]


        lowerS = ''.join(char for char in s.lower() if char.isalnum())

        left = 0
        right = len(lowerS) - 1

        while left < right:
            if lowerS[left] != lowerS[right]:
                return False
            left += 1
            right -= 1

        return True
  

  class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #receive a list of int in non-decreasing order
        #return the length of the array back where duplicates have been removed
        #ex: [1,2,3] => 3 

        #initialize a new result
        #iterate through with i and j
        #check if the value is same as last value
        #if not add it to count

        if not nums:
            return 0

        k = 1 #index pointer to help rewrite

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
      
        
class Solution:
    def reverseVowels(self, s: str) -> str:
        #receive a string of upper or lowercase
        #return the string back where vowels are reversed
        #ex: 'hello' => 'holle'

        #iterate through each char
        #check if it exists in vowel
        #add it to the stack
        #then iterate through string again
        #add in from the stack

        stack = []
        vowels='AEIOUaeiou'

        for char in s:
            if char in vowels:
                stack.append(char)
            
        result = ''

        for char in s:
            if char in vowels:
                result += stack.pop()
            else:
                result += char
        return result
    
    class Solution:
    def reverseVowels(self, s: str) -> str:
        #receive a string of upper or lowercase
        #return the string back where vowels are reversed
        #ex: 'hello' => 'holle'

        #iterate through each char
        #check if it exists in vowel
        #add it to the stack
        #then iterate through string again
        #add in from the stack

        vowels=set('AEIOUaeiou')

        left = 0
        right = len(s) -1
        s=list(s)


        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            
            if s[right] not in vowels:
                right -=1 
                continue

            s[left],s[right] = s[right], s[left]
            left += 1
            right -=1
        return ''.join(s)

       