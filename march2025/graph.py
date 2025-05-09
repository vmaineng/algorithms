matrix = [
    [0, 1, 1, 0],  # Node 0
    [1, 0, 1, 0],  # Node 1
    [1, 1, 0, 1],  # Node 2
    [0, 0, 1, 0]   # Node 3
]

node_values = [5, 3, 7, 2] #arbitary values
#              0  1  2  3
# Print node values
print("Node values:")
for i in range(len(matrix)):
    print(f"Node {i}: {node_values[i]}")

# Print connections
print("\nConnections:")
for i in range(len(matrix)):
    connections = [j for j in range(len(matrix[i])) if matrix[i][j] == 1]
    print(f"Node {i} connects to: {connections}")

const breadthFirstSearch = (graph, startNode) => {
  const queue = [startNode]
  while queue.length > 0 { 
    const current = queue.shift()
    console.log(current)
    for (const neighbor of graph[current]) {
      queue.push(neighbor)
    }   
  }
}

def has_path(graph, src, dst):
  #dfs
  #receives a graph, node, and distance
  #return True if path from src to destination nodes
  #ex: graph = { 
  #  'f': ['g']
  #   'h': []
  #}

  #graph, 'f', 'g' => True
  #graph, 'f', 'h' => False

  #base case: 
  #if src == dist, return True
  #else recursively call to it's next neighbors

  # if src == dist:
  #   return True
  # for neighbor in graph[src]:
  #  if(has_path(graph, neighbor, dist) == True):
  #    return True
  # return False

  #bfs
  from collections import dequeue

  dequeue = [src]
  while dequeue.length > 0:
    current = dequeue.popleft()

    if current == dst:
      return True
      
    for neighbor in graph[current]:
      queue.push(neighbor)
    return False
       
       def how_much_i_love_you(nb_petals):
    #receive a flower of x amount of petals
    #return the saying that the last petal struck on 
    #ex: '3' => 'a lot'
    #ex: '10' => 'madly'
    
    #edge cases: if flower with no petal
    
    #take the # of petals % length of array
    
    sayings= ["I love you", 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    
    return sayings[nb_petals % (len(sayings)) - 1]