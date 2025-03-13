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

return a + b <= c or a + c <= b or b + c <= a

#time: O(1)
#space: O(1)

import random

class RandomizedSet:

    def __init__(self):
        self.list = []

    def insert(self, val: int) -> bool: #O(n)
        if val in self.list:
            return False
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool: #O(n)
        if not val in self.list:
            return False
        self.list.append(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def goals(laLiga, copaDelRey, championsLeague):
    #receive 3 integers
    #return the sum of all 3 points
    
    #ex: (4, 3, 2) => 9

    #add each integer to get the total

    #handles fixed number of arguments
    #raises error if args don't match
    return laLiga + copaDelRey + championsLeague

    #using args is more dynamic and flexible
    #assuming any number of arguments
    #no error raised if more or less args are passed.
    return sum(*a)

    def get_age(age):
    #receive a string of 'x years old'
    #return the x in an integer
    
    #ex: '3 years old' => return 3
    
    #return the first char and convert into a num
    return int(age[0:1])
    return int(age[0])

    import random

class RandomizedSet:

    def __init__(self):
        self.random_list = []

    def insert(self, val: int) -> bool:
        #if item is in the list, return False
        #else add it to the list, return True
        if val in self.random_list:
            return False
        self.random_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        #if item is not in the set, return False
        #else remove the item from the list
        #return True

        if val not in self.random_list:
            return False
        self.random_list.remove(val)
        return True

    def getRandom(self) -> int:
        #from random library, add in random.choice of the intgeters in the list
        return random.choice(self.random_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

def feast(beast, dish):
    # receive a string of lowercase letters for beast and dish
    #return True if first letter and last name letters are the same as food
    #ex: 'blue jay', 'belly ray' => true
    
#     print(dish[-1:], beast[-1:])
    
    return beast[0] == dish[0] and beast[-1:] == dish[-1:]

    def array_diff(a, b):
    #receive two lists of elements
    #return a list back of where an element of 2 does not exist in element of 1
    
    
    #ex: [3,4,5,2], [3] => [4,5,2]
    
    #create an empty list
    #create pointers starting from first index of each list
    #sort the elements
    #check the first value if it equals the same
    #then move the pointer
    #else add it in the list
    
    output = []
    for num in a:
        if num not in b:
            output.append(num)
    return output

#time: O(n * m)
#space: O(n)

def reverse_words(s):
    #receive a string of words and spaces, upper and lower cases, 
    #return a string back by reversing the string by words
    
    #ex: 'hello world' => 'world hello'
    #ex: 'The dog jumped' => 'jumped dog The'
    
    #brute force:
    #initialize an empty string
    #iterate starting from the end
    #check if it is an empty space, add the word to the empty string
    #return the string back
    
    #time: O(n^2)
    #space: O(n) #n amount of words
    
    #split the string by spaces
    #intiialize an empty array
    #iterate from the end of the string, add to the end of an array
    #return by join back by strings

    #time: O(n) n amount of words in s
    #space: O(n) n amount of words
    
    #split the string, use the slicing method and reverse
    return ' '.join(s.split(" ")[::-1])
    
    #time: O(n) n amoutn of words in s
    #space: O(n) n amoutn for list in memory

    return ' '.join(reversed(s.split(' ')))
    
    def longest(a1, a2):
    #receive two strings of lowercase letters with no spaces
    #return a new sorted string containing unique characters
    
    #ex: 'aaaabcdbbe', 'bbbiiilel' => 'ab
    
    #brute force:
    #create a pointer in the first char of each string
    #compare if the characters are the same
    #if not, add to the output string
    #else, increment
    #return the output string
    
    #optimize:
    #create sets for both string a and b
    
    set1 = set(a1)
    set2 = set(a2)
    
    return ''.join(sorted(set1.union(set2)))

    #time: O(n log n) #sort
    #space: O(n) for n amount of chars we have to iterate through

    import random

class RandomizedSet:

    def __init__(self):
        #initialized the object
        self.randomList = []

    def insert(self, val: int) -> bool:
        #if val is present, return False immediately
        #add the value, return True

        if val in self.randomList:
            return False
        self.randomList.append(val)
        return True

        #O(1) operation

    def remove(self, val: int) -> bool:
        #if the value does not exist, return false
        #else, delete the item, return true

        if val not in self.randomList:
            return False
        self.randomList.remove(val)
        return True

        #O(N)

    def getRandom(self) -> int:
        #random library and use the .choice method to obtain a number from the elements
        return random.choice(self.randomList)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

import random

class RandomizedSet:

    def __init__(self):
        #initialized the object
        self.randomList = []
        self.randomObj = {}

    def insert(self, val: int) -> bool:
        #if val is present, return False immediately
        #add the value, return True

        if val in self.randomList:
            return False

        self.randomList.append(val)
        self.randomObj[val] = len(self.randomList) - 1
        return True

        #O(1) operation

        #[1, 2, 3]
        #{
        #     1: 0,
        #     2: 1,
        #     3: 2
        # }

    def remove(self, val: int) -> bool:
        #if the value does not exist, return false
        #else, delete the item, return true

        if val not in self.randomList:
            return False
        
        #if val exists, 
        #move value from the middle of the list to the end of the list = swapping places
        #pop the value
        #update the idx position in the dictionary for the element that was swapped
        #delete the previous entry

        last_val = self.randomList[-1]
        element_to_move = self.randomObj[val] #O(1) time to grab the index position

        self.randomList[element_to_move] = last_val
        self.randomObj[last_val] = element_to_move

        self.randomList.pop()
        del self.randomObj[val]

        return True
        #orig
        #[1, 2, 3]
        #{
        #     1: 0,
        #     2: 1,
        #     3: 2
        # }
        #new
        #[1, 3, 2] => [1, 3]
        #{
        #     1: 0,
        #     2: 2,
        #     3: 1
        # }

        #O(N)

    def getRandom(self) -> int:
        #random library and use the .choice method to obtain a number from the elements
        return random.choice(self.randomList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
    
    
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #receive two sorted list1 and list2
        #return back one sorted LL

        #ex: list1: 1 -> 2 -> 3 -> null
        #list2: 2 -> 5 -> null

        #output: 1 -> 2 -> 2 -> 3 -> 5 -> null

        #edge cases: if list1 and list2 are empty, return []

            #ex: list1: 1 -> 2 -> 3 -> null
              #.           c1
        #list2: 2 -> 5 -> null
        #.     c2

        #head: None -> 1 -> 

        if not list1 and not list2:
            return None
        
        current1 = list1
        current2 = list2
        head = ListNode() #0
        tail = head

        while current1 and current2:
            if current1.val < current2.val:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            
            tail = tail.next
            
        if current1:
            tail.next = current1
        else:
            tail.next = current2
        
        return head.next

        class Solution:
    def fib(self, n: int) -> int:
        #receive an integer
        #return the total of adding numbers from each integers up to n

        #ex: could iterate up to n amount
        #add to total

        #optimize force:
        #call the function until it hits n
        #base case if num == n, then return sum
        #else add up total

        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)
        class Solution:
    def fib(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        memo[n] = self.fib(n-1, memo) + self.fib(n - 2, memo)
        return memo[n]

    
    
def usdcny(usd):
    #receive a whole integer
    #return the chinese yuan equivalent of usd
    #ex: 1usd => 6.75
    
    #calc amt by taking usd x 6.75
    #return amount with two decimal places
    amount = usd * 6.75
    return f"{amount:.2f} Chinese Yuan"

    def six_toast(num):
    #receive a whole integer
    #return the total amount of toast you need to put in or take out
    #toaster can fit 6 slices
    #ex: 14 => 14 -6 => 8
    
    #take num - 6 and return the number
    
    return abs(num - 6)

    def sum_str(a, b):
    #receive string of integers or empty spaces
    #return the total of two integers back as a string
    
    #ex: '3', '' => '3'
    
    #if string is empty, return 0
    #else convert them to int
    #return it back as string
    
    a = a if a else '0'
    b = b if b else '0'
    return str(int(a) + int(b))

    class Solution:
    def fib(self, n: int) -> int:
        #receive an integer
        #return the sum of the two numbers from before
        #ex: 3 => 1 + 1 = 2

        #base case: if 1, return 1; if 0, return 0
        #else keep calling until you hit 1 or 0

        if n == 1:
            return 1
        if n == 0:
            return 0
        return self.fib(n-1) + self.fib(n-2)
    
    def remove_every_other(my_list):
    #receive a list of strings or a list of integers
    #return a list back where the secondn element is removed
    
    #ex: [1] => [1]
    #ex: [ 1, 2, 3] => [1, 3]
        # 0.  1  2
    
    #brute force:
    #initialize an empty list
    #iterate through val
    #if idx position is even: 
    #add it to the list
    #return list
    
#     evenList = []
#     for idx,ele in enumerate(my_list):
#         if idx % 2 == 0:
#             evenList.append(ele)
#     return evenList

    #Time: O(n) n for all of the elements in the list
    #space:O(n) n for all elements in the list
    
    return [my_list[ele] for ele in range(len(my_list)) if ele %2 == 0]

    #time:O(n) n for each iterable item in the list
    #space: O(n) n for each iterable item in the list

    return my_list[::2] => [start, stop, step]


    def open_or_senior(data):
    #receive a list of lists showing [age, handicap level]
    #return a list back of strings stating if they belong in "Open" or "Senior"
    
    #senior => age >= 55 years and handicap > 7
    
    #ex: [[34, 8], [72, 12], [89, -2]] => ['Open', 'Senior', 'Open']
    
    #use a list comprehension
    #terinary: 'Senior' age >= 55 and handicap > 7 else 'Open'
    
    return ['Senior' if age >= 55 and handicap > 7 else 'Open' for [age, handicap] in data]

#     output = []
#     for pair in data:
#         [age, handicap] = pair
#         if age >= 55 and handicap > 7:
#             output.append('Senior')
#         else:
#             output.append('Open')
#     return output


class Solution:
    def fib(self, n: int, memo={}) -> int:
        #receive an integer
        #return the total from the sequence

        #ex: fib(2) => fib(1) + fib (0) => 1 + 0 => 1

        #brute force:
        #base case: hit fib(1), and/or fib(0)
        #recursively call: fib(n-1) and fib(n-2)

        # if n == 1:
        #     return 1
        # if n == 0:
        #     return 0
        # return self.fib(n-2) + self.fib(n - 1)

        #time: O(n^2)?
        #space: O(N)?

        #using memoization
        #create an object
        #store the values associated with the key
        #fib(3) => going to check in our object with the key exists
        #if key exists of 3, grab and return the value

        if n == 1:
            return 1
        if n == 0:
            return 0
        if n in memo:
            return memo[n]
      
        memo[n] = self.fib(n-2, memo) + self.fib(n - 1, memo)

        return memo[n]