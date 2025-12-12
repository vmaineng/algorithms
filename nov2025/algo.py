def to_csv_text(array):
    #receive a list of list
    #return a string back
    
    #splitlines the list
    #and add together
    
    #add it into one list
    #for each row, convert number to a string and join with a comma
    #join back with a string and a \n
    
    csv_rows=[]
    for row in array:
        csv_rows.append(','.join(map(str,row)))
    return '\n'.join(csv_rows)

def to_csv_text(array):
    #receive an array
    #return a string back of new items
    
    #create a new empty list
    #iterate through the rows in array
    #convert them into a string
    #return it joined back with csv
    
    csv_rows = []
    for row in array:
        csv_rows.append(','.join(map(str, row)))
    return '\n'.join(csv_rows)

    def contamination(text, char):
    #receive a string of lowercase letters, numbers, and a string char
    #replace the text with chars
    
    #ex: 'hello', 'z' => 'zzzzz'
    
    #initialize an empty list
    #iterate through each char
    #replace each text with char
    #return new string
    
    new_word = []
    for letter in text:
        new_word.append(char)
    return ''.join(new_word)

def calculator(x, y, op):
    #receive two numbers and a string of operations
    #return the output from x & y based off of operations
    
    #ex: 4, 2, '+' => 4 + 2 => 6
    #ex 8,4, '/' => "unknown vaue"
    
    if x == str(x) or y == str(y):
        return "unknown value"
    
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x /y
    else:
        return "unknown value"
    

    def rain_amount(mm):
    if (mm < 40):
         return f"You need to give your plant {abs(mm - 40)}mm of water"
    else:
         return "Your plant has had more than enough water for today!"
    

    def sakura_fall(v):
    #receive an integer, ensure it is positive
    #return total time for petal to reach ground
    #ex: travels 5 cm/s, and it is 80 secs
    #ex: 10cm/s, now it's 40 secs
    
    new_cm = v /5
    return 80 / new_cm if v > 0 else 0
    
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #receive an array of integers and an integer number target
        #return the position of two numbers

        #ex: [4,3, 1, 0], 1 => [2, 3]

        #iterate through the numbers for one loop
        #continue a second iteration while having first pointer stay one value
        #check to see if two values at index positions are equal to target
        #return the index position
        #else, return [-1, -1] and not found

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [ -1, -1]
        

        #time: O(n^2) due to using two inner for loops
        #space: O(n) for n in nums

        obj = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in obj:
                return [obj[difference], i]
            else:
                obj[nums[i]] = i
        return [ -1, -1]
    
    def divide_numbers(x,y):
    return x / y

def remove(st):
    #receive a string
    #return a strign with no '!' at end
    #ex: '!hel!' => '!hel'
    
    #check if end of string is !
    #then do not add
    
#     newWord = []
#     revWord = ''.join(reversed(st))
# #     print(revWord)
#     for i in range(len(revWord)):
#         if revWord[i] != '!':
#             newWord.append(revWord[i])
#     return ''.join(reversed(newWord))

    newWord = []
    
    for i in range(len(st)-1, -1, -1):
        if st[i] != '!':
            newWord.append(st[i])
    return ''.join(newWord)

class Person:
    def __init__(self, name,age):
        self.info="{}s age is {}".format(name, age)


        # input is an unsorted list of 3 positive integers
def pythagorean_triple(integers):
    # return True if it is possible to form a Pythagorean triple with the 3 integers
    # return False if it is not possible
    #receive a list of integers
    
    #sort the list of integers
    #check if a^2 + b^2 = c^2, return True, else return False
    
    sortList = list(sorted(integers))
    
#     if sortList[0]**2 + sortList[1]**2 == sortList[2]**2:
#         return True
#     else:
#         return False
    
    return True if sortList[0]**2 + sortList[1]**2 == sortList[2]**2 else False

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    #receive distance, speed and a dolphin
    #return Alive if can make it to pontoon, else Shark Bait
    
    #shark's: 8/4 = 2 b/c dolphin present, 50;  50 /2 = 25
    #human's: 4 , 12 => 12 /4 = 3
    
    #25 > 3 => "Alive"
    
    if dolphin:
        shark_speed = shark_speed /2
        
    shark = shark_distance / shark_speed
    human = pontoon_distance / you_speed
    
    return 'Alive!' if human < shark else 'Shark Bait!'
    
    # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  #receive the root node of a tree
  #return the nodes

  #if no nodes, return empty list

  #intialize a list
  #iterate from left, then iterate on right
  #return the list

  if root is None:
    return []

  left_values = depth_first_values(root.left)
  right_values = depth_first_values(root.right)

  return [root.val, *left_values, *right_values]

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  #receive a root Node
  #return the root values in DFS order

  #intialize a stack with root Node
  #values list
  #iterate while stack is not empty
  #pop off top node, add to stack
  #then iterate on right, then on left
  #return list

  if not root:
    return []

  values = []
  stack = [ root ]
  while len(stack) > 0:
    current = stack.pop()
    values.append(current.val)

    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)

  return values

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def breadth_first_values(root):
  #receive a root Node
  #return BFS 

  #initialize a queue
  #values list
  #while queue is not empty
  #iterate through all the nodes

  if not root:
    return []
  
  values = []
  queue = deque([ root ])

  while queue:
    current = queue.popleft()
    values.append(current.val)

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return values
  
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  #receive the root node of a tree_sum
  #return the sum of all node values


  #intiialize a total
  #iterate through each node and add to sum 

  if not root:
    return 0

  return root.val + tree_sum(root.left) + tree_sum(root.right)


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def tree_includes(root, target):
  #receive the root node, and a target node
  #return True if node exists, else False

  #visit bfs

  if not root:
    return False

  queue = deque([root])
  while queue:
    current = queue.popleft()
    if current.val == target:
      return True

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return False

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  #receive a root node of a binary tree
  #return an integer of total sum 
  #ex:  5
  #   /  \
  # -3   null (0)

  #5 + -3 => 2

  #base case: if not root, return 0
  #recursive case: keep calling and adding to the total for left side & right side

  if not root:
    return 0

  return root.val + tree_sum(root.left) + tree_sum(root.right)

  #time: O(n) #n of nodes
  #space: O(n) #n of nodes
  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  #receive a root node of a binary tree
  #return an integer of total sum 
 
  #base case: if not root, return 0
  #recursive case: keep calling and adding to the total for left side & right side

  # if not root:
  #   return 0

  # return root.val + tree_sum(root.left) + tree_sum(root.right)

  #time: O(n) #n of nodes
  #space: O(n) #n of nodes

  #bfs: uses a queue, (python will use a deque)

  #pop off the current node in the queue
  #add current's value to the total
  #if there are any left children, add it to the queue
  #if there are any right children, add it to the queue
  #return the total

   #ex:  5
  #   /  \
  # -3   null (0)

  #5 + -3 => 2


  from collections import deque

  if not root:
    return 0

  total_sum = 0
  queue = deque([root]) #5, -3
  while queue:
    current = queue.popleft()
    total_sum += current.val #total_sum = 5 + -3 = 2

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return total_sum

  #time: O(n) # n of nodes
  #space: O(n) #n of nodes
  
  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def tree_min_value(root):
  #receive root node of a tree 
  #return the min value seen

  #ex:

  #intialize a variable to float infinity
  #if the number is smaller than float infinity
  #then update float infinity
  #traverse left and right
  #bfs to check level by level

  if not root:
    return 0

  queue = deque([root])
  min_value = float('infinity')

  while queue:
    current = queue.popleft()
    if current.val < min_value:
      min_value = current.val

    if current.left:
      queue.append(current.left)

    if current.right:
      queue.append(current.right)
  return min_value

def tree_min_value(root):
  if not root:
    return float('inf')

  smallest_left = tree_min_value(root.left)
  smallest_right = tree_min_value(root.right)
  return min(root.val, smallest_left, smallest_right)
  