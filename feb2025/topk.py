from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        countNums = Counter(nums)

        sortedCount = sorted(countNums.items(), key=lambda x:x[1], reverse = True)
        return [num for num, value in sortedCount[:k]] #O(k)

s=Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))

#time: O(n log n)
#space: O(k)

#bucket sorting #O(N)
#heaps #o (n log k)

def greet(name, owner):
    #re eive a string of name
    #return 'hello boss' if name == owner, else 'hello guest'
    
    #ex: Mary, Mar => 'hello guest'
    #ex: mary, mary => 'hello boss'
    
    #return 'hello boss' if name == owner, else 'hello guest'
    
    return 'Hello boss' if name.lower() == owner.lower() else 'Hello guest'

    def get_sum(a,b):
    #receive two integers
    #return the sum between a and b
    
    #sort the integers from smallest to biggest
    #add the sum in between
    #return sum
    
    if a < b:
        return sum(range(a, b+1))
    else:
        return sum(range(b, a+1))