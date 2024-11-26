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

function wallsandWells(matrix) {
  //receive a 2d matrix
  //return min directions to get to destination
  //initialize the row and cols
  //in the queue, it's holding x, y, and distance
  //as we traverse along
  //check it's new neighbors to see if they are 0's and 1s
  //increment steps
}

function quadrant(x, y) {
  //receive two integers for x and y
  //return what qudrant they exist in 1,2,3,4

  //ex: (-3, -4) => 3
  //ex: (100, 100) => 1

  //check if x and y are both positive, return 1
  //check if x and y are both negative, return 3
  //check if x is positive and y is negative, return 4
  //check if x is negative, and y is positive, return 2

  if (x > 0 && y > 0) return 1;
  if (x < 0 && y < 0) return 3;
  if (x > 0 && y < 0) return 4;
  if (x < 0 && y > 0) return 2;
}

function differenceInAges(ages) {
  //receive an array of ages (positive)
  //return an array of [youngestAge, oldestAge, difference between ages]

  //ex: [52, 3, 5, 21] => [3, 52, 49]

  //find mind for youngestAge
  //find old for oldestAge
  //find the difference between two
  //slot in between arrays

  let youngestAge = Math.min(...ages);
  let oldestAge = Math.max(...ages);
  let difference = oldestAge - youngestAge;
  return [youngestAge, oldestAge, difference];
}
