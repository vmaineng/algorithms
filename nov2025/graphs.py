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