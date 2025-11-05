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