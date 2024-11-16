function hasCycle(graph) {
  //if a node is revisited while still in the stack, there's a cycle
  //use two sets

  //create two Sets
  //create a dfs function
  //check if the stack has a node, return true;
  //check if visited.has(node) return false;
  //add node to visited
  //add node to stack
  //for each neighbor of node in graph
  //if dfs(neighbor) is true
  //return true
  //else remove node from stack
  //return false

  let visited = new Set();
  let stack = new Set();

  const dfs = (node) => {
    console.log(visited, stack);
    if (stack.has(node)) return true;
    if (visited.has(node)) return false;

    visited.add(node);
    stack.add(node);

    for (const neighbor of graph[node]) {
      if (dfs(neighbor)) return true;
    }
    stack.delete(node);
    return false;
  };
  for (const node in graph) {
    if (dfs(node)) return true;
  }
  return false;
}

console.log(
  hasCycle({
    A: ["B"],
    B: ["C"],
    C: ["D"],
    D: [],
  })
);

function