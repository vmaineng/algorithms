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
  

  def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)
  visited = set([node_A])
  queue = deque(([node_A, 0]))

  while queue:
    node, distance = queue.popleft()

    if node == node_B:
      return distance

    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, distance + 1))
  return -1

def has_path(graph, src, dst):
  #receive graph, src node, and dst node
  #
  if src==dst:
    return True
  for neighbor in graph[src]:
    if (has_path(graph, neighbor, dst) == True):
      return True
  return False

def has_path(graph, src, dst):
  #receive a graph as adj matrix, src, and dst
  #return True if src == dst node, else False
  #

  if src == dst:
    return True

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst):
      return True
  return False

 queue = deque([src])

  while queue:
    current = queue.popleft()

    if current == dst:
      return True
      
    for neighbor in graph[current]:
      queue.append(neighbor)

  return False

def undirected_path(edges, node_A, node_B):
  #receive a list of edges, and two nodes
  #return True if nodes are connected
  graph = build_graph(edges)
  return has_path(graph, node_A, node_B, set())


  #build a adj matrix
  #then iterate through the matrix to see if edges are connected, return True if yes, else False


def build_graph(edges):
  graph = {}

  for a,b in edges:
    if a not in graph:
      graph[a] = []

    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph


def has_path(graph, src, dst, visited):
  if src == dst:
    return True

  if src in visited:
    return False

  visited.add(src)

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) == True:
      return True
  return False

from collections import deque

def has_path(graph, src, dst):
  #receive a adj matrix, src node, and dst node
  #return true if path from src reaches dst, else False
  #ex: 

  #bfs using queue:
  #import deque
  #check if current node == dst, return true
  #if not, add in its neighbor node
  #return False after checking everything if it's not it

  queue = deque([src])
  while queue:
    current = queue.popleft()
    if current == dst:
      return True 

    for neighbor in graph[current]:
      queue.append(neighbor)
  return False

def has_path(graph, src, dst):
  if src == dst:
    return True

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst):
      return True
  return False

def undirected_path(edges, node_A, node_B):
  #receive an adj list, node value, node value
  #return True if node a reaches node B, else False
  #ex:

  #create an adj matrix
  #check if path exits

  graph = build_graph(edges)
  return has_path(graph, node_A, node_B, set())

def build_graph(edges):
  graph = {}

  for a,b in edges:
    if a not in graph:
      graph[a] = []

    if b not in graph:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)
  return graph

def has_path(graph, src, dst, visited):
  if src == dst:
    return True

  if src in visited:
    return False

  visited.add(src)

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited):
      return True
  return False

def connected_components_count(graph):
  #receive an adj matrix
  #return count of how many connected 
  #ex:

  #initialize a count
  #iterate through graph
  #check if node connects
  #return count

  count = 0
  visited = set()

  for node in graph:
    if explore_path(graph, node, visited) == True:
      count += 1
  return count

def explore_path(graph, current, visited):
  if current in visited:
    return False

  visited.add(current)

  for neighbor in graph[current]:
    explore_path(graph, neighbor, visited)
  return True
    

    from collections import queue

def shortest_path(edges, node_A, node_B):
  #receive a graph list
  #return shortest path count from node a to b  
  #ex:

  #create an adj matrix
  #initialize a count of min steps
  #traverse through using a queue for bfs

  graph = build_graph(edges)
  queue = deque([ (node_A, 0) ])
  visited = set([node_A])

  while queue:
    node, distance = queue.popleft()

    if node == node_B:
      return distance

    visited.add(node)

    for neighbor in graph[node]:
      queue.append(neighbor, distance + 1)
  return -1


def build_graph(edges):
  graph = { }

  for a,b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)
  return graph

from collections import deque

def shortest_path(edges, node_A, node_B):
  #receive an adj list
  #return min distance
  #ex:

  #create an adj matrix
  #traverse through queue
  #visited - keep track of nodes seen
  #queue to travel

  graph = build_graph(edges)
  queue = deque([ (node_A, 0) ])
  visited = set([node_A])

  while queue:
    node, distance = queue.popleft()
    if node == node_B:
      return distance

    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, distance + 1))
  return -1

def build_graph(edges):
  graph = {}

  for a,b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph

from collections import deque

def has_path(graph, src, dst):
  #receive an adj matrix
  #return True if src reaches dst, else False
  #ex:

  #dfs:
  #base case: if src == dst, return True
  #else traverse through its neighbor, return True if they meet, else return False

  # if src == dst:
  #   return True

  # for neighbor in graph[src]:
  #   if has_path(graph, neighbor, dst):
  #     return True
  # return False

  #bfs: using queue
  queue = deque([src])

  while queue:
    current = queue.popleft()
    if current == dst:
      return True

    for neighbor in graph[current]:
      queue.append(neighbor)
  return False
  
  class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #receive a list of list
        #return how many min intervals
        #ex:

        if not intervals:
            return 0

        count = 0 
        intervals.sort(key=lambda x:x[0])
        prev_end= intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if end <= prev_end:
                count += 1
            else:
                prev_end = end
        return count
    
def island_count(grid):
  #receive a grid of m x n
  #return count of islands spotted

  #ex:

  #iterate through rows and cols
  #check if value is a L, mark all visited
  #return count of L

  visited = set()
  count = 0

  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if explore(grid, row, col, visited):
        count += 1
  return count

def explore(grid, row, col, visited):
  if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 'W' or (row, col) in visited):
    return False

  visited.add((row, col))

  explore(grid, row + 1, col, visited)
  explore(grid, row - 1, col, visited)
  explore(grid, row, col + 1, visited)
  explore(grid, row, col - 1, visited)

  return True
  
  from collections import deque

def shortest_path(edges, node_A, node_B):
  #receive an adj list, node value, and another node value
  #return an integer of how many edges it takes to get from node to node 
  #ex: edges: [
  # ['w', 'x'],
  #['y','z'],
  # ['x', 'y']
  #]

  # w = > y => 2

  #[ {
  # 'w':  ['x'],
  #'x': ['y', 'w'],
  #'y': ['z', 'x'],
  #'z': ['y']
  #}]

  #bfs: use a queue, add a distance
  #create adj matrix
  #iterate through each node
  #check to see if the node value == node_B
  #return distance affilated 
  #add in its neighbor node to the queue, continue checking
  #increment count of distance
  #else return -1

  graph = build_graph(edges)
  queue = deque([ (node_A, 0) ]) #[  ('w', 2)]
  visited = set(( node_A )) #('w', 'x', 'y','w')

  while queue:
    current, distance = queue.popleft() #('y', 2)

    if current == node_B: #'y' => 'y'
      return distance

    for neighbor in graph[current]:
      if neighbor not in visited:
        visited.add((neighbor))
        queue.append((neighbor, distance + 1))
  return -1
      # w => x 

def build_graph(edges):
  graph = {}

  for a,b in edges:
    if a not in graph:
      graph[a] = [] #'w': ['x']
    if b not in graph:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)
  #{'w': ['x', 'v'], 'x': ['w', 'y'], 'y': ['x', 'z'], 'z': ['y', 'v'], 'v': ['z', 'w']} 
  return graph
    
  def island_count(grid):
  #receive a row by col
  #return the amout of island_count
  #ex:

  #intiialize a island_count
  #iterate through if it's L
  #else return 0

  count = 0
  visited = set() 
  
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if explore(grid, row, col, visited):
        count +=1 
  return count

def explore(grid, row, col, visited):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 'W' or (row, col) in visited:
    return False

  postion = (row, col)
 
  visited.add((row, col))

  explore(grid, row - 1, col, visited)
  explore(grid, row + 1, col, visited)
  explore(grid, row, col - 1, visited)
  explore(grid, row, col + 1, visited)
  return True

def minimum_island(grid):
  #receive a grid
  #return the size of smalleset island count 
  #ex: 

  #iterate through one
  #count the size
  #return size back of smallest one

  min_size = float("inf")
  visited = set()
  
  for row in range(len(grid)):
    for col in range(len(grid[0])):
        size = dfs(grid, row, col, visited)
        if size < min_size and size > 0:
          min_size = size
  return min_size

def dfs(grid, row, col, visited):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 'W' or (row, col) in visited:
    return 0

  visited.add((row, col))

  size = 1
  size += dfs(grid, row -1 , col, visited)
  size += dfs(grid, row + 1, col, visited)
  size += dfs(grid, row, col - 1, visited)
  size += dfs(grid, row, col + 1, visited)
  
  return size
  
  def minimum_island(grid):
  #receive a row and col
  #return smallest island size
  #ex:

  #iterate through row and cols
  #if size is smaller than current size, update it
  #return size

  size= float('inf')
  visited = set()
  
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      count = explore(grid, row, col, visited)
      if count < size and count > 0:
        size = count
  return size

def explore(grid, row, col, visited):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 'W' or (row, col) in visited:
    return 0

  visited.add((row, col))

  size = 1
  size += explore(grid, row - 1, col, visited)
  size += explore(grid, row +1, col, visited)
  size += explore(grid, row, col - 1, visited)
  size += explore(grid, row, col + 1, visited)
  return size
  

  def island_count(grid):
  #receive a row x cols
  #return a count of island_count
  #ex:

  #iterate through rows and cols
  #through the funciton perform dfs
  #return a count of islands seen

  count = 0
  visited = set()

  for row in range(len(grid)):
    for col in range(len(grid[0])):
      count += explore(grid, row, col, visited)
  return count

def explore(grid, row, col, visited):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 'W' or (row, col) in visited:
    return False

  visited.add((row, col))

  explore(grid, row - 1, col, visited)
  explore(grid, row + 1, col, visited)
  explore(grid, row, col - 1, visited)
  explore(grid, row, col + 1, visited)
  return True

def fizz_buzz(n):
  #receive an integer
  #return a list of integers 
  #Fizzbuzz if % 3 and 5 or 3 = fizz and if 5 only = Fizzbuzz
  #ex: 15 => fizzbuzz, 4 => None

  #iterate up to n
  #if num % 3 and 5 == fizzbuzz, else, print the num

  result = []
  for num in range(1, n +1):
    if num % 3 == 0 and num % 5 == 0:
      result.append("fizzbuzz")
    elif num % 3 == 0 :
      result.append("fizz")
    elif num % 5 == 0 :
      result.append("buzz")
    else:
      result.append(num)
  return result

  