from collections import deque

def shortest_path(edges, node_A, node_B):
  #receive an edge list, two nodes
  #return the length of shortest path between A and B

  #convert our edge list into an adj matrix,
  #iterate through the adj matrix
  #bfs = queue => intitialize with a deque
  #keep track of the distance associated with the node
  #create a set to keep track of nodes visited
  #if node has been seen, Return False
  #otherwise, iterate through the neighbor nodes
  #add 1 to the distance
  #after looking thorugh everything, return -1

  graph = build_graph(edges)
  queue = deque([(node_A , 0)])
  visited = set([node_A])

  while queue:
    node, distance = queue.popleft()
    if node ==node_B:
      return distance
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, distance + 1))
  return -1
  

def build_graph(edges):
  graph ={}
  for edge in edges:
    a,b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w','z'))