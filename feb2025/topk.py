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
    return sum(range(min(a,b), max(a,b) + 1))

    def add_binary(a,b):
    #receive two numbers
    #return the sum of ttwo numbers in a string of binary
    
    #ex: 3,4 =>7 in decimal => '111'
    
    #add a + b together to get the decimal sum
    #apply the bin function on the decimal sum
    #return the number converted from bin
    
    total = a + b
    return bin(total)[2:]

    #time: O(n)???
    #space: O(1) => only dealing with 2 numbers

    class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if not self.empty() else None

    def top(self) -> int:
        return self.stack[-1] if not self.empty() else None

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

class Trie:

    def __init__(self):
        self.words = words

    def insert(self, word: str) -> None:
        return self.words.append(word)

    def search(self, word: str) -> bool:
        return word in self.words
        #O (n * m)

    def startsWith(self, prefix: str) -> bool:
        return any(w.startswith(prefix) for w in self.words)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.bookings:
            if startTime < end and endTime > start:
                return False
        self.bookings.append((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        return self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self) -> int:
        return self.q1[-1] if self.q1 else None
        

    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

import random

class RandomizedSet:

    def __init__(self):
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.list:
            return False
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.list:
            return False
        self.list.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

import random

class RandomizedSet:

    def __init__(self):
        self.list = []
        self.map = {}
        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.list.append(val)
        self.map[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        last_val = self.list[-1]
        index = self.map[val]
        self.list[index] = last_val
        self.map[last_val] = index

        self.list.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def area_or_perimeter(l , w):
    # receive two integers
    #return the area if it's a square, else return its perimeter if it is a rectangle
    
    #ex: (3,3) => 3 * 3 => 9
    #ex: (2, 3) => 2 + 2+ 3 + 3 => 
    #ex: (6, 10) => 6 + 6 + 10 + 10 => 32
    
    
    #could have l or w as 0?
    #no possibility of negative numbers => area or perimeter would be 0

    #brute force:
    #if l and 2 are the same numbers, 
    #calculate the area (l *w)
    #else, calcualte the perimeter ( l + l + w + w)
    
    if l == w:
        area = l * w
        return area
    else:
        perimeter = (l * 2) + (w * 2)
        return perimeter

#time: O(1)
#Space: O(1)

return l * w if l == w else (l + w) * 2

def is_triangle(a, b, c):
    #receive 3 integers (can be pos and neg)
    #return boolean; true if can make a triangle, else False
    
    #ex: 

    #edge case:
    #if any of the numbers are negative, return False immediately
    
    #.  a /\b
    #   c _
    
    #(5,1,2)
    
    #if a > b * c, return False
    #else return True
    
    
#     if a + b <= c or a + c <= b or b + c <= a:
#         return False
#     else:
#         return True

    return False if a + b <= c or a + c <= b or b + c <= a else True

#time: O(1)
#space: O(1)