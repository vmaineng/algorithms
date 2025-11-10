def dfs(graph, source) {
    #receive a graph and a source node to start off
    #initialize a stack with source
    #while stack is not empty
    #pop it off
    #print it
    #add to the end of the stack
    
    stack = [source]
    current = stack[-1]
    while len(stack) > 0:
        current = stack.pop()
        for neighbor in graph[current]:
            stack.append(neighbor)
    
}

def dfs(graph, source){
    current = source
    for neighbor in graph[current]:
       dfs(graph, neighbor)
}


from collections import deque 
def bfs(graph, source) { 
    #initialize a deque
    #while the deque is not empty
    #iterate through each neighbor
    queue = deque([start])
    while len(queue) > 0: 
       current = queue.popleft()
       for neighbor in graph[current]:
          queue.append(neighbor)
}


def has_path(graph, src, dst):
  #receive graph, src node, and dst node
  #
  if src==dst:
    return True
  for neighbor in graph[src]:
    if (has_path(graph, neighbor, dst) == True):
      return True
  return False

def undirected_path(edges, node_A, node_B):
  #TURN PATH INTO adjency matrix
  #then check if it has PATH
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
    if has_path(graph, neighbor, dst, visited) == True:
      return True
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

def connected_components_count(graph):
  visited = set()
  count = 0

  for node in graph:
    if explore(graph, node, visited) == True:
      count += 1

  return count

def explore(graph, current, visited):
  if current in visited:
    return False

  visited.add(current)

  for neighbor in graph[current]:
    explore(graph, neighbor, visited)
  return True

def largest_component(graph):
  #receive an adj list
  #return largest size
  #ex: 

  #keep track of largest size
  #iterate through each node
  largest = 0
  visited = set()

  for node in graph:
    size = explore(graph, node, visited)
    if size > largest:
      largest = size
  return largest
 

def explore(graph, node, visited):
  if node in visited:
    return 0

  visited.add(node)

  size = 1

  for neighbor in graph[node]:
    size += explore(graph, node, visited)
  return size

def largest_component(graph):
  #receive an adj list
  #return largest size

  #iterate through each node
  #then iterate through the neighbors, count size

  largest = 0
  visited = set()

  for node in graph:
    size = explore(graph, node, visited)
    if size > largest:
      largest = size
  return largest

def explore(graph, node, visited):
  if node in visited:
    return 0

  visited.add(node)

  size = 1

  for neighbor in graph[node]:
    size += explore(graph, neighbor, visited)
  return size

from collections import deque

def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)
  visited = set([node_A])
  queue = deque([(node_A, 0)])

  while len(queue) > 0:
    node, distance = queue.popleft()

    if node == node_B:
      return distance

    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor, distance + 1)
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


def island_count(grid):
  #receive a grid
  #return the count of islands on grid

  #isolate rows and cols
  #iterate through if grid is 'L'
  #increment island count
  #return count

  count = 0
  rows, cols = len(grid), len(grid[0])

  def explore(row, col):
    if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 'W':
      return 0
    grid[row][col] = "W"

    explore(row + 1, col)
    explore(row -1, col)
    explore(row, col + 1)
    explore(row, col - 1)
    

  for row in range(rows):
    for col in range(cols):
      if grid[row][col] == 'L':
        explore(row, col)
        count += 1
  return count

from preloaded import DECK

def define_suit(card):
    #recceive a string starting with a number and a char
    #return what suite it is 
    
    #ex: '3C' => 'clubs'
    #ex: '4D' => 'diamonds'
    
    #capture the last letter int he string
    #if it is c, clubs
    #if it is d, it is diamonds
    #if it is h, it is hearts
    #if it is s, spades
    
    if card[1] == 'C':
        return 'clubs'
    elif card[1] == 'D':
        return 'diamonds'
    elif card[1] == 'H':
        return 'hearts'
    else:
        return 'spades'
    
    from preloaded import DECK

def define_suit(card):
    #create an object
    #do a search up in O(1)
    
    suits = { 
    'C': 'clubs',
    'S': 'spades',
    'D': 'diamonds',
    'H': 'hearts'}
    
    return suits[card[-1]]