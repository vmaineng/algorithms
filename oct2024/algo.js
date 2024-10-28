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

  // This is an input class. Do not edit.
class BinaryTree {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  function heightBalancedBinaryTree(tree) {
  //receive the root node of a tree
    //return true if balanced, else false
  
    //if tree is empty, return true
  
    //recursively call: traverse through left, traverse through right
    //keep track of height
    //if height exceeds 1 , then return false
    //else traverse through entire tree, return true
  
    if (!tree) return true;
  
    function calcHeight(tree, height) {
      const leftHeight = calcHeight(tree.left, height + 1)
      const rightHeight = calcHeight(tree.right, height + 1)
  
      maxHeight = Math.max (leftHeight, rightHeight)
    }
  
    return tree.balanced
  }
  
  // Do not edit the lines below.
  exports.BinaryTree = BinaryTree;
  exports.heightBalancedBinaryTree = heightBalancedBinaryTree;
  
  function Dog (breed) {
    this.breed = breed;
  }
  
  var snoopy = new Dog("Beagle");
  
  snoopy.bark = function() {
    return "Woof";
  };
  
  var scoobydoo = new Dog("Great Dane");
  
  scoobydoo.bark = function() {
    return "Woof";
  }

  class Dog {
    constructor(breed) {
    this.breed = breed;
}
  bark() {
    return "Woof"
  }
 
  }
  
  var snoopy = new Dog("Beagle");
  
  snoopy.bark()
  
  var scoobydoo = new Dog("Great Dane");
  
  scoobydoo.bark()
  
  function getDrinkByProfession(param){
    //receive an input of string letters
      //return the output of a string associated with it
      
      //'RaPPer' => 'Cristal'
      
      //lowercase the params
      //check if the params is in the object
      //return the value associated with it
      
      
      const drinkObj = {
      "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal"
    }
    
    const lowerCaseParam = param.toLowerCase()
    
    if (drinkObj[lowerCaseParam]) {
      return drinkObj[lowerCaseParam]
    } else {
      return "Beer"
    }
    }

    class Person {
        constructor(name) {
          this.name = name;
        }
      
      greet(yourName) {
        return `Hello ${yourName}, my name is ${this.name}`;
      }
    }      

    function reverseWordsInString(string) {
        // Write your code here.
      let result = "";
      
          
          let i = string.length - 1; 
      let word = "";
        
          while (i >= 0) {
              const char = string[i];
              if (char === " ") {
                  result += word + " ";
                  //reset
                  word = "";
              } else word = char + word;
              i--;
          }
      
          return result + word
      }
      
      // Do not edit the line below.
      exports.reverseWordsInString = reverseWordsInString;
      
      function reverseWordsInString(string) {
        //receive a string of words in a string
        //return the words reversed
        //'hello world' => "world hello"
      
        //create a new string
        //iterate at the end of the string
        //add it in to new string
        //check if it is a space, then add space
        //else add in word
        //return new string
      
        let newString = "";
        let word = "";
      
        for (let i = string.length - 1; i >= 0; i--) {
          if (string[i] === " ") {
            console.log(string[i]);
            newString += word + " ";
            word = "";
          } else {
            word = string[i] + word;
          }
        }
        return newString + word;
      }
      
      // Do not edit the line below.
      exports.reverseWordsInString = reverseWordsInString;
      
      console.log(reverseWordsInString("hello world"));
      
      function isValidSubsequence(array, sequence) {
        //receive two arrays of integers (pos and neg)
        //return boolean ; true if sequence is in array, else false
        //[3,225,1,4,7,-78], [3, 7,11,8,9] => false
      
        //edge case: if sequence's length > array => false
      
        //create indexs on array and sequence
        //iterate through both arrays
        //if you find that the values match, increment both pointers
        //return if index of seq has reached end of array
      
        if (sequence.length > array.length) return false;
      
        let arrayIdx = 0;
        let seqIdx = 0;
      
        while (arrayIdx < array.length && seqIdx < sequence.length) {
          if (array[arrayIdx] === sequence[seqIdx]) seqIdx++;
          arrayIdx++;
        }
        return seqIdx === sequence.length;
      }
      
      // Do not edit the line below.
      exports.isValidSubsequence = isValidSubsequence;
      
      function tournamentWinner(competitions, results) {
        //receive an array of array of teams, and an array of results
        //return which team was the winner
        //[
        //  Home        away
        //[ "Fashion", "Makeup"],
        //["Shoes", "Fashion"],
        //["Makeup", "Fashion"]
        //]
      
        //[0,0,1] => Fashion, Fashion, Fashion => winner Fashion
      
        //keep track of score with the teams as key
        //iterate through array based on the results received
        //iterate through object to see who has the most point, return the key (team)
      
        let scores = {};
        let currentBestTeam = "";
        scores[currentBestTeam] = 0;
      
        for (let i = 0; i < competitions.length; i++) {
          const [homeTeam, awayTeam] = competitions[i]; //good to deconstruct
          const result = results[i];
          const winningTeam = result === 1 ? homeTeam : awayTeam;
      
          if (!scores[winningTeam]) {
            scores[winningTeam] = 0;
          }
          scores[winningTeam] += 1;
      
          if (scores[winningTeam] > scores[currentBestTeam]) {
            currentBestTeam = winningTeam;
          }
        }
        return currentBestTeam;
      }
      
      // Do not edit the line below.
      exports.tournamentWinner = tournamentWinner;
      
      function checkThreeAndTwo(array) {
        //receive an array of 5 strings of either 'a', 'b', or 'c',
          //return true if array contains 3 of same values and 2 of same values
          //['a', 'a', 'a', 'b', 'a'] => false
          
          //sorted order? 
        
          //keep count of values seen
          
          //iterate through the object to check if there are 3 of values and 2 of values
          
          let objCount = { };
          
          for (let char of array){
            if (!objCount[char]) {
              objCount[char] = 0
            }
        objCount[char] += 1
          }
        
        let hasThree = false;
          let hasTwo = false;
        
        for (let key in objCount) {
         if (objCount[key] === 3) {
          hasThree = true;
         } else if (objCount[key] === 2) {
           hasTwo = true;
         }
        }
        return hasThree && hasTwo
        }

        function checkThreeAndTwo(array) {
            //receive an array of fixed chars
              //return true if 3 values & 2 values, else false
              
              //initialize an object to the fixed chars
              //iterate trhough the array
              //increment the counts
              //return if values matches
              
              let objCount = {"a": 0, "b": 0, "c": 0};
              
              for (let char of array) {
            objCount[char]++
            }
            
            const counts = Object.values(objCount);
              return counts.includes(3) && counts.includes(2)
            }

            class Guesser {
                constructor(number, lives) {
                  this.number = number;
                  this.lives = lives;
                }
                
                guess(n) {
                 if (!this.lives ) {
                   throw new Error('Expect error already dead')
                 }  
              
              if (n === this.number) {
                   return true
                 } else {
               this.lives--
                   return false
                  
                 }
                }
              }
              
              //receives integer for number and lives
              //return true if user guess number right
              //else false & lose a life
              //if guess > limit, throw an error

              class Cat extends Animal {
                speak() {
                  return `${this.name}` + ' meows.'
                }
              }

              function tournamentWinner(competitions, results) {
                //receive an array of array for compeitions (homeTeam, awayTeam) and an array results
                  //return the winningTeam based on results
                
                //iterate through compeitions
                  //keep track of their points from results
                  //find the max score
                  //return winning team
                
                  let scores = {};
                  let currentBestTeam = "";
                  scores[currentBestTeam] = 0;
                
                  for (let i = 0; i < competitions.length; i++) {
                    const [homeTeam, awayTeam] = competitions[i]
                    const result = results[i]
                    const winningTeam = result === 1 ? homeTeam : awayTeam
                
                if (!scores[winningTeam]) {
                  scores[winningTeam] = 0
                 }
                scores[winningTeam]++
                
                if (scores[winningTeam] > scores[currentBestTeam]) {
                  currentBestTeam = winningTeam
                }
                  }
                return currentBestTeam
                
                }
                
                // Do not edit the line below.
                exports.tournamentWinner = tournamentWinner;
                
                function bestSeat(seats) {
                    //receive an array of 0 (open seats) & 1(reserved seats)
                     //return the index of a good seat
                   
                   //iterate through seats
                     //have a pointer at beginning and a pointer seraching next to it
                     //if it's a 1, check before and after if it's a 0, then return the index
                     //else keep looking
                     //return -1 after looking b/c no seats
                   
                     if (!seats) return -1;
                   
                   let bestSeat = -1;
                     let maxSpace = 0;
                   
                     let left = 0;
                     while (left < seats.length) {
                       let right = left + 1;
                       while (right < seats.length && seats[right] === 0) {
                         right+=1;
                       }
                   const availableSpace = right - left - 1;
                       if (availableSpace > maxSpace) {
                         bestSeat = Math.floor((left + right) /2);
                         maxSpace = availableSpace
                       }
                       left = right;
                     }
                   return bestSeat
                     
                   }
                   
                   // Do not edit the line below.
                   exports.bestSeat = bestSeat;
                   
                   function smallestDifference(arrayOne, arrayTwo) {
                    //receive two arrays of unsorted integers
                      //return an array with pairs closest to 0
                      //[3, 2, -1]
                      // [0, 4, 2]
                      //=> [2, 2]
                    
                      //edge case: If one array is empty, then can't return pairs
                      //or both arrays are empty, return an empty array
                    
                      //initialize an empty array to return the pair
                    
                      //iterate through both arrays
                      //keep pointer at the first value in the arrays
                      //check if total is close to 0, add in to the array
                      //else keep iterating
                    
                      let smallestDiff = Infinity;
                      let pairArray = [];
                    
                     for (let i = 0;i < arrayOne.length;i++) {
                       for (let j = 0; j < arrayTwo.length; j++) {
                         let currentDiff = Math.abs(arrayOne[i] - arrayTwo[j])
                         if (currentDiff < smallestDiff) {
                           smallestDiff = currentDiff
                           pairArray = [arrayOne[i], arrayTwo[j]]
                         }
                       }
                     }
                      return pairArray
                    }
                    
                    // Do not edit the line below.
                    exports.smallestDifference = smallestDifference;
                    
                    function past(h, m, s){
                        //receive integers for h, m, and s
                          //return milliseconds
                          
                          //if all 0 then return 0
                          
                          //divide all my 1 milliseconds
                        
                        //past(1,1, 1) => 1* 360mins *1000 =60000, 1 * 60mins, 1* 1000
                        
                        //hour = h * 360 * 1000
                          //min = m * 60 * 1000
                          //sec = s * 1000
                          
                        
                        let total = 0
                          
                          if (h > 0 || m > 0 || s > 0) {
                         let totalHour = h * 3600 *1000
                         let totalMin = m * 60 * 1000
                         let sec = s * 1000
                        total = totalHour + totalMin + sec
                          }
                        return total
                        
                        // To convert hours, minutes, and seconds into milliseconds:
                        
                        // 1 hour = 60 minutes × 60 seconds × 1000 milliseconds = 3,600,000 milliseconds
                        // 1 minute = 60 seconds × 1000 milliseconds = 60,000 milliseconds
                        // 1 second = 1,000 milliseconds
                        }

                        function findSum(matrix) {
                            let sum = 0;
                            for (let i = 0; i < matrix.length; i++) {
                              for (let j = 0; j < matrix[i].length; j++) {
                                sum += matrix[i][j];
                              }
                            }
                            return sum;
                          }
                          
                          /**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function(matrix) {
    //receive a 2d matrix of cols and rows;
    //return a matrix back where the columns are swapped with row numbers
    //[[1,2],
    //[3, 4]]

    //[[1, 3
    //2, 4]]

    //if matrix is empty, return an empty array back
    ///initialize an array at the beginning
    //iterate through the cols
    //then create another array
    //iterate through rows
    //push in row values
    //push in col value sinto the rows
    //return the array

    if (!matrix) return [];

let transposed = []
  for(let j = 0; j < matrix[0].length; j++) {
    let newRow = [];
    for (let i = 0; i < matrix.length;i++) {
        newRow.push(matrix[i][j]);
    }
    transposed.push(newRow)
  }
  return transposed
};


function findMax(matrix) {
    //receive a 2D array
    //return the max element found in matrix
    //[[1,2, 3]
    //[4, 8, 2]] => 8

    //initialize a variable to -Infinity (to account for negative values)
    //iterate through rows
    //then iterate through columns
    //check if the value is > what we currently have
    //set it as the new maxValue
    //return the maxValue

    let maxValue = -Infinity

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] > maxValue){
                maxValue = matrix[i][j]
            }
        }
    }
    return maxValue
}

//time : O(m*n)
//space : O(1)

function countNegs(matrix) {
    //receive a 2D matrix
    //return an integer of count of negatives values in 2d

    //iterate through rows and values
    //if they are <0, increment count
    //return count

    let count = 0;

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length;j++) {
            if (matrix[i][j] < 0) {
                count++
            }
        }
    }
    return count
}

//time:O(m * n)

// This is an input class. Do not edit.
class BST {
    constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
    }
  }
  
  function findKthLargestValueInBst(tree, k) {
   //receive a BST, and integer to find the kth largest value in bst
    //return the node value of kth largest value
  
    //edge case if tree is empty, return 0
  
    //brute force: traverse through every node in the array
    //using inOrderTraversal
  
  //create an array
    //do recrusive call on three node, and array
    //then return the array.length - k b/c it's toward the endo fthe array
  
  
  let sortedValues = []
   inOrderTraversal(tree, sortedValues);
    return sortedValues[sortedValues.length - k];
  
    function inOrderTraversal(node, sortedValues) {
      if (node === null) return;
  
      inOrderTraversal (node.left, sortedValues)
      sortedValues.push(node.value);
      inOrderTraversal(node.right, sortedValues);
    }
    //optimized: using reverse inOrder
  
  // let kthLargestValue = null;
  
  //   function helperKthLargest(tree) {
  //     if (!tree) return;
  
  //     helperKthLargest(tree.right);
  //     if (k === 0) return;
  //     kthLargestValue = tree.value;
  //     k--;
  //     helperKthLargest(tree.left;)
  //   }
  // helperKthLargest(tree);
  //   return kthLargestValue;
  }
  
  // Do not edit the lines below.
  exports.BST = BST;
  exports.findKthLargestValueInBst = findKthLargestValueInBst;
  
  function  calculateAge(birthYear, countYears) {
    //receive two integers
    //return 'You are...year(s) old'
  
  //calculateAge(2012, 2018) => 2018 - 2012 = 6 years old
  
  //calc the age
    //if the age > 1, return 'You are ...years old',
    //else return "you are 1 year old."
  
  let age = countYears - birthYear;
    if (age > 1) {
      return "You are " + `${age}` + " years old."
    } else if (age === 1){
      return "You are 1 year old."
    } else if (age === - 1) {
      return 'You will be born in ' + Math.abs(age) + " year."
    } else if (age < 0) {
      return 'You will be born in ' + Math.abs(age) + " years."
    } else {
      return 'You were born this very year!'
    }
  }
  
  
  /**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    //receive two arrays of integers
    //return an array of arrays fwhere values do not exist in the other array

    //[1, 2, 3], [3, 4, 2]
    //=[[1], [4]]

    //edge cases: if the array is empty, return the other array
    //if both arrays are empty, return empty arrays

    //brute force: have a pointer at first array
    //have a pointer on second array
    //iterate through entire second array
    //check if the value is the same in the array
    //else, add it tothe uqniue arrays
    //return array

    if (!nums1) return [nums2];
    if (!nums2) return [nums1];

    let uniqueVals = [];
    let uniqueVals2 = [];

    for (let i = 0; i < nums1.length; i++) {
        if ((!nums2.includes(nums1[i])) && !uniqueVals.includes(nums1[i])) {
            uniqueVals.push(nums1[i])
        }
    }

    for (let i = 0; i < nums2.length; i++) {
        if (!nums1.includes(nums2[i])  && !uniqueVals2.includes(nums2[i])) {
            uniqueVals2.push(nums2[i])
        }
    }
    return [uniqueVals, uniqueVals2]
};

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    //receive two arrays of integers
    //return an array of arrays fwhere values do not exist in the other array

    //[1, 2, 3], [3, 4, 2]
    //=[[1], [4]]

    //edge cases: if the array is empty, return the other array
    //if both arrays are empty, return empty arrays

    //brute force: have a pointer at first array
    //have a pointer on second array
    //iterate through entire second array
    //check if the value is the same in the array
    //else, add it tothe uqniue arrays
    //return array

//     if (!nums1) return [nums2];
//     if (!nums2) return [nums1];

//     let uniqueVals = [];
//     let uniqueVals2 = [];

//     for (let i = 0; i < nums1.length; i++) {
//         if ((!nums2.includes(nums1[i])) && !uniqueVals.includes(nums1[i])) {
//             uniqueVals.push(nums1[i])
//         }
//     }

//     for (let i = 0; i < nums2.length; i++) {
//         if (!nums1.includes(nums2[i])  && !uniqueVals2.includes(nums2[i])) {
//             uniqueVals2.push(nums2[i])
//         }
//     }
//     return [uniqueVals, uniqueVals2]

//optimized; using Sets
//initialize both arrays into sets
//check if nums1's values exists in nums2.
//if not, then return the arrays
//push into the array

let uniqueSet1 = new Set(nums1);
let uniqueSet2 = new Set(nums2);

let array1 = []
let array2 = []

for (let char of uniqueSet1) {
    if (!uniqueSet2.has(char)) {
        array1.push(char)
    }
}

for (let char of uniqueSet2) {
    if (!uniqueSet1.has(char)) {
        array2.push(char)
    }
}
return [array1, array2]
};

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {number}
 */
var pathSum = function(root, targetSum) {
    //receive the root node of a tree and an integer for targetSum
    //return the # of paths that totals up to targetSum

    //initialize a variable for totalPaths
    //use dfs -> go as deep as possible, and add each value up
    //if the ttotal is equal to targetSum, increment TotalPaths
    //else, keep looking

    //edge cases: if rootnode is empty, return 0
    //else add in root node's value from left and right

    //base case: if the total is > targetSum, move to th enext node
    //else keep looking

    if (!root) return 0;

 let totalPaths = findsPaths(root, targetSum)
  totalPaths += findsPaths(root.left, targetSum);
  totalPaths += findsPaths(root.right, targetSum);
  return totalPaths;
};

function findsPaths(node, targetSum) {
    if (!node) return 0;
    let paths = 0;

    if (node.val === targetSum) {
        paths = 1
    }
    paths += findsPaths(node.left, targetSum - node.val)
    paths += findsPaths(node.right, targetSum - node.val)
    return paths
}

/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function(rooms) {
    //receive an array of arrays
    //return true if you can visit all rooms in arrays, else false

    //ex: 2
    //keys for 1 and 3
    //room1: 1, 0, 3
    //no way for us to get to room 2 - key is in room 2
    //and can't get in to room 2

    //use bfs; 
    //add 

    let visited = new Array(rooms.length).fill(false);
    let queue = [0];
    visited[0] = true;

    while (queue.length > 0) {
        console.log('queue:', queue)
        let currentRoom = queue.shift();
        for (let key of rooms[currentRoom]) {
            console.log(currentRoom, rooms[currentRoom])
            if (!visited[key]) {
                visited[key] = true;
                queue.push(key)
            }
        }
    }


return visited.every(room => room === true)


};

/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function(rooms) {
    //receieve an array of rooms
    //return true if can visit all rooms, else return fals
    
    //ex: [[1], [3, 1]] => false b/c I need to visit room 2
    
    //initialize an array with same length of rooms filled with false
    //visit the rooms bfs with queue
    //if we can visit in the array, flip it to true
    //then add key into the queue
    
    let visitedRooms = new Array(rooms.length).fill(false);
    let queue = [0];
    visitedRooms[0] = true;
    let visitedCount = 1;
    
    while (queue.length > 0) {
        const currentRoom = queue.shift();
        for (let key of rooms[currentRoom]) {
            if (!visitedRooms[key]) {
                visitedRooms[key] = true;
                visitedCount++
                queue.push(key)
    
                if (visitedCount === rooms.length) {
                    return true;
                }
            }
        }
    }
    return visitedCount === rooms.length;
    
    
    };

    /**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    //receive an array of integers (postive and negative)
    //return an answer of array where at each value it is the product of all the numbers in the array except at the pointer
    
    //[-3, 6, 2] => [12, -6, -18]
    // i
    //        j 
    
    //brute force: 
    //create an answer array to hold the product values
    //create a pointer starting the at first index, 
    //create a second pointer starting at the first index
    //create a multiplier, set to 1;
    //mutiply every value that we see for j by the mutiplier
    //take the values from the answer array * values at i;
    //return the array
    
    
    
    //edge case: if the array only has one number, return the array itself;
    
    // for (let i = 0; i < nums.length;i++) {
    //     let multiplier = 1
    //     for (let j = 0; j < nums.length; j++) {
    //         if (i !==j ){
    //             multiplier *= nums[j]
    //         }
    //         answer[i] = multiplier
    //     }
    // }
    // return answer
    //time: O(n^2)
    //space: O(1)
    
    let answer = [];
    let leftArray = new Array(nums.length).fill(1);
    let rightArray = new Array(nums.length).fill(1);
    
    //optimized
    //create an answer array to hold each value
    //iterate through starting at the first index in the array
    //single loop - capture all the values from the left
    //another single loop - capture all the values from the right - set in the values
    //using a mutliplier, set to 1, multiply all the left values into the answer array by 1
    //right values - use mutliplier of 1, multiply by right values
    //return the answer array
    
    //[-3, 6, 2]
    //leftArray = [ -3, 6, 2]
                        // j
    //rightArray = [ ]
    
    let leftMultiplier = 1
    for (let i = 0; i <= nums.length; i++) {
        leftArray[i] *= leftMultiplier
    }
    
    let rightMultiplier = 1
    for (let i = nums.length - 1; i>=0; i--) {
        rightArray[i] *= rightMultiplier
    }
    
    answer[i] *= leftArray[i]
    
    return answer
    
    };
    
    /**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    //receive an array of integers of pos and negative
    //return an array back of all products except self value
    
    //[1,2] => [2, 1]
    
    //initialize an empty array
    //iterate through nums
    //create another pointer to point at the beginning of index
    //create a multiplie to multiply by 1
    //multiplier * j's value
    //add the answer into the array at designated spot in i
    
    // let answer = [];
    
    // for (let i = 0; i < nums.length; i++) {
    //     let multiplier = 1;
    //     for (let j = 0; j < nums.length; j++) {
    //         if (i !== j) {
    //             multiplier *= nums[j]
    //         }
    //     }
    //     answer[i] = multiplier
    // }
    // return answer
    
    //optimized way:
    //create an answer array
    //iterate left and add to answer array
    //iterate right down to 0, add to answer array
    //return answer array
    
    let answer = []
    
    let leftMultiplier= 1
    for (let i = 0; i < nums.length; i++) {
        answer[i] = leftMultiplier
        console.log(answer[i])
        leftMultiplier *= nums[i]
    }
    
    
    let rightMultiplier = 1;
    for (let i = nums.length - 1; i >=0 ; i--) {
        answer[i] *= rightMultiplier
        rightMultiplier *= nums[i]
    }
    
    return answer
    };
    
    /**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    //receive a string of lowercase letters
    //return longest substring with unique chars
    //'rhinocareus' => 'rhinoca' => 7
    
    //edge case: if string is empty
    
    //create a new set
    //keep track of each letter
    //keep extending right side of window until it's no longer unique
    //then push in the left side window
    //keep track of the max Count you've seen
    //return the count
    
    let uniqueChars = new Set();
    let left = 0;
    let right = 0;
    let count = 0;
    
    while (right < s.length) {
        if (!uniqueChars.has(s[right])) {
            uniqueChars.add(s[right])
            right++
        } else {
            uniqueChars.delete(s[left]) 
            left++
            
        }
        count = Math.max(count, uniqueChars.size)
    }
    return count
    
    }
    
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
  
  function spiralTraverse(array) {
    //receive an array of arrays
     //return one array back
   
     //edge case, could one array be longer than the other?
   
     //start at the left corner and go around, 
     //once you hit an end, decrement row down
     //and column down
   
     let result = [];
   let top = 0;
     let bottom = array.length - 1;
     let left = 0;
     let right = array[0].length - 1;
   
     while (top <= bottom && left <= right) {
       for (let i = left; i <= right; i++) {
         result.push(array[top][i])
       }
       top++
       
       for (let i = top; i <= bottom; i++) {
         result.push(array[i][right])
       }
       right--;
   
       if (top <= bottom) {
         for (let i = right; i >= left; i--) {
          result.push(array[bottom][i])
         }
         bottom--;
       }
   
       if (left <= right) {
         for (let i = bottom; i >= top; i--) {
           result.push(array[i][left])
         }
         left++
       }
   }
    return result
   }
   
   // Do not edit the line below.
   exports.spiralTraverse = spiralTraverse;
   
   function longestSeq(nums) {
    //receive an integer array of nums
    //return the longest increasing subsequence
    //ex: [3, 2, 5, ,6, 7, 8] => 4 b/c of [5,6, 7, 8]

//intiailize a count
//increment through the nums
//check if the value before it is increasing
//increment count
//if the value is not, update the count to max values seen
//then move pointer

let count = 0;
for (let i = 0; i < nums.length;i++) {
    for (let j = i + 1; j < nums.length; j++) {
        if (nums[j] < nums[i]) {
            count = Math.max(count, i - j)
        } 
    }
}
return count;

//time: O(n^2)
//space: O(1)

//optimized; do it in place
//initialize a count
//check the value before if it's less
//increment count
//else start count all over again

let count = 0;

for (let i = 1; i<nums.length; i++) {
    if (nums[i-1] > nums[i]) {
        count = Math.max(count, i - (i-1))
    }
}
return count

//time:O(n)
//space:O(1)

}

function mostWater(height) {
    //receive an array of positive integers
    //return max amount of water a container can store
    //[3, 5, 6,3] => [3, 3] => 4 distances apart; 3 * 4 = 12

    //initialize a count to keep track of max water a container can store
    //iterate through the array
    //take the min height of i and j (length)
    //and take the width
    //update count with new l x w
    //return count

    let maxAmount = 0;
    for (let i = 0; i < height.length; i++) {
        for (let j = i + 1; j < height.length; j++) {
            const minHeight = Math.min(height[i], height[j])
            const currentarea = minHeight * (j - i)
            maxAmount = Math.max(maxAmount, currentarea) 
        }
    }
    return maxAmount

    //time: O(n^2)
    //space: O(1)

    //optimized: two pointers
    //check from left to right
    //grab the minHeight and width
    //update maxAmount

    const left = 0;
    const right = height.length - 1;
    const maxAmount =0;
    
    while (left < right) {
   
      const minHeight = Math.min (height[left], height[right])
      const currentWidth = minHeight * (left - right)
      maxAmount = Math.max(currentWidth, maxAmount)
    if (height[left]< height[right]) {
        left++
    } else {
        right--
    }

}
return maxAmount
}

//time: O(n);
//space: O(1)

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    //receive an array of sorted integers and unique values
    //return the min element in the array

    //ex:[1, 2, 3, 4] => 1
    //[3, 4, 1, 2] => 1
 //1.        4
//Math.min(...nums) => O(n)

//initialize left pointer and right pointer 
//find the middle 
//check if the middle is our min value
//check if the middle value < left value 
//or if the middle value > right value

let min = nums[0];
let left = 0;
let right = nums.length - 1;

while (left <= right) {
    if (nums[left] < nums[right]) {
        min = Math.min(nums[left], min)
        break;
    }
    const middle = (Math.floor(left + right) /2)
    min = Math.min(min, nums[middle])
    if (nums[middle] < nums[left]) {
    
        right = middle - 1
    } else {
        left = middle + 1
    }
}
return min

};

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
    
    let maxArea = 0;
    
    for (let i = 0; i < height.length; i++) {
        for (let j = i + 1; j < height.length; j++) {
            const smallestHeight = Math.min(height[i], height[j]);
            const width = j - i;
            area = smallestHeight * width
            maxArea = Math.max(maxArea, area)
        }
    }
    
    return maxArea
    };

    var maxArea = function(height) {
        //receive an array of positive integers
        //return max amt of water can store
    
        //[3, 5, 2, 1, 4, 5] => [ 5 , 5] and they are 5 apart 5 * 5 = 25
    
        //keep track of maxAmount of water
        //iterate through height
        //keep a pointer on the first value
        //look at all the other possible maxAmt
        //check the smallest height * width
        //update maxAmt
        //return maxAmt
    
        let maxAmount = 0
        for (let i = 0; i < height.length;i++) {
            for (let j = i + 1; j < height.length; j++) {
             let minHeight = Math.min(height[i], height[j])
             let maxArea = minHeight * (j - i)
             maxAmount = Math.max(maxAmount, maxArea)   
            }
        }
        return maxAmount
    
        //time: O(n^2);
        //space: O(1)
    
        //optimized method:
        //create a pointer at left side and pointer at right side
        //find the min height of left or right
        //find the width
        //calculate l * x to get the max area
       //update maxAmount
       ////check if left side smaller or right side smaller
       //move left pointer up
       //else move right pointer
       //return maxArea
    
       let left = 0;
       let right = height.length - 1;
       let maxAmount = 0;
    
       while (left < right) {
        let minHeight = Math.min(height[left], height[right]);
        let currentArea = minHeight * (right - left)
        maxAmount = Math.max(currentArea, maxAmount)
        if (height[left] < height[right]) {
            left++
        } else {
            right--
        }
       }
    return maxAmount
    
    //time: O(n);
    //space:O(1)

    function dfs(matrix) {
        //if grid is empty, return 0,
        //capture the rows and cols
        //intiialize a count for island at 0
        
        //create a dfs function that takes in the row and col
        //checks the boundaries and if it's already water
        
        //expore all 4 directions, top, left, right, bottom
        //iterate through each cell in the grid
        //check if the value is a 1
        //increment island count
        //else continue searching
        //return island count
        
        if (!matrix) return 0;
        
        let islandCount = 0; 
        let rows = matrix.length;
        let cols = matrix[0].length;
        
        function dfs(row, col) {
            if (row < 0 || row >= rows || col < 0 || col >= cols || matrix[row][col] === '0') {
                return;
            }
        
            grid[row][col] = '0'
        
            dfs(row-1, col);//top
            dfs(row + 1, col)//bottom
            dfs(row, col - 1); //left;
            dfs(row, col + 1); //right
        }
        
        for (let row = 0; row < rows; row++) {
            for (let col = 0; col < cols; col++) {
                if (grid[row][col] === '1') {
                    islandCount++
                    dfs(row, col)
                }
            }
        }
        return islandCount
        }

        /**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    //prefix and postfix
    //p: an unsorted array of integers nums
    //return the length of longest consecutive elemtns sequence
    
    
    
    //brute force would be to sort it
    //sort the array
    //iterate through it
    //sliding window technique
    //keep count of it is equal the value + 1
    //if next element isn't adjacent to the value
    //reset count to 0; 
    //time: O(n log n)
    //space: O(1) b/c not creating new space
    
    // nums.sort((a,b) => a - b); 
    
    if (nums.length === 0) return 0; 
    if (nums.length === 1) return 1; 
    
    let count = 0; 
    //let temp = 1; //start with 1 b/c there's at least one element 
    
    // for (let i = 0; i < nums.length - 1; i++) {
    //     if (nums[i] === nums[i + 1] - 1) { //prefix
    //         console.log(nums[i], nums[i+1] - 1)
    //         temp++
    //         count = Math.max(count, temp)
    //     } else if (nums[i] === nums[i+ 1]) {
    // console.log(nums[i], nums[i+1])
    //         count = Math.max(count, temp)
    //     } else {
    //         temp = 1;
    //         count = Math.max(count, temp)
    //     }    
    // }
     
    //  return count;
    
    //optimzed:
    //initialize a Set to remove duplicates
    //iterate through it
    //increment a count
    //increment to check next element
    
    let newSet = new Set(nums);
    
    for (let num of nums) {
        if (!newSet.has(num - 1)) {
            let total = 0;
    
            while (newSet.has(num)) {
                total++;
                num++;
            }
            count = Math.max(count, total)
        }
    }
    return count;
    
    //
    
    };

    /**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
function topKFrequent(nums, k) {
    //receive an array of integers and an integer for k
    //return the k most frequent elements back in an array
  
    //[1, 1, 1, 1, 2, 3], k = 1 => [1]
  
    //edge cases: ex: k = 3, [1, 1, 1, 2, 2]
  
    //use a Map
  //iterate through the array, keept rack of the values seen
  //sort the elements in the by frequency amount
  //slice out the top k elements
  
  const frequencyMap = new Map();
  
  for (let num of nums) {
   frequencyMap.set(num, (frequencyMap.get(num) || 0 )+ 1)
  }
  
  const sorted = [...frequencyMap.entries()].sort((a,b) => b[1] - a[1]);
  
  return sorted.slice(0,k).map(entry => entry[0])
  
  }
  
  //time: O(n log n)
  //space: O(n)

  function majorityElement(array) {
    //receive an array of integers unsorted
      //return the majority element; appears more than half of its indices
      //[3, 2, 5, 6, 6, 6,3] => -1
    
    //initialize a frequencyCounter pattern
      //then check which element appeared more than half of the length
      //return the element
    
    if (array.length ===0) return -1;
    
      let obj = {};
    let maxVal = 0;
      let maxEle =0
    
      for (let num of array){
      if (!obj[num]) {
        obj[num] = 0
      }
        obj[num]++
      }
    
    for (let key in obj) {
      if (obj[key] > maxVal) {
       maxVal = obj[key]
        maxEle = parseInt(key)
      }
    }
    
    if (maxVal > Math.floor(array.length /2) ) {
      return maxEle
    }
    return -1;
    }
    
    // Do not edit the line below.
    exports.majorityElement = majorityElement;
}
function billboard(name, price = 30){
    //receive a name
      //return total amount it cost to add a name
      //'mary jo' => length of name is 7, 7 * 30 = 210
      
      //iterate up to the names length, add the price everytime
      //return total
      
      let total = 0;
      for (let i = 0; i < name.length; i++) {
        total += price
      }
    return total
    } 

     //receive an array of integers
    //return true if the number of occurrences in each value is all unique, else return false

    //[3, 4, 4, 5, 5] => false b/c 2 4's and 2 5's

    //brute force: FrequencyCounter
    //create an object
    //store the occurences of values seen into the object
    //iterate through to check the values if ssame as others
    //if they are, return false automatically
    //else return true

    let obj = {};
    for (let num of arra) {
        obj[num] = (obj[num] || 1) + 1
    }

    for (let key in obj){
        if (obj[key] === obj[key]) {
            return false
        }
    }
    return true;
};

/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    let freqObj = {};

    for (let num of arr) {
        freqObj[num] = (freqObj[num] || 0) + 1
    }

    let freqVals = new Set()

for (let key in freqObj){
    if (freqVals.has(freqObj[key])){
        return false
    } else {
        freqVals.add(freqObj[key])
    }
}
    return true
}

//time: O(n+m)
//space:O(n)

function getLength(arr){
    //return length of arr
    return arr.length
  }
  function getFirst(arr){
    //return the first element of arr
    return arr.shift()
  }
  function getLast(arr){
    //return the last element of arr
    return arr[arr.length -1]
  }
  function pushElement(arr){
    var el=1;
    //push el to arr
    arr.push(el)
    return arr
  }
  function popElement(arr){
    //pop an element from arr
    arr.pop()
    return arr
  }

  function capitalize(s){
    //receive a string lowercase with no spaces
      //return an array with even numbers captialize odd numbers capitalize 
    
    //'hello' => ['hElLo', 'HeLlO']
      
      //initialize an empty string
      //iterate through the strings
      //if the index mod 2 === 0, (even),
      //capitzlize it
      //return the string
      
      //iterate through the string again for odd 
      
      //return array
      
      //if string is empty, return an empty array
      if (!s) return ["", ""];
      
      let capAlternative = '';
      let capOdd = '';
      let answer = []
    
      for (let i =0; i < s.length; i++) {
        if (i % 2 === 0) {
          const upper = s[i].toUpperCase()
          capAlternative += upper
        } else {
          capAlternative += s[i]
        }
      }
    
    for (let i = 0; i < s.length; i++) {
    if (i % 2 !== 0) {
      const upperOdd = s[i].toUpperCase()
      capOdd += upperOdd
    } else {
      capOdd += s[i]
    }
    }
        answer.push(capAlternative, capOdd)
      return answer
    };

    function sweetAndSavory(dishes, target) {
        //receive an array of dishes - negative = sweet dish; positive = savory dish, and a target
          //the abs value of the integer presents intensity of a flavor
        
          //return one savory and one sweet to meet the target in an array
          
          //edge case: if dishes empty, return an empty array
        
          //separate the dishes array into a sweet array (negative) and savory (positive)
          //sort both arrays in values
          //have a pointer at the first value in the arrays
          //capture the pair
          //else if the total of the two pairs is < target, move pointer in savory
          //else move pointer in sweet
          //return pair
        
          if (dishes.length === 0) return [0,0];
        
          let sweet = [];
          let savory = [];
          let pair = [0, 0]
          let bestDiff = Infinity;
        
          for (let num of dishes){
            if (num < 0) {
              sweet.push(num)
            } else {
              savory.push(num)
            }
          }
        
          if (sweet.length === 0 || savory.length === 0) return [0, 0];
        
        for (let i = 0; i < sweet.length; i++) {
          for (let j = 0; j < savory.length; j++) {
            let sum = sweet[i] + savory[j]
            let diff = Math.abs(target - sum)
            if (diff < bestDiff) {
              bestDiff = diff
              pair = [sweet[i], savory[j]]
            } 
          }
        }
          
        return pair
        }
        
        
        // Do not edit the line below.
        exports.sweetAndSavory = sweetAndSavory;
        
        function sweetAndSavory(dishes, target) {
            // receive an array of integers: neg = sweet; pos = savory, and integer target
            //return one savory dish and one sweet dish that equals target
            //[-3, 4, 5, -2] 1 => [-3, 4]
          
            //if dishes are empty, return [0,  0]
          
            //create 2 arrays: 1 for sweet and 1 for savory
            //sort arrays
            //iterate through both arrays
            //check if the difference is smaller than the current difference
            //update the best pairs
            //return best pairs
          
            if (dishes.length === 0) return [0,0]
          
            let bestDiff = Infinity;
            let pair= [0,0]
          
            let sweet = dishes.filter((num) => num < 0).sort((a,b) => a -b);
            let savory = dishes.filter((num) => num > 0).sort((a,b) => a - b);
          
            for (let i = 0; i < sweet.length; i++) {
              for (let j = 0; j < savory.length; j++) {
                let sum = sweet[i] + savory[j]
                  if (sum <= target) {
                  let diff = (target - sum)
                  if (diff < bestDiff) {
                    bestDiff = diff;
                    pair = [sweet[i], savory[j]]
                }
                }
              }
            }
            return pair
          }
          
          // Do not edit the line below.
          exports.sweetAndSavory = sweetAndSavory;
          

          function sweetAndSavory(dishes, target) {
            // receive an array of integers: neg = sweet; pos = savory, and integer target
            //return one savory dish and one sweet dish that equals target
            //[-3, 4, 5, -2] 1 => [-3, 4]
          
            //if dishes are empty, return [0,  0]
          
            //create 2 arrays: 1 for sweet and 1 for savory
            //sort arrays
            //iterate through both arrays
            //check if the difference is smaller than the current difference
            //update the best pairs
            //return best pairs
          
            if (dishes.length === 0) return [0,0]
          
            let bestDiff = Infinity;
            let pair= [0,0]
          
            let sweet = dishes.filter((num) => num < 0).sort((a,b) => b - a);
            let savory = dishes.filter((num) => num > 0).sort((a,b) => a - b);
          
          let i = 0;
            let j = 0;
            
          while (i < sweet.length && j < savory.length) {
                let sum = sweet[i] + savory[j]
            
                  if (sum <= target) {
                  let diff = (target - sum)
                  if (diff < bestDiff) {
                    bestDiff = diff;
                    pair = [sweet[i], savory[j]]
                } 
                  j++
                } else {
                i++
                }    
          }
            return pair
          }
          
          // Do not edit the line below.
          exports.sweetAndSavory = sweetAndSavory;
          