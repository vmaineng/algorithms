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
function classPhotos(redShirtHeights, blueShirtHeights) {
  //receive an array of integers for red shirts, and blue shirts
  //return true or false

  //sort the arrays from tallest to shortest

  redShirtHeights.sort((a, b) => b - a);
  blueShirtHeights.sort((a, b) => b - a);

  const firstShirt = redShirtHeights[0] > blueShirtHeights[0] ? "BLUE" : "RED";

  for (let i = 0; i < redShirtHeights.length; i++) {
    const redShirtHeight = redShirtHeights[i];
    const blueShirtHeight = blueShirtHeights[i];

    if (firstShirt === "RED") {
      if (redShirtHeight >= blueShirtHeight) {
        return false;
      }
    } else if (blueShirtHeight >= redShirtHeight) {
      return false;
    }
  }
  return true;
}

// Do not edit the line below.
exports.classPhotos = classPhotos;

function minimumWaitingTime(queries) {
  //receive an an array of integers
  //return the min waiting time
  //[6, 2, 4] => (0) +(6) + (6+ 2) + (8+ 4) = 26
  //[2, 4, 6] => (0) + (2) + (4 + 2) + (6 + 6) = 20

  //sort by smallest
  //iterate through queries
  //add each value to the waiting time
  //return min total waiting time

  queries.sort((a, b) => a - b);

  let waitingTime = 0;

  for (let i = 0; i < queries.length; i++) {
    let currentLoad = queries[i];
    let previousLoad = queries.length - (i + 1);
    console.log(previousLoad);
    waitingTime += currentLoad * previousLoad;
  }
  return waitingTime;
}

// Do not edit the line below.
exports.minimumWaitingTime = minimumWaitingTime;

console.log(minimumWaitingTime([5, 1, 4]));

function minimumWaitingTime(queries) {
  //reeceiv an array of integers
  //return the min waiting time
  //[5,1 ,4] => 0 + 5 + (5 + 1) + (1+ 4) = 16
  // [ 1, 4, 5] => 0 + 1 + (1 + 4) + (4 + 5) =15

  //sort
  //initialize a minWaitingTime to 0
  //iterate through each queries
  //take each queries * duration
  //duration = the queries remaining + 1 (since array is 0 - indexed);
  //return minWaiting Time

  queries.sort((a, b) => a - b);
  let minWaitingTime = 0;

  for (let i = 0; i < queries.length; i++) {
    let query = queries[i];
    let duration = queries.length - (i + 1);
    minWaitingTime += query * duration;
  }
  return minWaitingTime;
}

// Do not edit the line below.
exports.minimumWaitingTime = minimumWaitingTime;

function classPhotos(redShirtHeights, blueShirtHeights) {
  //receive equal amount of length for redShirt and blueShirt
  //return true if place all same color in the back row, else false
  //[8, 32, 4], [8, 2, 9] =>
  //after sorting: [32, 8, 4], [9, 8, 2] => false b/c [8, 8]

  //edge case: not equal lengths

  //sort red and blue by tallest
  //first indicate who in in the front row

  //iterate through the redshirt array
  //check who is in front row
  //verify the back row is not taller than the front row
  //else return false
  //after checking, return true;

  redShirtHeights.sort((a, b) => b - a);
  blueShirtHeights.sort((a, b) => b - a);

  let firstRowShirt = redShirtHeights[0] > blueShirtHeights[0] ? "BLUE" : "RED";

  for (let i = 0; i < redShirtHeights.length; i++) {
    blueShirt = blueShirtHeights[i];
    redShirt = redShirtHeights[i];

    if (firstRowShirt === "BLUE") {
      if (redShirt <= blueShirt) return false;
    } else {
      if (redShirt >= blueShirt) return false;
    }
  }
  return true;
}

// Do not edit the line below.
exports.classPhotos = classPhotos;

function transposeMatrix(matrix) {
  //receive a matrix
  //return the matrix transposed - columns into rows
  //[
  // [3, 4],
  //   [5, 6]
  // ]

  //[
  // [3, 5],
  //   [4, 6],
  // ]

  //iterate through cols first
  //create a new array
  //iterate through row
  //push in the row and columns
  //add it to the new matrix

  let transposedMatrix = [];

  for (let cols = 0; cols < matrix[0].length; cols++) {
    let newRow = [];
    for (let rows = 0; rows < matrix.length; rows++) {
      newRow.push(matrix[rows][cols]);
    }
    transposedMatrix.push(newRow);
  }
  return transposedMatrix;
}

// Do not edit the line below.
exports.transposeMatrix = transposeMatrix;

function commonCharacters(strings) {
  // Write your code here.
  //input: array of strings
  //output: array of common chars
  //constraints:
  //edge cases:  if string is empty
  //brute force: have a pointer on one and check on every string

  //optimized: use a Set
  //iterate through each char
  //return what's left in the set

  // let standardSet = new Set(strings[0])

  // do a frequency counter
  //count all the letters in each string
  //if the letters have the same amount as the strings length in array
  //that means they are found in all strings

  let freq = {};

  for (const string of strings) {
    const uniqueStringChars = new Set(string); //makes a set of unique chars
    for (const char of uniqueStringChars) {
      if (!freq[char]) {
        freq[char] = 0;
      }
      freq[char]++;
    }
  }
  const finalChars = [];

  for (const [char, count] of Object.entries(freq)) {
    if (count === strings.length) {
      finalChars.push(char);
    }
  }
  return finalChars;
}

// Do not edit the line below.
exports.commonCharacters = commonCharacters;

function commonCharacters(strings) {
  //receive an array of strings
  //return an array of common characters
  //['jump', 'ube', 'run'] => ['u']

  //initialize a Set
  //capture the first array in the set
  //then iterate at the second word in the set, check if any of the letters exist in it
  //if it doesn't, then delete it

  //return the chars left in set as an array

  let firstSet = new Set(strings[0]);

  for (let i = 1; i < strings.length; i++) {
    let theRestSet = new Set(strings[i]);
    for (let char of firstSet) {
      if (!theRestSet.has(char)) {
        firstSet.delete(char);
      }
    }
  }
  return Array.from(firstSet);
}

// Do not edit the line below.
exports.commonCharacters = commonCharacters;

function findThreeLargestNumbers(array) {
  //receive an array of integers (pos and neg)
  //return an array of sorted integers of 3 highest integers
  //[3,2,-34, 12, 56, 1] => [3,12, 56]

  //create an array and initalize 3 spots to null
  //iterate through the array
  //if the value is > than the last array
  //then move all the values down
  //assign the values to the last spot in the array since it's the highest
  //same for the other 2 values
  //return the array

  if (array.length === 0) return [];

  let biggestNumsArray = [-Infinity, -Infinity, -Infinity];

  for (let num of array) {
    if (num > biggestNumsArray[2]) {
      biggestNumsArray[0] = biggestNumsArray[1];
      biggestNumsArray[1] = biggestNumsArray[2];
      biggestNumsArray[2] = num;
    } else if (num > biggestNumsArray[1]) {
      biggestNumsArray[0] = biggestNumsArray[1];
      biggestNumsArray[1] = num;
    } else if (num > biggestNumsArray[0]) {
      biggestNumsArray[0] = num;
    }
  }
  return biggestNumsArray;
}

// Do not edit the line below.
exports.findThreeLargestNumbers = findThreeLargestNumbers;

function caesarCipherEncryptor(string, key) {
  //receive a string of chars and key of integer to add more placements
  //return a new string + key spaces
  //'abc', 3 => 'def'

  //edge case: if string is empty
  //iterate through string
  //add key spaces
  //if it surpasses the length of 26, % to loop around
  //return new string

  if (!string) return "";
  key = key % 26;
  let newString = "";

  for (let char of string) {
    let newCharCode = char.charCodeAt(0) + key;
    if (newCharCode > 122) {
      newCharCode = 96 + (newCharCode - 122);
    }
    newString += String.fromCharCode(newCharCode);
  }
  return newString;
}

// Do not edit the line below.
exports.caesarCipherEncryptor = caesarCipherEncryptor;

function isValidSubsequence(array, sequence) {
  // Write your code here.
  //input - two arrays, ,
  //output - true or false
  //edge - if array length is less than sequence length;
  //strategy - create a pointer starting at the first value
  //create a pointer for array and pointer for sequence
  //check if they are equal to each other
  //return true, otherwise, return false

  let idx = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] === sequence[idx]) {
      idx++;
    }
  }
  return idx === sequence.length;
}

// Do not edit the line below.
exports.isValidSubsequence = isValidSubsequence;
function isValidSubsequence(array, sequence) {
  //receive two arrays of integers (pos and negative)
  //return true if sequqnce is part of array, else false
  //[32, 4, 52, 5], [52, 5] => true;

  //edge case: if sequence's length > array's length, return false

  //create two pointers for both arrays
  //iterate through both arrays until reach the end of one of them
  //if sequence value has been found in array, move pointer in sequence pointer
  //else move arrays pointer
  //then return if sequence pointer reached end of sequence's end of array

  if (sequence.length > array.length) return false;

  let idx = 0;
  let sIdx = 0;

  while (idx < array.length && sIdx < sequence.length) {
    if (array[idx] === sequence[sIdx]) sIdx++;
    idx++;
  }
  return sIdx === sequence.length;
}

// Do not edit the line below.
exports.isValidSubsequence = isValidSubsequence;

function smallestDifference(arrayOne, arrayTwo) {
  //receive two array of integers
  //return an array with a pair (the values) (one from both arrays) with smalleset difference
  //[3, 4, 5, -1], [1, 3, 2, 5] => [-1, 1]

  //edge case: if one array is empty, can't get a pair

  //sort both arrays from smallest to biggest
  //create an array to store pairs
  //keep track of min total
  //iterate through both arrays

  //if found min pair, return the array

  let pairArray = [];
  let minTotal = Number.MAX_SAFE_INTEGER;

  arrayOne.sort((a, b) => a - b);
  arrayTwo.sort((a, b) => a - b);

  let idx = 0;
  let idxTwo = 0;

  while (idx < arrayOne.length && idxTwo < arrayTwo.length) {
    let tempSum = Math.abs(arrayOne[idx] - arrayTwo[idxTwo]);
    if (tempSum < minTotal) {
      minTotal = tempSum;
      pairArray.push[(arrayOne[idx], arrayTwo[idxTwo])]; //replaces
    }
    arrayOne[idx] > arrayTwo[idxTwo] ? idxTwo++ : idx++;
  }
  return pairArray;
}

// Do not edit the line below.
exports.smallestDifference = smallestDifference;

function isPalindrome(string) {
  //receive a string w/ no spaces
  //return boolean if written same forward and backwards
  //'apple' =false
  //'hijih' => true

  //if string has one length = return true;

  //use methods
  //split it and reverse and it and see if it equals the string

  //return string.split("").reverse().join("") === string

  //two pointers
  //create one at beginning and one at end
  //check if they are not the same
  //return false
  //else decrement pointers
  //return true

  let left = 0;
  let right = string.length - 1;

  while (left < right) {
    if (string[left] !== string[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
}

// Do not edit the line below.
exports.isPalindrome = isPalindrome;
