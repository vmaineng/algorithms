function taskAssignment(k, tasks) {
  //receive number of workers (k) and an array of positive integers
  //return min total time and pair tasks

  //sort the tasks from smallest to biggest
  //pair the smallest with the biggest duration
  //continue pairing until all tasks are assigned

  const taskIndices = tasks.map((task, index) => [task, index]);
  //taskIndices = [[1, 0], [3, 1], [5, 2], [3, 3], [1, 4], [4, 5]]

  taskIndices.sort((a, b) => a[0] - b[0]);
  //sort by task
  //ex: [[1, 0], [1, 4], [3, 1], [3, 3], [4, 5], [5, 2]]

  const pairs = [];

  let left = 0;
  let right = taskIndices.length - 1;

  while (left < right) {
    const pair = [taskIndices[left][1], taskIndices[right][1]];
    //taskIndices[left][1] = b/c need index
    //taskIndices[left][0] would access the taskDuration.
    //taskIndices[left][1] accesses the originalIndex.

    pairs.push(pair);
    left++;
    right--;
  }
  return pairs;
}

// Do not edit the line below.
exports.taskAssignment = taskAssignment;

// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function removeDuplicatesFromLinkedList(linkedList) {
  //receive a SLL in sorted order
  //return the a LL where there are no duplicates
  // 1 -> 1 -> 2 -> 3 -> null => 1 -> 2 -> 3 -> null

  //iterate through LL while current and the next node is not null
  //compare the two values
  //if they are the same, point to the next next node
  //return ll

  let current = linkedList;

  while (current !== null && current.next !== null) {
    if (current.value === current.next.value) {
      current.next = current.next.next;
    } else {
      current = current.next;
    }
  }
  return linkedList;
}

// Do not edit the lines below.
exports.LinkedList = LinkedList;
exports.removeDuplicatesFromLinkedList = removeDuplicatesFromLinkedList;

// Do not edit the class below except
// for the depthFirstSearch method.
// Feel free to add new properties
// and methods to the class.
class Node {
    constructor(name) {
      this.name = name;
      this.children = [];
    }
  
    addChild(name) {
      this.children.push(new Node(name));
      return this;
    }
  
    depthFirstSearch(array) {
  //pushes the name of the node
      //goes through each children of the node
      //calls DFS on each child and add them into the array
      //return array
  
  // Recursive Addition: Inside each recursive call:
  
  // The child node’s name is added to the array when array.push(this.name) runs for that child.
  // This process continues for each child node, going as deep as possible into the tree before backtracking.
  
      array.push(this.name);
      for (const child of this.children ) {
        child.depthFirstSearch(array)
      }
    }
    return array;
  }
  
  // Do not edit the line below.
  exports.Node = Node;
  
  function riverSizes(matrix) {
    //receive a matrix
    //return the an array of where the river lies
  
    //use helper functions to traverse each river, count its size, and mark the cells as visited
  
    //create a visited matrix to track which cells have already been processed
    //loop through each cell in the matrix
    //if found an unvisited '1', initiate dfs or bfs to determine river size
    //and mark all connected cells as visited
    //add size of each river to the results array
  
    const sizes = []; //stores the size of found rivers
    const visited = matrix.map(row => row.map(() => false)); //track visited cells
  
    for (let i = 0; i < matrix.length;i++) {
      for (let j = 0; j < matrix[i].length; j++) {
        if (visited[i][j]) continue;
        traverseNode(i, j, matrix, visited, sizes); // uses a stack called nodeExplore to perform DFS
      }
    }
    return sizes;
  }
  
  function traverseNode(i, j, matrix, visited, sizes) {
  let currentRiverSize = 0;
    const nodesToExplore = [[i, j]] //stack for DFS
  
    while (nodesToExplore.length) { //for each node visited, count if it is a river
      const currentNode = nodesToExplore.pop();
      const [currentI, currentJ] = currentNode;
  
      if (visited[currentI][currentJ]) continue;
      visited[currentI][currentJ] = true;
  
  if (matrix[currentI][currentJ] === 0) continue; //skip non-river cells;
      currentRiverSize++
  
  const unvisitedNeighbors = getUnvisitedNeighbors(currentI, currentJ, matrix, visited);
      for (const neighbor of unvisitedNeighbors) {
        nodesToExplore.push(neighbor);
      }
    }

    //once a full river is traverse, the size is added to sizes array
    if (currentRiverSize > 0) sizes.push(currentRiverSize);
  }
  
//explore neighbors - returns valid neighbors that haven't been visited;
//helps expand DFS to adjacent cells

  function getUnvisitedNeighbors(i, j, matrix, visited) {
    const unvisitedNeighbors = [];
    // Check neighbors: up, down, left, right
    if (i > 0 && !visited[i-1][j]) unvisitedNeighbors.push([i-1, j]); //up
    if (i < matrix.length - 1 && !visited[i + 1][j]) unvisitedNeighbors.push([i + 1, j]); //down
    if (j > 0 && !visited[i][j-1]) unvisitedNeighbors.push([i, j-1]); //left
    if (j < matrix[0].length - 1 && !visited [i][j + 1]) unvisitedNeighbors.push([i, j + 1]); //right
    return unvisitedNeighbors
    
  }
  
  // Do not edit the line below.
  exports.riverSizes = riverSizes;
  
  // This is an input class. Do not edit.
class AncestralTree {
    constructor(name) {
      this.name = name;
      this.ancestor = null;
    }
  }
  
  function getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo) {
  let currentOne = descendantOne;
    let currentTwo = descendantTwo;
  
    while (currentOne !== currentTwo) {
      currentOne = currentOne === topAncestor ? descendantTwo : currentOne.ancestor;
      currentTwo = currentTwo === topAncestor ? descendantOne : currentTwo.ancestor;
    }
    return currentOne;
  }
  
  // Do not edit the lines below.
  exports.AncestralTree = AncestralTree;
  exports.getYoungestCommonAncestor = getYoungestCommonAncestor;
  
  // This is an input class. Do not edit.
class AncestralTree {
    constructor(name) {
      this.name = name;
      this.ancestor = null;
    }
  }
  
  function getDepth(descendant, topAnestor) {
    let depth = 0;
    while (descendant !== topAnestor) {
      depth++;
     descendant = descendant.ancestor;
    }
  return depth;
  }
  
  function getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo) {
    //receive the top node
    //return the node where both descendant nodes meet
  
    //obj = find the parentNode where two nodes "merge together" or meet in the tree structure
    //calc depth of each node
    //then equalize depths
    //move both nodes up until they meet
    //return the yca
  
    const depthOne = getDepth(descendantOne, topAncestor);
    const depthTwo = getDepth(descendantTwo, topAncestor);
  
    if (depthOne > depthTwo) {
      return backTrack(descendantOne, descendantTwo, depthOne - depthTwo)
    }else {
      return backTrack(descendantTwo, descendantOne, depthTwo - depthOne)
    }
  }
  
  // Do not edit the lines below.
  exports.AncestralTree = AncestralTree;
  exports.getYoungestCommonAncestor = getYoungestCommonAncestor;
  
  class Ship {
    constructor(draft, crew) {
      this.draft = draft
      this.crew = crew
    }
    
    //YOUR CODE HERE...
    isWorthIt() {
  //draft = total ship weight
      //crew = # of humans
      //eaach crew + 1.5
      //draft - crew weight > 20, return true
      //else return false
      
      let crewWeight = this.crew* 1.5
     let newWeight = this.draft - crewWeight
     
     if (newWeight > 20) {
       return true
     } else { 
     return false; 
     }
      }
  }