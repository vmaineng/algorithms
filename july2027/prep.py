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