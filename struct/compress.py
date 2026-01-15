def uncompress(s):
    #receive a string
    #return a string back with the count of occurrences for each character
    #ex: '3a2b' => 'aaabb'
    #.    i
    #.     j

    #using two pointers, i && j
    #i stays on the number, and j will increment and find the char
    #iterate through the string
    #if j is not a number
    #add in the amount of letters into the list
    #increment j
    #increment i pointer to where j
    #return the result

    i = 0
    j = 0
    result = []
    numbers = '0123456789'

    while j < len(s):
        if s[j] in numbers:
            j += 1
        else:
            num = int(s[i:j])
            result.append(num * s[j])
            j+=1
            i = j
    return ''.join(result)

# print(uncompress('3a2b'))

#time: O(n)
#space:O(n)

def compress(s):
    #receive a string of lowercase letters
    #return the compressed version with the count of letters next to the character
    #ex: 'aaabbb!' => '3a3b'
    #     i
    #.       j
    #.    012345

    #i and j starting at 0
    #j keeps incrementing until a new letter has been found
    #take the j index - i index * old letter on i
    #move i to j's position 
    
    s += '!'
    i = 0
    j = 0
    result = []

    while j < len(s):
        if s[j] == s[i]:
            j += 1
        else:
            count = j - i
        
            result.append(f"{count}" + s[i])
            i = j

        # if s[j] != s[i]:
        #     count = j - i
        #     result.append(f"{count}" + s[i])
        #     j += 1
        #     i = j
        # else:
        #     j += 1

    return ''.join(result)

print(compress('aaabbb'))

#time: O(n)
#space: O(n)

def uncompress(s):
  #receive a string of chars
  #return the the uncompress version
  #ex: '4ab2c' => 'aaaabcc'

  #two pointers
  #while j is not a number
  #then keep going
  #else, add it the result list
  #take the value of j * int of i

  numbers = '0123456789'
  i =0 
  j = 0 
  result = []

  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      count = int(s[i:j]) 
      result.append(count * s[j])
      j += 1
      i = j
  return "".join(result)
      
      def compress(s):
  #receive a string
  #return a compressed version
  #ex: 'caat' => 'c2at'

  #keep result of a list
  #j - i => the count

  s += '!'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[i] == s[j]:
      j += 1
    else:
      count = j - i
      if count < 2:
        result.append(s[i])
      else:
        result.append(f"{count}")
        result.append(s[i])
      i = j
  return ''.join(result)
  

def is_subsequence(string_1, string_2):
  i = 0
  j = 0

  while i < len(string_1) and j < len(string_2):
    if string_1[i] == string_2[j]:
      i += 1
      j += 1
    else:
      j += 1
  return i == len(string_1)


def has_path(graph, src, dst):
  if src == dst:
    return True
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst):
      return True
  return False

def undirected_path(edges, node_A, node_B):
  graph = build_path(edges)

 


def build_graph(edges):
  graph = {}

  for a,b in edges:
    if a not in edges:
      graph[a] = []
    if b not in edges:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)
  return graph

def has_path(graph, src, dst, visited):
  if src == dst:
    return True

  def intersection(a, b):
  #receive two lists of integers
  #return the list where same elements exist

  #ex: [4,2,1], [3, 2, 1] => [ 2, 1]

  #add all the values from first list to intersection
  #iterate through b and check if num exists in there
  #if is, then leave, else delete it

  unique_a = set(a)
  result = []

  for num in b:
    if num in unique_a:
      result.append(num)
  return result

def sum_of_lengths(strings):
  #receive a list of strings
  #return the total sum of lengths of all strings
  #ex: 

  #base case: if strings empty, return 0
  #add up the sum of the first length with the rest of the item

  if len(strings) == 0:
    return 0

  return len(strings[0]) + sum_of_lengths(strings[1:])

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):
  #receive the head of a linked list 
  #return boolean if linkedlist contains one value 
  #ex: 3 -> 2 -> 3 => False
  #ex: 3 -> 3 -> null => True

  #iterate thorugh while ll is not empty
  #check if the val is same as head's val
  #return False if it does not
  #else iterate through entire had, return True

  current = head
  while current:
    if current.val != head.val:
      return False
    current = current.next
  return True


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def tree_levels(root):
  #receive a root Node
  #return all paths by tree_levels
  #ex: 

  #bfs

  #while queue is not empty
  #add in current level to result
  #add in their children
  #then add in the current level

  if not root:
    return []

  result = []
  queue = deque([root])
  while queue:
    levels = len(queue)
    current_level = []

    for node in range(levels):
      current = queue.popleft()
      current_level.append(current.val)

      if current.left:
        queue.append(current.left)

      if current.right:
        queue.append(current.right)
    result.append(current_level)
  return result

def undirected_path(edges, node_A, node_B):
  #receive an edge list, two nodes 
  #return a boolean

  #ex: 

  #modify edges into an adj matrix to traverse easier
  ##check if the path has been visited

  visited = set()

  graph = build_graph(edges)
  return has_path(graph, node_A, node_B, visited)

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

def connected_components_count(graph):
  #keep count 
  #iterate through neighbor
  #keep track of nodes seen



  count = 0
  visited = set()


  for node in graph: 
    if explore(graph, node, visited):
      count += 1
  return count

def explore(graph, current, visited):
  if current in visited:
    return False

  visited.add(current)
  
  for neighbor in graph[current]:
    explore(graph,neighbor, visited)
    
  return True


def largest_component(graph):
  #receive a graph and node
  #return largest size in 


  visited = set()
  max_size = 0
  
  for node in graph:
    size = explore(graph, node, visited)
    if size > max_size:
      max_size = size
  return max_size

def explore(graph, node, visited):
  if node in visited:
    return 0

  visited.add(node)
  
  size = 1

  for neighbor in graph[node]:
    size += explore(graph, neighbor, visited)
  return size
      
    def running_sum(numbers):
  #receive a list of integers
  #return a list of the running total

  #have an empty list
  #iterate through each number and add to a running total
  #then add in the number to the list
  #return list

  result = []
  total = 0

  for num in numbers:
    total += num
    result.append(total)

  return result
    
      def connected_components_count(graph):
  #receive a graph
  #return the # of connected connected_components_count

  #ex: 

  #iterate through each node in the graph
  #track if it's been visited
  #mark it as one of the component 
  #return connected_components_count

  visited = set()
  count = 0

  for node in graph:
    if explore(graph, node, visited):
      count += 1
  return count

def explore(graph, node, visited):
  if node in visited:
    return False

  visited.add(node)

  for neighbor in graph[node]:
    explore(graph, neighbor, visited)
  return True

  