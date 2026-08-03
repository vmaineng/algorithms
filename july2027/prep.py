def charAccum(str):
    #receive a string of chars
    #return the chars
    #ex: 
    result = []
    for idx, char in enumerate(str):
        
        result.append(char * (idx + 1))
        
    return '-'.join(result)

# print(charAccum('abc'))


def weighsMore(str1,str2):
    #take the first num // second num
    #see which one out weighs the other
    #ex: ('1:3','1:2')

    totalOne = int(str1[0]) // int(str1[2])
    totalTwo = int(str2[0]) // int(str2[2])

    return True if totalOne > totalTwo else False
print(weighsMore('1:3','1:2'))

class Dog ():
  def __init__(self, breed):
    self.breed = breed
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")
scoobydoo.bark = lambda: "Woof"

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #receive a large unsorted nums array
        #return the kth largest element
        #ex: [3,2,5,1] => 2 
        # [1,2,3,5] => 2 # time: O(n log n); #space: O(n)

        #initialize a max heap
        #iterate through the integers
        #add all of the integers until it reaches the length of k
        #then we are oging to opop it off until we hit k times

        heap = [ ]

        for num in nums:
            heapq.heappush(heap, num) 
            if len(heap) >k:
                heapq.heappop(heap)

        
        return heap[0] #O(logK) #space:O(K)

    class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums *2

    class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #receive an integer of nums
        #return True if value > 1, else False
        #ex: [1,3,5] => False
        #ex: [1, 3,1] => True b/c 1 is duplicate

        #iterate through the array
        #iterate again through the array at second number
        #this will be O(n ^2)

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
             
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        #use a set
        #iterate through
        #check if num exists in set, if not add, in, if it does, return False

        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #receive two strings and check if anagrams of each
        #anagram = same amount of letters as each other
        #ex: 'helllo', 'joje => False
        #ex: 'hi', 'ih' => True

        #if not the same length, can return False

        #sort them
        #check ift he sorted versions == other

        if len(s) != len(t):
            return False

        # return sorted(s)== sorted(t)

        #time: O(2nlogn) => O(logn)
        #space: O(2n) => O(n)

        #keep track of chars from one of the words
        #then iterate through the second word
        #if the object is empty, we used all words => return True else return False

        seen = { }

        for char in s:
            seen[char] = seen.get(char, 0) + 1

        for char in t:
            if char in seen:
                seen[char] -= 1
            else:
                return False
        
        return all(count == 0 for count in seen.values())

    class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #receive a list of lowercase chars
        #return the list back in reverse
        #ex: ['h','e'] => ['e','h'] 

        #could use the reverse function
        # return s.reverse()

        #to do it in place - use two pointers
        #starting from left and right
        #keep going until it hits middle and swap them

        left = 0
        right = len(s) - 1

        while left < right:
            s[left],s[right] = s[right], s[left]
            left += 1
            right -=1 
        return s