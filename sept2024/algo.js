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

  function findSmallestInt(arr) {
    //receive an array of integers 9pos and negative
      //return tsmallest number
      
      //[34, 2, 5, -6, 6] => -6
      
      //sort the values smallest to biggest
      //grab the first number
      
      arr.sort((a,b) => a - b);
      return arr[0]
    
    //time: O(n log n)
    //space: O(n) => sorting 
    
    //optimized method:
      //capture the first value as smallest
      //iterate through the rest of the array integers
      //check if the value is smaller, than the current smallest one
      //update if necessary
      //return smallest value
    
      let smallestValue = arr[0]
    
    for (let i = 1; i < arr.length; i++) {
      if (arr[i] < smallestValue) {
        smallestValue = arr[i]
      }
      }
    return smallestValue
    }
    
    //time:O(n)
    //space:O(1)
    
    
    //spread out the values and use Math.min
    return Math.min(...arr)
    
    }
    
    //time:O(n)
    //space:O(n)

    function nodeDepths(root) {
        //receive root of a tree
         //return the depths of tree
       
         //if tree is empty, return 0;
       
         //create a stack
         //add the root to the stack
         //while stack is not empty, pop off the nodes, and add to the depths
         //return depths
       
         if (!root) return 0;
       let sumOfDepths = 0;
         let stack = [{node: root, depth:0}];
       
         while (stack.length > 0 ) {
           const { node, depth} = stack.pop();
           if (node === null) continue;
           sumOfDepths += depth
           stack.push({node: node.left, depth: depth + 1})
           stack.push({node: node.right, depth: depth + 1})
         }
         return sumOfDepths
       }
       
       // This is the class of the input binary tree.
       class BinaryTree {
         constructor(value) {
           this.value = value;
           this.left = null;
           this.right = null;
         }
       }
       
       // Do not edit the line below.
       exports.nodeDepths = nodeDepths;
       
       function sumOfDifferences(arr) {
        //receive an array of integers
        //return the sum of the difference in pairs in descending order
        //[34, 2, -4] = [ 32, 2, -4] = (32 - 4) + (2 - -4) 28 + 6 = 34
        
        //if array is empty, return 0
        //initialize a total to 0 that the differences will add to
        //iterate through the array
        //calc the difference between two numbers
        //add to the total
        //move on to the rest of the array
        //return the total
        
        if (!arr) return 0;
        
        arr.sort((a,b) => b - a);
        
        let total = 0;
        
        for (let i = 0; i < arr.length - 1; i++) {
          let pairTotal = arr[i] - arr[i + 1]
          total += pairTotal
        }
      return total
      }
      function solve(s){
        //receive a string of characters with no spaces
          //return the string of char uppercase if majority of letters uppercase, else lowercase it
          //'warS' => 'wars'
          //'WaRs' => 'wars' => equal amount of uppercase and lowercase = change all to lowercase
          
          //edge case: if string length is empty, return an empty string
          
          //keep track of count of uppercase and lowercase
          //if they're equal, lowercase them
          //else if majority are uppercase, then uppercase teh words
          //return string
          
          if (s.length === 0) return '';
          
        let upperCaseCount = 0;
          let lowerCaseCount = 0;
          
          for (let char of s) {
            if (char === char.toLowerCase()) {
              lowerCaseCount++
            } else {
              upperCaseCount++
            }
          }
        
        if (upperCaseCount > lowerCaseCount) {
          return s.toUpperCase()
        } else {
         return s.toLowerCase()
        }
        }

        // Do not edit the class below except
// for the breadthFirstSearch method.
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
  
    breadthFirstSearch(array) {
  //return the final array with all nodes inside
      //initialize our queue with current node (root node)
      //while queue is not empty,
      //grab first node (FIFO)
      //add in the node to array
      //then add in their children into the queue
      //get out of the w hile loop
      //return the array
  const queue = [this]; 
      while (queue.length > 0) {
        const current = queue.shift();
        array.push(current.name);
        for (const child of current.children) {
          queue.push(child)
        }
      }
      return array;
    }
    //O(v+e) time; O(v) space (return length of V)
  }
  
  // Do not edit the line below.
  exports.Node = Node;
  
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
  //dfs = goes deep
      //add children to the array
      //push in parent's node
      //then iterate through it's children
      
    array.push(this.name) //push in the parent node
      //then go through each child
      //each child will repeat line 22
      //where it gets pushed in and it traverse through it's child
      //return array
      for (const child of this.children) {
    child.depthFirstSearch(array)
      }
      return array;
   
    }
  }
  
  // Do not edit the line below.
  exports.Node = Node;
  
  function twoColorable(edges) {
    //receive a graph with verties and edges
      //return true if can make graph two-colorable
      //else false
    
      //create a stack that has same length of edges
      //grab the first node
    
    
      const colors = new Array(edges.length).fill(null);
      colors[0] = true;
      const stack = [0]; //use stack for dfs
    
      //start with the first node and color it with true
    
      while (stack.length > 0) {
        const node = stack.pop();
        for (const connection of edges[node]) {
          if (colors[connection] === null) {
            colors[connection] = !colors[node];
            stack.push(connection);
          } else if (colors[connection] === colors[node]) {
            return false;
          }
        }
      }
      return true;
    }
    
    // Do not edit the line below.
    exports.twoColorable = twoColorable;
    
    function generateDocument(characters, document) {
        //receive a string of chars with spaces, uppercase and lowercase letters
          //return true if you can make the document string with characters string
          //document('hello', 'hi') => false b/c need 'ello'
        
          //edge case: if not the same length, can't generate the same string
          //if string is empty, return 0;
        
          //freq counter pattern
        
          //create an object
          //track how many values have been seen
          //if values is not found in document's length, return false
          //else after seaching entire string, return true
        
   
          let objChars = {};
        
          for (let char of characters) {
            if (!objChars[char]) {
             objChars[char] = 0
            }
        objChars[char]++
          }
        
        for (let char of document) {
          if (!objChars[char] || objChars[char] === 0) {
          return false;
          }
         objChars[char] -= 1
        }
        return true;
        
        }
        
        // Do not edit the line below.
        exports.generateDocument = generateDocument;
        
        function roundToNext5(n){
            //receive an integer as input
              //return the next closest multiple of 5
              
              //25 => 25
              //18 => 20 b/c 18/5; closest one is 20, so it's 20
              
              //take the integer module of 5
              //round it up
             //return what's it's difvided by
              
            return Math.ceil(n /5) * 5
            }

            function nodeDepths(root) {
                //receive a tree's root
                  //return an integer stating level of trees
                  //1 // 0 && then Node 2: Depth 1
                //Node 3: Depth 1
                //2  3 => 0 + 1 + 1 = 2, not 3.
                
                  //capture root node
                  //create a stack
                  //capture the node and depth
                  //add in depth from left side
                  //add in depth from right side
                  //return the sum of depths
                
                let sumDepths = 0;
                
                  let stack = [{node: root, depths: 0}];
                  while (stack.length > 0) {
                    const {node, depths} = stack.pop();
                    if (node === null) continue;
                    sumDepths += depths;
                    stack.push({node: node.left, depths: depths + 1});
                 stack.push({node: node.right, depths: depths + 1});
                
                  }
                return sumDepths
                }
                
                // This is the class of the input binary tree.
                class BinaryTree {
                  constructor(value) {
                    this.value = value;
                    this.left = null;
                    this.right = null;
                  }
                }
                
                // Do not edit the line below.
                exports.nodeDepths = nodeDepths;
                
                function generateDocument(characters, document) {
                    //receive a string of characters of chars and string of document of lowercase chars
                      //return true if can make document out of chars, else false
                      //'hazyew', 'hazy' => true
                    
                      //create an object of chars seen in characters
                      //then iterate through document
                      //if seen values, subtract by 1
                    
                      //if characters is missing and empty,return false
                    //return true;
                    
                      let objChars = {};
                    
                      for (let char of characters) {
                        if (!objChars[char]) {
                          objChars[char] = 1
                        }
                    objChars[char] += 1
                      }
                    
                    for (let char of document) {
                      if (!objChars[char] || objChars[char] === 0) {
                      return false
                      }
                      objChars[char] -= 1
                    }
                    return true;
                    }
                    
                    // Do not edit the line below.
                    exports.generateDocument = generateDocument;
                    function stringClean(s){
                        //receive a string of characters - letters, spaces, digits
                          //return remove numbers
                          //'h3ello, worl2d' => 'hello, world'
                          
                          //look at each characters
                          //check to see if it's a number, if it is don't add to the string
                          //return the string back
                         
                        //edge cases: string is empty, return back an empty string
                          
                          //create a varaible to hold string
                          //iterate through each characters in the string that we received
                          //check if it does not equal a number, add it to string
                          //return the string
                          
                          if (!s) return '';
                          
                          let stringWord = '';
                          
                         for (let i = 0; i < s.length; i++) {
                           if (isNaN(s[i]) || s[i] === ' ') {
                             stringWord += s[i]
                           }
                         }
                        return stringWord;
                        }
                        //time O(n) | space O(n)

                        function generateRange(min, max, step){
                            //receive 3 arguments; all integers
                              //return an array showing the range of characters, based on steps
                              //range(1, 3, 1) => [1, 2, 3]
                              
                              //create an array, push range of integers in
                              //loop all the way up to max
                              //increment by steps
                              
                              //edge case: steps can't be greater than max, return min
                              if (step > max) return [min];
                              
                              let rangeArray = [];
                              
                              for (let i = min; i <= max; i += step) {
                                rangeArray.push(i)
                              }
                            return rangeArray
                            }
                            
                            //time: array = O(N)
                            //space: array = O(N)

                            function weatherInfo (temp) {
                                const c = convertToCelsius(temp)
                                console.log("c", c)
                                if (c < 0)
                                  return (c + " is freezing temperature")
                                else
                                  return (c + " is above freezing temperature")
                              }
                              
                              function convertToCelsius (temp) {
                                const celsius = (temp - 32) * (5/9)
                                console.log("celsius", celsius)
                                return celsius
                              }

                              function nodeDepths(root) {
                                //receive the root of a tree
                                  //return an integer of how many node's depths there are
                                  // 1 => 1 depth
                                
                                
                                  //go deep left, go deep right => dfs => stack => LIFO
                                
                                  //initialize a variable to hold the root node in a stack
                                  //a variable to count how many integers
                                  //iterate through the stack while it's not empty
                                  //look at the node and add depth by 1
                                  //do for left side and right side
                                  //return level of depths
                                
                                  let stack = [{node: root, depth: 0}];
                                  let sumOfDepths = 0;
                                
                                  while (stack.length > 0) {
                                    const {node, depth} = stack.pop();
                                    if (node === null) continue;
                                    sumOfDepths += depth;
                                    stack.push({node: node.left, depth: depth + 1});
                                    stack.push({node: node.right, depth: depth + 1});
                                  }
                                  return sumOfDepths
                                }
                                
                                // This is the class of the input binary tree.
                                class BinaryTree {
                                  constructor(value) {
                                    this.value = value;
                                    this.left = null;
                                    this.right = null;
                                  }
                                }
                                
                                // Do not edit the line below.
                                exports.nodeDepths = nodeDepths;
                                
                                function nodeDepths(root, depth = 0) {
                                    //receive root node;
                                    
                                      //base case;
                                      if (!root) return 0;
                                    
                                      //recursive: 
                                      //pass in a depth parameter at 0;
                                      //traverse through left and right childs
                                     return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1) 
                                    }
                                    
                                    // This is the class of the input binary tree.
                                    class BinaryTree {
                                      constructor(value) {
                                        this.value = value;
                                        this.left = null;
                                        this.right = null;
                                      }
                                    }
                                    
                                    // Do not edit the line below.
                                    exports.nodeDepths = nodeDepths;
                                    
                                    // This is an input class. Do not edit.
class BinaryTree {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  function evaluateExpressionTree(tree) {
  //receive the root of a tree 
    //return an integer from the operators conducted
  
    //eddge case: if root tree is empty, return 0
  
    //intialize a sum
    //iterate through left side of tree
    //iterate through right side of tree
    //if the value of the node is -1, left + right
    //if value is -2, left - right
    //if valueis -3, left / right
    //if value is -4, left * right
    
  //return value
  
  //the leaf nodes represent numbers (operands), while the parent nodes (non-leaf nodes) represent operators (evaluators)
  
  if (tree.value >=0 ) return tree.value;
    const leftValue = evaluateExpressionTree(tree.left);
    const rightValue = evaluateExpressionTree(tree.right);
  
  if (tree.value === -1) return leftValue + rightValue;
    if (tree.value === -2) return leftValue - rightValue;
    if (tree.value === -3 ) return Math.trunc(leftValue / rightValue);
  
  return leftValue * rightValue
  }
  
  // Do not edit the lines below.
  exports.BinaryTree = BinaryTree;
  exports.evaluateExpressionTree = evaluateExpressionTree;

  let encoded = "";
  let count = 1;

for (let i = 1; i <= string.length; i++) {
  if (i < string.length && string[i] === string[i - 1]) {
    count++
if (count === 10) {
  encoded += "9" + string[i - 1]
  count = 1
}
  } else {
  encoded += `${count}` + string[i-1]
  count = 1
}
}
  return encoded
}
    
    // Do not edit the line below.
    exports.runLengthEncoding = runLengthEncoding;
    
    function runLengthEncoding(string) {
        //create a string to hold encoded
         //iterate through string
         //grab the first char
         //add the number
         //check if letters still equal each other and count < 9
         //return the  string
       
       let encodedString = "";
         let count = 1;
         let char = null;
       
         for (let i = 0; i < string.length; i++) {
           char = string[i]
       
       if (char === string[i + 1] && count <9) {
       count++
       } else {
         encodedString += `${count}${char}`
         count= 1;
       }
         }
         return encodedString
       }
       
       // Do not edit the line below.
       exports.runLengthEncoding = runLengthEncoding;
       
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
  array.push(this.name); //add in their parent's node
      for (const child of this.children) { //go through each children
  child.depthFirstSearch(array) //call dfs for each child
  }
    }
  return array;
  }
  
  // Do not edit the line below.
  exports.Node = Node;
  
  function animal(obj){
    //receive an object
      //return a string of the values
      //obj= {
      //name: "mary",
      //last: "joe"
    // } => 'Their name is mary joe'
    
    return `This ${obj.color} ${obj.name} has ${obj.legs} legs.`
    
    }
    
    function generateDocument(characters, document) {
        //receive a string for chars and document
         //return true if can generate document from chars, else false
       
         //'hello', 'hlo' => false; need an 'e', 'l'
       
       //edge case: if chars is empty;
         //if both chars and document, return true;
       
         //iterate through chars, keep count of frequency
         //iterate through document, each time a char is found, decrement it from the object
         //if can't find a value, return false
         //else return true;
       
         let chars = {};
       
         for (let char of characters){
           if (!chars[char]){
             chars[char] = 0
           } 
             chars[char]++
           
         }
       
         for (let char of document) {
            if (!chars[char] || chars[char] === 0) {
              return false
            }
          chars[char]--
          }
          return true
       }
       
       // Do not edit the line below.
       exports.generateDocument = generateDocument;
       
       function arrayOfProducts(array) {
        //receive an array of integers
          //return an output array where all integers of the product sums
          //[1, 2, 4] => [6, 4, 2]
        
          //create an array to store the output
          //edge cases: if array is empty, return an empty array
          //keep a pointer on first value;
          //create a second pointer to the value right of it;
          //multiply each value
          //push value into array;
          //return new array;
          
        let productArray = [];
        
          for (let i = 0; i < array.length; i++) {
            let multiplier = 1
            for (let j = 0; j < array.length; j++) {
              if (i !== j) {
                multiplier *= array[j]
              }
        productArray[i] = multiplier
            }
          }
        return productArray
        }
        
        //time:O(n^2)
        //space:O(n)
        
        // Do not edit the line below.
        exports.arrayOfProducts = arrayOfProducts;
        
        function arrayOfProducts(array) {
            //receive an array of integers unsorted
             //return an aray back with products
             //[3,2] => [2, 3]
           
             //create an array product
             //iterate through array starting at left at 0
             //add to the array product
             //iterate trhough array starting at right at the end
             //add to the array product
             //return array product
           
             let productArray = new Array(array.length).fill(1)
           
             let multipler = 1;
             for (let i = 0 ; i < array.length; i++) {
               productArray[i] = multipler
                 multipler *= array[i]
             }
           
             let rightMultipler = 1;
           for (let j = array.length - 1; j >=0; j--) {
             productArray[j] *= rightMultipler //For each element, it multiplies the existing value in productArray[j] 
             //(which already contains the product of elements to the left) by the product of elements to the right, updating the final result.
             rightMultipler *= array[j]
           }
           
           return productArray
           }
           
           // Do not edit the line below.
           exports.arrayOfProducts = arrayOfProducts;
           
           // This is an input class. Do not edit.
class BST {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  function validateBst(tree, min = -Infinity, max = Infinity) {
   //receive a root node of a tree
    //return true if bst is valid, else false
  
    //base case: if node's value is < than min, and greater than max, return false
    //recursive case: keep traversing left and checking the value, and keep traversing right and check the values
  
    if (!tree) return true;
  
    if (tree.value < min || tree.value >= max) return false;
    
  return validateBst(tree.left, min, tree.value) && validateBst(tree.right, tree.value, max)
  }
  
  // Do not edit the line below.
  exports.BST = BST;
  exports.validateBst = validateBst;
  
  // This is an input class. Do not edit.
class LinkedList {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }
  
  exports.LinkedList = LinkedList;
  
  function mergingLinkedLists(linkedListOne, linkedListTwo) {
  //receive two LL's 
    //return the node where the two LL merges
    //1 -> 2 -> 3 -> null
    // 2-> 3 -> null
  
  //return 2 -> 3
  
    //keep track of the head LL1
    //keep track of the head LL2
  
    //while the values do not equal, 
    //keep traversing
    //if we hit the null of the linked list, go look in the other LL
  //return the first current head
  
    let p1 = linkedListOne;
    let p2 = linkedListTwo;
  
    while (p1 !== p2) {
      p1 = p1 === null ? linkedListTwo : p1.next
      p2 = p2 === null ? linkedListOne : p2.next
    }
    return p1
  }
  
  // Do not edit the line below.
  exports.mergingLinkedLists = mergingLinkedLists;
  

  class TreeNode {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  // Separate function to find the longest path (or height)
  function longestPath(node) {
    if (!node) return 0;  // Base case: null node has height 0
  
    // Recursively find the height of the left and right subtrees
    let leftHeight = longestPath(node.left);
    let rightHeight = longestPath(node.right);
  
    // Return the height of the current node
    return Math.max(leftHeight, rightHeight) + 1;
  }
  
  // Main function to find the diameter
  function diameterOfBinaryTree(root) {
    let diameter = 0;  // Store the maximum diameter found
  
    function calculateDiameter(node) {
      if (!node) return 0;
  
      // Get the height of the left and right subtrees
      let leftHeight = longestPath(node.left);
      let rightHeight = longestPath(node.right);
  
      // Update the diameter if the path through this node is larger
      diameter = Math.max(diameter, leftHeight + rightHeight);
  
      // Return the height of this node
      //determines the max height of the two subtrees,
      //adds 1 for the height of the current node
      return Math.max(leftHeight, rightHeight) + 1;
    }
  
    calculateDiameter(root);  // Start the recursion from the root node
    return diameter;  // Return the largest diameter found
  }
  
  // Example binary tree
  let root = new TreeNode(1);
  root.left = new TreeNode(2);
  root.right = new TreeNode(3);
  root.left.left = new TreeNode(4);
  root.left.right = new TreeNode(5);
  
  console.log(diameterOfBinaryTree(root));  // Output: 3
  
  function invertBinaryTree(tree) {
    //receive a tree root node
      //return the tree with nodes reverted
    
      //recursive bfs - level order traversal
    
      //edge case; if tree node is empty, return null
      //traverse through left, traverse through right
      //swap
      //return tree
    
      if (!tree) return null;
    
      if (tree) {
        let temp = tree.left
        tree.left = tree.right;
        tree.right = temp
      }
    
       invertBinaryTree(tree.left)
        invertBinaryTree(tree.right) 
    
    return tree
    }
    
    // This is the class of the input binary tree.
    class BinaryTree {
      constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
      }
    }
    
    // Do not edit the line below.
    exports.invertBinaryTree = invertBinaryTree;
    
    function getPermutations(array, perm=[], output=[]) {
        // Base case: if the input array is empty, push the current permutation to output
        if (array.length === 0) {
          output.push(perm);  // Store the permutation
          return [];
        }
        
        // Iterate through the elements of the array
        for (let i = 0; i < array.length; i++) {
          let curr = array[i];  // Select the current element
          let newArr = array.filter(integer => integer !== curr);  // Create a new array excluding the current element
          let newPerm = perm.concat([curr]);  // Add the current element to the permutation path
          
          // Recursive call to continue building permutations with the new array and new permutation path
          getPermutations(newArr, newPerm, output);
        }
        
        // Once all permutations are generated, return the output
        return output;
      }
      