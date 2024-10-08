function minHeightBst(array, left = 0, right = array.length - 1) {
    //receive an array of sorted integers
      //return a root node of bst
      //[1, 3, 4] => 
      // 3
      //1 4
    
      //grab the middle value as root node

      //base case: if (endindx < startIdxx) return null
    
      const midIdx = Math.floor((left + right) /2);
const valueToAdd = array[midIdx];
    
    if (bst === null) 
    return new BST(valueToAdd)
    } else {
      middle.insert(middle.right)
    }
      return bst
    }
    
    class BST {
      constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
      }
    
      insert(value) {
        if (value < this.value) {
          if (this.left === null) {
            this.left = new BST(value);
          } else {
            this.left.insert(value);
          }
        } else {
          if (this.right === null) {
            this.right = new BST(value);
          } else {
            this.right.insert(value);
          }
        }
      }
    }
    
    // Do not edit the line below.
    exports.minHeightBst = minHeightBst;
    
    function minHeightBst(array, left = 0, right = array.length - 1) {
        //receive an array of sorted integers
          //return a root node of bst
          //[1, 3, 4] => 
          // 3
          //1 4
        
          //grab the middle value as root node
        
        if (left > right) return null;
        
          const middleIdx = Math.floor((left + right) /2 );
         const bst = new BST(array[middleIdx]);
          bst.left = minHeightBst(array, left, middleIdx-1);
          bst.right = minHeightBst(array, middleIdx+1, right);
          return bst
        
        }
        
        class BST {
          constructor(value) {
            this.value = value;
            this.left = null;
            this.right = null;
          }
        
          insert(value) {
            if (value < this.value) {
              if (this.left === null) {
                this.left = new BST(value);
              } else {
                this.left.insert(value);
              }
            } else {
              if (this.right === null) {
                this.right = new BST(value);
              } else {
                this.right.insert(value);
              }
            }
          }
        }
        
        // Do not edit the line below.
        exports.minHeightBst = minHeightBst;
        
        // Do not edit the class below except for
// the insert, contains, and remove methods.
// Feel free to add new properties and methods
// to the class.
class BST {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  
    insert(value) {
      // Write your code here.
      // Do not edit the return statement of this method.
  
  //instantiate a currentNode;
  //while the loop is true,
      //check if the value is less than the currentNode's value
      //check if the left side is null
      //then add it in, else add in the current left
      //same with right side
  
      let currentNode = this; //current instance of the bst
      while (true) {
        if (value < currentNode.value){
          if (currentNode.left === null){
            currentNode.left = new BST(value)
            break;
          } else {
             currentNode = currentNode.left
          }
        } else {
          if (currentNode.right === null){
            currentNode.right = new BST(value)
            break;
          } else {
            currentNode = currentNode.right;
          }
        }
      }
    
      
      return this;
    }
  
    contains(value) {
      let currentNode = this;
  
      while (currentNode !== null){
        if (value < currentNode.value){
          currentNode = currentNode.left
        } else if (value > currentNode.value){
          currentNode = currentNode.right
        } else {
          return true;
        }
      }
      return false
    }
  
    remove(value) {
      // Write your code here.
      // Do not edit the return statement of this method.
      return this;
    }
  }
  
  // Do not edit the line below.
  exports.BST = BST;
  
  /**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    //receive an array of integers
    //return the max amt of water a container can store
    
    //ex: [3, 5, 2]max is 3; l x h = 1, h 3 =3
    
    //brute force
    //iterate through each one of them and create a max
    
    //optimized:
    //initialize a varaible to hold max
    //create two pointers - starting from left to right
    //grab smallest height at left or right
    //take w * height
    //return max
    
    let left = 0;
    let right = height.length - 1;
    let maxArea = 0;
    
    while (left < right) {
    
    const smallestHeight = Math.min(height[left], height[right]);
    
    const area = smallestHeight * (left - right + 1)
    
    if (height[left] > height[right]) {
        left++
    } else {
        right--
    }
    
    }
    return maxArea
    };

    /**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    //receive an array of integers of pos and neg, k amount of integer
    //return the max average value
    
    //[3, 5, 2, 5], 2 => 4
    
    //start at the first pointer
    //add all the numbers up to k index
    //then divide by k
    
    let maxAverage = -Infinity
    
    for (let i = 0; i <= nums.length -k; i++) {
    let sum = 0;
    
    for (let j = i; j < i + k; j++) {
        sum+= nums[j]
    }
    let average = sum /k;
    maxAverage = Math.max(average, maxAverage)
    }
    return maxAverage
    }

    /**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    //receive an array of integers, and k (integer of target)
    //return max operations of numbers can be performed
    
    //[0, 1, 3,2], 1 => 
    //[0, 1] = 1
    
    //edge case: if nums array is empty
    
    //keep track of count
    //iterate through the entire array starting first value
    //create a second pointer at second value
    //check if the total is equal to k
    //if so, slice it out to create a new array
    //increment count
    //check the array again
    //increment count if needed
    //return count
    
    if (!nums) return 0;
    
    let count = 0;
    
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === k) {
                count++
                 nums.splice(j, 1);
                nums.splice(i, 1); 
            i--;
            break;
            }
        }
    }
    return count
    };

    function firstNonRepeatingCharacter(string) {
        //receive a string of letters (all lowercase)
          //return the index of the string's first nonRepeat char
        
          //'hiehsljf' => '1' b/c of 'i'
        
          //edge case: if string is empty, return -1;
        
          //if string is 1, return 0
        
          //brute force: 
          //keep a pointer on the first value
          //create a second pointer on the second value
          //check if the value are equal to each other,
          //if they are not, move on to the next one
          //if not found after searching entire string, return i
          //else return -1
        
          if (!string) return -1; 
          if (string.length === 1) return 0;
        
          for (let i = 0; i < string.length;i++) {
            let foundDuplicate = false;
            for (let j = 0; j < string.length; j++) {
              if (string[i] === string[j] && i !== j) foundDuplicate = true;
            }
            if (!foundDuplicate) return i
          }
        return -1
        
          //start j at index 0 b/c when i is at index 3, j will check the values again starting from index 0
        
        }
        
        // Do not edit the line below.
        exports.firstNonRepeatingCharacter = firstNonRepeatingCharacter;
        
        // This is an input class. Do not edit.
class BST {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  function findKthLargestValueInBst(tree, k) {
  //receive the root node of a tree and an integer stating the largest integer contained in the bst
  
    //edge case: k exceeds tree's length
  
    //brute force;
    //solve it using an array and return the end of the array - k
    //base case: if k = 0, return the last array
  
    //else, traverse through left, then traverse through right, push nodes into an array
  
    const sortedValues = [];
    inOrderTraverse(tree, sortedValues);
    return sortedValues[sortedValues.length - k];
  
    function inOrderTraverse(node, sortedValues) {
      if (node == null) return ;
      inOrderTraverse(node.left, sortedValues);
      sortedValues.push(node.value)
      inOrderTraverse(node.right, sortedValues);
  }
    
  }
  
  // Do not edit the lines below.
  exports.BST = BST;
  exports.findKthLargestValueInBst = findKthLargestValueInBst;
  
  // This is an input class. Do not edit.
class BinaryTree {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  //O(n) time for all nodes; O(h) space due to recursion stack
  function heightBalancedBinaryTree(tree) {
  //receive the root node of a binary tree;
  //return true if height is balanced, else false
  
    //if height is empty, return true;
  
    //traverse through left sub tree, count how many edges
    //traverse through right subtree, count how many edges
  
  
    function calcHeight(node, height, balance) {
        if (!node) return height;
      const leftHeight = calcHeight(node.left, height+1, balance);
      const rightHeight = calcHeight(node.right, height+1, balance);
  
      if (Math.abs(leftHeight - rightHeight) > 1) balance.isBalanced = false;
      return Math.max(leftHeight, rightHeight)
    }
    const balance = {isBalanced: true};
    calcHeight(tree, 0, balance);
    return balance.isBalanced;
  
  }
  
  // Do not edit the lines below.
  exports.BinaryTree = BinaryTree;
  exports.heightBalancedBinaryTree = heightBalancedBinaryTree;
  
  \// This is an input class. Do not edit.
class BinaryTree {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
      this.parent = null;
    }
  }
  
  // If the node has a right child, traverse down to find the leftmost node in the right subtree.
  // If the node does not have a right child, traverse up the tree using the parent pointer until you find a node where the given node is in the left subtree (i.e., where the node is the left child of its parent).
  // If no such node exists (e.g., the node is the rightmost node), return null.
  
  
  function findSuccessor(tree, node) {
  if (node.right) {
    return getLeftMostChild(node.right);
  }
    return getRightmostParent(node);
  }
  
  function getLeftMostChild(node) {
    let current = node;
    while (current.left) {
      current = current.left;
    }
    return current;
  }
  
  function getRightmostParent(node) {
    let current = node;
    while (current.parent && current.parent.right === current) {
      current = current.parent;
    }
    return current.parent;
  }
  // Do not edit the lines below.
  exports.BinaryTree = BinaryTree;
  exports.findSuccessor = findSuccessor;
  

  function reversePolishNotation(tokens) {
    //receive an an array of strings of integers and arthmetic operators
    //return an integer result
  
    const stack = [];
  
    for (const token of tokens) {
      if (token === '+') {
        stack.push(stack.pop() + stack.pop())
      } else if (token === '-') {
        const firstNum = stack.pop();
        stack.push(stack.pop() - firstNum);
      } else if (token === '*') {
        stack.push(stack.pop() * stack.pop())
      } else if (token === '/') {
        const firstNum = stack.pop()
        stack.push(Math.trunc(stack.pop() / firstNum))
      } else {
        stack.push(parseInt(token)); //push the string numbers as integers into the stack
      }
    }
    return stack.pop()
  }
  
  // Do not edit the line below.
  exports.reversePolishNotation = reversePolishNotation;
  
  function formatMoney(amount){
    //receive a float number
      //return the float number in dollar and cents
      //(4.99) => $4.99
      
      //parseInt the amount
      //with dollars signs
      
      return '$'+ `${amount.toFixed(2)}`
      
      
    }

    /**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    //receive the head of a linked list
    //return true if cycle, else falase
    
    if (!head) return false;
    
    //fast and slow pointer
    //if fast meets slow = true
    //else false
    
        let slow = head;
        let fast = head;
    
    while (fast.next !== null && fast.next.next !== null) {
            slow.next;
     fast.next.next;
        if (fast === slow) {
            return true
        }
    
    }
    
    return false;
     
    };

    //receive the root node of a tree
//return the tree inverted

//.     1
//    /. \
//. 32.   5


// => 1
//  /. \
// 5.   32

//recursive: 
//time: O(n)
//space: O(d) number of nodes the queue will hold

//base case: if tree is empty, return null;
//recursive case: 
//swap nodes
//call function on the left subtree, then call function on the right subtree
//return tree

if (root === null) return root;

let temp = root.left;
root.left = root.right;
root.right = temp;

invertTree(root.left);
invertTree(root.right);
return root;

//iterative: using bfs - level order traversal, uses a queue, FIFO
//create a queue to hold the nodes from tree
//as long the queue is not empty
//swap the nodes
//add them to the array being returned back$

let queue = [root]
while (queue.length > 0) {
    let current = queue.shift();

    if (current === null) continue;
    let temp = current.left
    current.left = current.right;
    current.right = temp; 

    if (current.left) queue.push(current.left);
    if (current.right) queue.push(current.right);
}
return root
//time: O(n)
//space:O(n) #number of nodes

function isSantaClausable(obj) {
    //receive an object
    //return true if the object's methods exists, else false
    
    //check if the functions exists
    
    return typeof obj.sayHoHoHo === 'function' && typeof obj.distributeGifts === 'function'&& typeof obj.goDownTheChimney === 'function'
  }