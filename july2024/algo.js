function kadanesAlgorithm(array) {
  // Write your code here.

  //receive an array of integers
  //return the max total
  //[1, -4, 3, 2] => 5 (3 + 2)

  //keep track of maxSum;
  //keep track of maxNumber
  //iterate through and grab each max total
  //if the maxsum < the next number, start a new total with the next number
  //return maxsum

  let maxSum = array[0];
  let maxNumber = array[0];

  for (let i = 1; i < array.length; i++) {
    maxSum = Math.max(array[i], maxSum + array[i]);
    maxNumber = Math.max(maxNumber, maxSum);
  }
  return maxNumber;
}

// Do not edit the line below.
exports.kadanesAlgorithm = kadanesAlgorithm;

function twoNumberSum(array, targetSum) {
  //receive an array of integers (pos and neg), and a target sum (integer) to reach
  //return the two values that adds up to targetSum in an array

  //[3, -3, -2, -4, 6], -6 => [-2, -4]

  //edge case if array is empty
  //need to make sure sum is two differente integers

  //iterate through the array
  //create another pointer to point to the next value
  //if you find the first instance and they are not of the same value
  //return the values

  if (!array) return [];

  for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      if (array[i] + array[j] === targetSum) {
        return [array[i], array[j]];
      }
    }
  }
  return [];
}

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;

function moveElementToEnd(array, toMove) {
  //receive an array of integers, and an integer to identify which number to move
  //return an array of integers back with all the elements === toMove towards the end
  //[1,2,3,1,4],1 => [2, 3, 4 1, 1]

  //edge cases: if array is empty

  //initialize a pointer at starting index
  //initialize a pointer at end of array
  //check if the value at beginning of array is equal toMove
  //swap the value
  //then increment left point, decrement right pointer
  //return array

  //time: O(n) - iterating through array once
  //space: O(1) - doing it in place

  if (array.length === 0) return [];

  let left = 0;
  let right = array.length - 1;

  while (left < right) {
    while (left < right && array[right] === toMove) {
      right--;
    }
    if (array[left] === toMove) {
      let temp = array[left];
      array[left] = array[right];
      array[right] = temp;
    }
    left++;
  }
  return array;
}

// Do not edit the line below.
exports.moveElementToEnd = moveElementToEnd;

function twoNumberSum(array, targetSum) {
  //receive an array of integers (pos and neg), targetSum (an integer)
  //return an array back of the two values
  //[2, 3, 5, 1], 4 => [3, 1]

  //if array is empty, return empty array

  //create an object
  //iterate through array, put the value seen as value in obj
  //check if the difference exists in obj,
  //return it
  //else store it

  if (array.length === 0) return [];

  let seenVals = {};

  for (let i = 0; i < array.length; i++) {
    let difference = targetSum - array[i];
    if (seenVals.hasOwnProperty(difference)) {
      return [seenVals[difference], array[i]];
    } else {
      seenVals[array[i]] = array[i];
    }
  }
  return [];
}

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;

function binarySearch(array, target) {
  //receive an array of sorted integers and a target number
  //return the index if the target value is found in the array, else return -1;

  //[3, 5, 6, 8, 11, 15, 23], 3 => return index 0

  //edge case: if array is empty

  //binary search algo
  //capture left(start of index) and right(end of the array) pointer
  //calc middle index, check the value
  //if the value does not equal target, check if the target is less than the middle value
  //move right pointer down
  //else if the value is greater than middle value, move left pointer up
  //else return -1;

  if (array.length === 0) return -1;

  let left = 0;
  let right = array.length - 1;

  while (left <= right) {
    let middle = Math.floor((left + right) / 2);
    if (array[middle] === target) {
      return middle;
    } else if (array[middle] > target) {
      right--;
    } else {
      left++;
    }
  }
  return -1;
}

// Do not edit the line below.
exports.binarySearch = binarySearch;

function shiftedBinarySearch(array, target) {
  //receive an array that has been shifted and a number integer target
  //return index of the target if found in the array, else return -1;
  //[1, 2, 3, 4, 5] => shifted [3, 4, 5, 1, 2], 2 => index 4

  //edge case: if array is empty, return -1

  //set up the binary algo
  //difference is add another if stmt to check if the left value is < middle idx
  //if not, return -1;

  //same set up for the right value too

  if (array.length === 0) return -1;

  let left = 0;
  let right = array.length - 1;

  while (left <= right) {
    let middleIdx = Math.floor((left + right) / 2);
    if (array[middleIdx] === target) {
      return middleIdx;
    } else if (array[left] <= array[middleIdx]) {
      // know the array is still sorted
      if (target < array[middleIdx] && target >= array[left]) {
        //check if the value is less than middleIdx value and greater than the left value
        right = middleIdx - 1;
      } else {
        left = middleIdx + 1;
      }
    } else {
      if (target > array[middleIdx] && target <= array[right]) {
        left = middleIdx + 1;
      } else {
        right = middleIdx - 1;
      }
    }
  }
  return -1;
}

// Do not edit the line below.
exports.shiftedBinarySearch = shiftedBinarySearch;

function findClosestValueInBst(tree, target) {
  //receive a BST and a target value
  //we want to find the closest node value to target

  //edge cases: if the tree is empty

  //traverse through the tree while the tree is not null
  //keep track of closestValue to target
  //keep track of closestValue node

  //if the target's value is less than root node, traverse on left side
  //else traverse on right side
  //return the treeNode value

  if (!tree) return 0;

  let treeNodeValue = null;
  let treeNodeDiff = Infinity;
  let treeNode = tree;

  while (treeNode !== null) {
    if (Math.abs(treeNode.value - target) <= treeNodeDiff) {
      treeNodeDiff = Math.abs(treeNode.value - target);
      treeNodeValue = treeNode.value;
    }
    if (treeNodeValue === 0) {
      break;
    }
    if (target < treeNode.value) {
      treeNode = treeNode.left;
    } else {
      treeNode = treeNode.right;
    }
  }
  return treeNodeValue;
}

// This is the class of the input tree. Do not edit.
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Do not edit the line below.
exports.findClosestValueInBst = findClosestValueInBst;

// This is an input class. Do not edit.
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function validateBst(tree, min = -Infinity, max = Infinity) {
  //receive a tree
  //return a boolean: true if BST, else false

  //if the tree is empty, return true

  //!check the min on right side, check the max on left side

  //traverse through the tree
  //check if the left node of the tree is < than parent,
  //if not, return false immediately
  //then check the right side of the tree is > than parent node
  //if not, return false immediately

  if (!tree) return true;

  if (tree.value < min || tree.value >= max) return false;
  return (
    validateBst(tree.left, min, tree.value) &&
    validateBst(tree.right, tree.value, max)
  );
}

// Do not edit the line below.
exports.BST = BST;
exports.validateBst = validateBst;

function inOrderTraverse(tree, array) {
  //starts at the left node
  //check if tree is not empty
  //adds in nodes from the left
  //then adds in nodes from the right

  if (tree !== null) {
    inOrderTraverse(tree.left, array);
    array.push(tree.value);
    inOrderTraverse(tree.right, array);
  }
  return array;
}

function preOrderTraverse(tree, array) {
  //checks if the tree is not empty,
  //adds in root node first
  //then adds in left nodes, then right nodes

  if (tree !== null) {
    array.push(tree.value);
    preOrderTraverse(tree.left, array);
    preOrderTraverse(tree.right, array);
  }
  return array;
}

function postOrderTraverse(tree, array) {
  //checks if the tree is not empty,
  //adds in nodes from left, right, then root node

  if (tree !== null) {
    postOrderTraverse(tree.left, array);
    postOrderTraverse(tree.right, array);
    array.push(tree.value);
  }
  return array;
}

// Do not edit the lines below.
exports.inOrderTraverse = inOrderTraverse;
exports.preOrderTraverse = preOrderTraverse;
exports.postOrderTraverse = postOrderTraverse;

function inOrderTraverse(tree, array) {
  //if tree is not empty,
  //traverse through the left node,
  //add to the array,
  //then traverse through right node
  //return array;

  if (tree !== null) {
    inOrderTraverse(tree.left, array);
    array.push(tree.value);
    inOrderTraverse(tree.right, array);
  }
  return array;
}

function preOrderTraverse(tree, array) {
  //if tree is not empty
  //start at root node
  //add in node values
  //then go to left
  //then go to right

  if (tree !== null) {
    array.push(tree.value);
    preOrderTraverse(tree.left, array);
    preOrderTraverse(tree.right, array);
  }
  return array;
}

function postOrderTraverse(tree, array) {
  // Write your code here.
  //if tree is not empty
  //traverse through left
  //traverse through right
  //add nodes to array
  if (tree !== null) {
    postOrderTraverse(tree.left, array);
    postOrderTraverse(tree.right, array);
    array.push(tree.value);
  }
  return array;
}

// Do not edit the lines below.
exports.inOrderTraverse = inOrderTraverse;
exports.preOrderTraverse = preOrderTraverse;
exports.postOrderTraverse = postOrderTraverse;

function isValidSubsequence(array, sequence) {
  //receive two arrays of integers
  //return true if sequence exists in array in the same order, else false
  //[3, 5, 6, 1, 3], [2, 3] => false
  //[-3,63,7,8,2], [-3, 7, 8] => true

  //edge cases: empty array
  //if sequence length is > array.length, return false

  //start at first index of both arrays
  //if you found the same values, then move pointer in sequence
  //else return false

  //else return true

  if (sequence.length > array.length) return false;
  let idx = 0;

  for (let i = 0; i < array.length; i++) {
    if (sequence[idx] === array[i]) {
      idx++;
    }
  }
  return idx === sequence.length;
}

// Do not edit the line below.
exports.isValidSubsequence = isValidSubsequence;

function sortedSquaredArray(array) {
  // Write your code here.
  //receive an array of integers
  //return an array back with numbers squared
  //[2,3 ,5, 8] => [4, 9, 25, 64]

  //edge case: if they are not in non-ascending order

  //create an array
  //iterate through the nums
  //math.pow the nums
  //return the array created

  let powerNums = [];
  let powNum = Infinity;

  for (let i = 0; i < array.length; i++) {
    powNum = Math.pow(array[i], 2);
    powerNums.push(powNum);
  }
  return powerNums.sort((a, b) => a - b);
}

// Do not edit the line below.
exports.sortedSquaredArray = sortedSquaredArray;

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

const teams = [
  ["Fashion", "Makeup"],
  ["Shoes", "Fashion"],
  ["Makeup", "Fashion"],
];

const results = [0, 0, 1];

for (let i = 0; i < teams.length; i++) {
  const [homeTeam, awayTeam] = teams[i];
  const result = results[i];
  const winningTeam = result === 1 ? homeTeam : awayTeam;
  console.log(winningTeam);
}

function majorityElement(array) {
  //receive an array of integers
  //return the value that is seen the most
  //[3, 5, ,6, 2,2,3,3] => 3

  //keep track of how many times an element has been seen
  //with frequency counter

  let seenVals = {};
  let maxCount = 0;
  let ele = null;

  for (let num of array) {
    seenVals[num] = (seenVals[num] || 0) + 1;
  }

  for (let key in seenVals) {
    if (seenVals[key] > maxCount) {
      maxCount = seenVals[key];
      ele = key;
    }
  }
  return parseInt(ele);
}

// Do not edit the line below.
exports.majorityElement = majorityElement;

function mergeOverlappingIntervals(array) {
  // receive an array of arrays
  //return an array of arrays where similar numbers are merged together
  //[[1,6], [2, 4], [8, 9]] => [[1, 6], [8, 9]]

  //edge case:

  //sort the intervals by start time
  //iterate through the arrays
  //look at the first number of start time, compare it to the end time of the next interval
  //if it is less than or equal to, they can be truncated together
  //return the array back

  array.sort((a, b) => a[0] - b[0]);
  const mergedIntervals = [array[0]];

  for (let i = 1; i < array.length; i++) {
    const current = array[i];
    const last = mergedIntervals[mergedIntervals.length - 1];
    if (current[0] <= last[1]) {
      last[1] = Math.max(last[1], current[1]);
    } else {
      mergedIntervals.push(current);
    }
  }
  return mergedIntervals;
}

// Do not edit the line below.
exports.mergeOverlappingIntervals = mergeOverlappingIntervals;

function nonConstructibleChange(coins) {
  //receive an array of integers
  //return the min amt for change you can't make
  //[3, 6, 7, 2] => 1
  //[1, 3,4] => 2

  //keep track of change,
  //sort the coins
  //iterate through the coins
  //add to change
  //check if the next coin is more than what the current change is,
  //can't make it
  //return change + 1

  let change = 0;
  coins.sort((a, b) => a - b);

  for (let i = 0; i < coins.length; i++) {
    if (coins[i] > change + 1) return change + 1;
    change += coins[i];
  }
  return change + 1;
}

// Do not edit the line below.
exports.nonConstructibleChange = nonConstructibleChange;

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  //receive a matrix
  //return an array back of the values seen in a spiral

  //edge case: if matrix is empty
  if (matrix.length === 0) return [];

  //create an array to store the values
  //iterate at top row, then right col, then bottom row, then left col
  //as i'm iterating, add the value into the array and after searching each row/col
  //decrement or increment b/c it's been visited
  //return the result back

  let result = [];

  let top = 0;
  let bottom = matrix.length - 1;
  let left = 0;
  let right = matrix[0].length - 1;

  while (top <= bottom && left <= right) {
    for (let i = left; i <= right; i++) {
      result.push(matrix[top][i]);
    }
    top++;

    for (let i = top; i <= bottom; i++) {
      result.push(matrix[i][right]);
    }
    right--;

    if (top <= bottom) {
      for (let i = right; i >= left; i--) {
        result.push(matrix[bottom][i]);
      }
      bottom--;
    }
    if (left <= right) {
      for (let i = bottom; i >= top; i--) {
        result.push(matrix[i][left]);
      }
      left++;
    }
  }
  return result;
};

function nonConstructibleChange(coins) {
  //receive an array of coins (pos)
  //return back an integer of the min change you cannot create
  //[3, 4, 1, 8] => 2

  //initialize variables change at 0
  //itereate through the array of integers
  //if the next coin >= change + 1, then return change + 1
  //else if iterate through entire array
  //return all of coins + 1 can't make

  coins.sort((a, b) => a - b);
  let change = 0;

  for (let coin of coins) {
    if (coin > change + 1) return change + 1;
    change += coin;
  }
  return change + 1;
}

// Do not edit the line below.
exports.nonConstructibleChange = nonConstructibleChange;
