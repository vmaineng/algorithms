function twoNumberSum(array, targetSum) {
  //receive an array of integers
  //return the two values in an array that totals up to targetSum
  //ex: [1, 3, -2, 4], -1 => [1, -2]

  //iterate through the array with one pointer
  //iterate through the rest of the array with a second pointer
  //if the total matches up to targetSum
  //return the two values in an array

  // for (let i =0; i < array.length; i++) {
  //   for (let j = i + 1; j < array.length; j++) {
  //     if (array[i] + array[j] === targetSum) {
  //       return [array[i], array[j]]
  //     }
  //   }
  // }
  // return []

  //time: O(n^2);
  //space: O(1)

  //optimized: use an object to store the values
  //iterate through the array of integers
  //look at the difference between target and the current integer value
  //if the obj, has the difference
  //return the difference and the current value of pointer
  //else set the value in the object

  let valueObj = {};

  for (let i = 0; i < array.length; i++) {
    let difference = targetSum - array[i];
    if (valueObj.hasOwnProperty(difference)) {
      return [array[i], valueObj[difference]];
    } else {
      valueObj[array[i]] = array[i];
    }
  }
  return [];
}

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;

/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  //receive an unsorted array of integers
  //return the length of the longest consecutive elements sequence
  //[3, 2, 5, 6, 7] => [5,6, 7] => 3

  //initialize a count
  //sort the integers in the array
  //check if the element in front is increasing by
  //if it's a duplicate, continue
  //if so, increment the count
  //else if it isn't increasing
  //capture the maxLength seen thus far
  //return the maxLength

  //edge case: if the nums array is less than one, it will always be the length of the array

  // if (nums.length < 2) return nums.length

  // let maxLength = 0;
  // let currentLength = 1;

  // nums.sort((a,b) => a -b);

  // for (let i = 1; i < nums.length; i++) {
  //     if (nums[i] === nums[i - 1]) continue;

  //     if(nums[i] === nums[i-1] + 1) {
  //         currentLength++
  //     } else {
  //         maxLength = Math.max(maxLength, currentLength)
  //         currentLength = 1
  //     }
  // }
  // maxLength = Math.max(maxLength, currentLength)
  // return maxLength
  //time: o(n log n);
  //space: O(1)

  //optimized using a set

  if (nums.length === 0) return 0;

  let consecVals = new Set(nums);
  let maxLength = 0;

  for (let num of consecVals) {
    if (!consecVals.has(num - 1)) {
      let currentNum = num;
      let currentLength = 1;

      while (consecVals.has(currentNum + 1)) {
        currentLength++;
        currentNum++;
      }
      maxLength = Math.max(maxLength, currentLength);
    }
  }
  return maxLength;
};

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function (nums, k) {
  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    let sum = 0;
    for (let j = i; j < nums.length; j++) {
      sum += nums[j];
      if (sum === k) {
        count++;
      }
    }
  }
  return count;
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
 * @return {number[][]}
 */
var levelOrder = function (root) {
  if (root === null) return [];

  let result = [];
  let queue = [root];

  while (queue.length > 0) {
    let levelSize = queue.length;
    let currentLevel = [];

    for (let i = 0; i < levelSize; i++) {
      let currentNode = queue.shift();
      currentLevel.push(currentNode.val);

      if (currentNode.left !== null) {
        queue.push(currentNode.left);
      }

      if (currentNode.right !== null) {
        queue.push(currentNode.right);
      }
    }
    result.push(currentLevel);
  }
  return result;
};

var topKFrequent = function (nums, k) {
  //if nums is empty, return empty array
  //create an object to track values seen
  //then get all the values in an array
  //sort by biggest to smallest
  //take the first k elements

  if (nums.length === 0) return [];

  // let objSeen = {};
  // for (let num of nums) {
  //    objSeen[num] = (objSeen[num] || 0) + 1
  // }
  // const objSeenArray = Object.entries(objSeen)

  // objSeenArray.sort((a,b) => b[1] - a[1]);

  // return objSeenArray.slice(0,k).map((item) => parseInt(item[0]))
  //time: O(n log n)

  //optimized:
  //count the frequencies
  //create buckets where index represents frequency
  //collect top 'k' most frequent elements from the buckets

  let frequencyObj = {};
  for (let num of nums) {
    frequencyObj[num] = (frequencyObj[num] || 0) + 1;
  }

  let buckets = Array(nums.length + 1)
    .fill()
    .map(() => []);

  for (let num in frequencyObj) {
    let frequency = frequencyObj[num];
    buckets[frequency].push(parseInt(num));
  }

  let result = [];
  for (let i = buckets.length - 1; i >= 0 && result.length < k; i--) {
    if (buckets[i].length > 0) {
      result.push(...buckets[i]);
    }
  }
  return result.slice(0, k);
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
 * @return {number[][]}
 */
var levelOrder = function (root) {
  //receive the root node of a binary tree
  //return level order traversal of nodes values from left to right

  //initialize a queue to hold the root's node
  //initialize an empty array to hold each levels
  //iterate through the queue while it's not empty
  //create another array to hold all the levels nodes
  //capture the current length in the queue
  //take the first node in the queue, add it to the answer array
  //then add in left and right children to queue next
  //add the levels array to answer array
  //return answer

  if (!root) return [];

  let queue = [root];
  let answer = [];

  while (queue.length > 0) {
    let currentLevels = [];
    let levelSize = queue.length;

    for (let i = 0; i < levelSize; i++) {
      const currentNode = queue.shift();
      currentLevels.push(currentNode.val);

      if (currentNode.left) queue.push(currentNode.left);
      if (currentNode.right) queue.push(currentNode.right);
    }
    answer.push(currentLevels);
  }
  return answer;
};

//to do bfs from right to left; add in right child first, then left child::

var levelOrderRightToLeft = function (root) {
  if (!root) return []; // Return an empty array if the root is null

  const result = []; // Store the final level order traversal
  const queue = [root]; // Queue initialized with the root node

  while (queue.length > 0) {
    const currentLevel = [];
    const levelSize = queue.length; // Nodes at the current level

    for (let i = 0; i < levelSize; i++) {
      const currentNode = queue.shift();
      currentLevel.push(currentNode.val);

      // Add right child first, then left child
      if (currentNode.right) queue.push(currentNode.right);
      if (currentNode.left) queue.push(currentNode.left);
    }

    result.push(currentLevel); // Add current level to the result
  }

  return result;
};

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  //receive an array of integers (pos and negative), k = integer
  //return an array where it's been shifted by right k times

  //[3, 2, 4], 2 => [2, 4, 3]

  //if array is empty, return an empty array
  //create a new array
  //iterate the array, starting at the end of the array
  //add k amount to it and add into the new array
  //keep going until array is empty

  if (nums.length === 0) return [];

  // k = k % nums.length

  // for (let i = 0; i < k; i++) {
  //     nums.unshift(nums.pop())

  k = k % nums.length;

  function reverse(start, end) {
    while (start < end) {
      [nums[start], nums[end]] = [nums[end], nums[start]];
      start++;
      end--;
    }
  }

  reverse(0, nums.length - 1);
  reverse(0, k - 1);
  reverse(k, nums.length - 1);

  //time: O(n x k) => n is the length of nums and k is the number of rotations
};

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function (nums, k) {
  //receive an array of integers of nums and an integer k
  //return total number of subarrays = k
  //[1,4,3],5 => 1 b/c of [1,4]
  //initialize a total sum
  //iterate nums
  //count up to k amount target
  //if total = target, incremet count
  // let count = 0;
  // for (let i = 0; i < nums.length;i++) {
  //     let sum = 0;
  //     for (let j = i; j < nums.length; j++) {
  //         sum += nums[j]
  //         if (sum === k) {
  //             count++
  //         }
  //     }
  // }
  // return count
  // let count = 0;
  // let sum = 0;
  // const map = new Map();
  // map.set(0,1);
  // for (let num of nums) {
  //     sum += num;
  //     if (map.has(sum - k)) {
  //         count += map.get(sum-k);
  //     }
  //     map.set(sum, (map.get(sum) || 0) + 1)
  // }
  // return count;
};

if (!root) return [];

let queue = [root];
let answer = [];

while (queue.length > 0) {
  let currentLevels = [];
  let levelSize = queue.length;

  for (let i = 0; i < levelSize; i++) {
    const currentNode = queue.shift();
    currentLevels.push(currentNode.val);

    if (currentNode.left) queue.push(currentNode.left);
    if (currentNode.right) queue.push(currentNode.right);
  }
  answer.push(currentLevels);
}
return answer;

function descendingOrder(n) {
  //recevie an integer
  //return an integer from biggest to smallest
  //3423589 => 9854332

  //turn the integer into a string, into an array
  //sort
  //return the string number into an number format back

  let stringNum = n.toString();

  console.log(stringNum);
  stringNum = stringNum
    .split("")
    .sort((a, b) => b - a)
    .join("");
  return Number(stringNum);
}

function solution(number) {
  //receive a number
  //return the sum of all multiples of 3 or 5 below the number

  //15 => 3, 5,6, 9, 10,12 => 45

  //initialize a sum total
  //iterate up to number
  //check if the number can be by number with no remaineder
  //add to the sum

  let sum = 0;
  for (let i = 1; i < number; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      sum += i;
    } else if (i % 3 === 0) {
      sum += i;
    } else if (i % 5 === 0) {
      sum += i;
    }
  }
  return sum;
}

/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function (rooms) {
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
        visitedCount++;
        queue.push(key);

        if (visitedCount === rooms.length) {
          return true;
        }
      }
    }
  }
  return visitedCount === rooms.length;
};

function level(instructions: string, obstacles: number[]): boolean {}

// R goes 1 step to the right, L goes 1 step to the left, j goes 2 steps in the prev movement direction
"RRRJRJRRR"[(4, 6)];
/*
->  ->  ->  *     *   ->   ->  ->  ->
1   2   3   4  5  6   7    8   9   10
*/
level("RRRJRJRRR", [4, 6]); // -> true

function level(instructions: string, obstacles: number[]): boolean {
  let position = 0;
  let prevMovement = null;

  for (const movement of instructions) {
    if (position >= 9) {
      return true;
    }

    if (obstacles.includes(position)) {
      return false;
    }

    if (movement === "R") {
      position++;
      prevMovement = "R";
    } else if (movement === "L") {
      position--;
      prevMovement = "L";
    } else if (movement === "J") {
      if (prevMovement === "R") {
        position += 2;
      } else {
        position -= 2;
      }
    }
  }

  return false;
}

function shortPath(matrix) {
  //receive a matrix
  //return min  directions to destination
  //use bfs -
  //pop on current position
  //iterate through matrix while queue.length > 0
  //add to steps
}

function spEng(sentence) {
  //receive a string of letters
  //return true if it contains "English", else false

  //ex: 'ehlkwhleoEnglishjslkdjfwlk' => true

  //initialize the world english
  //lowercase the setence received
  //check if the word contains 'English', return true, else return false

  const word = "english";

  if (sentence.toLowerCase().includes(word)) {
    return true;
  } else {
    return false;
  }
}

function typeOfSum(a, b) {
  //receive two types of data: a and b;
  //return the type of the sum of two arguments

  //add them together
  //return the typeof sum

  let sum = a + b;
  return typeof sum;
}

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  //receive an array of integers
  //return index of target if it is in nums
  //[1,2,3,4,5], 4
  //rotated => [3,4,5,1,2], 4 => 1

  //set up binary search method
  //calc middle idx
  //check the determine sorted half - if the left half is sorted to middle is sorted
  //check if the target is in range
  //else check the right value

  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let middle = Math.floor((left + right) / 2);
    if (target === nums[middle]) {
      return middle;
    }
    if (nums[left] <= nums[middle]) {
      //if it is sorted
      if (nums[left] <= target && target <= nums[middle]) {
        right = middle - 1;
      } else {
        left = middle + 1;
      }
    } else {
      if (nums[middle] < target && target <= nums[right]) {
        left = middle + 1;
      } else {
        right = middle - 1;
      }
    }
  }
  return -1;
};

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function (nums, k) {
  //receive an array of integers of nums and an integer of k
  //return total number of subarays total k
  //[3, 2, 1, 1,], 2 => [2]

  //brute force:
  //keep ointer on first value
  //keep ointer on second value
  //increment sum
  //if sum === k
  //count++
  //return count

  // let count = 0;

  // for (let i = 0; i < nums.length ;i++) {
  //     let sum = 0;
  //     for (let j = i; j < nums.length; j++) { // ! why start at i
  //         sum += nums[j]
  //         if (sum ===k){
  //             count++
  //         }
  //     }
  // }
  // return count;

  let count = 0;
  let sum = 0;

  const map = new Map();
  map.set(0, 1);

  for (let num of nums) {
    sum += num;
    if (map.has(sum - k)) {
      count += map.get(sum - k);
    }
  }
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  //receive an array of integers
  //return the majority element
  //ex: [1,2,2,2,3,5,5] => 2?

  //create a frequency counter
  //check if the num / length >
  //then update max

  // const countMap = {};
  // const majority = Math.floor(nums.length /2)

  // for (const num of nums) {
  //     countMap[num] = (countMap[num] || 0) + 1
  //     if (countMap[num] > majority) {
  //         return num
  //     }
  // }

  let count = 0;
  let candidate = null;

  for (const num of nums) {
    if (count === 0) {
      candidate = num;
    }
    count += num === candidate ? 1 : -1;
  }
  return candidate;

  // Initialize two variables: count to 0 and candidate to null.
  // Loop through the array:
  // If count is 0, set the current number as the candidate.
  // If the current number is equal to the candidate, increment count.
  // If the current number is different, decrement count.
  // By the end of the loop, the candidate will be the majority element.
};

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
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

  let maxAmount = 0;
  for (let i = 0; i < height.length; i++) {
    for (let j = i + 1; j < height.length; j++) {
      let minHeight = Math.min(height[i], height[j]);
      let maxArea = minHeight * (j - i);
      maxAmount = Math.max(maxAmount, maxArea);
    }
  }
  return maxAmount;

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
    let currentArea = minHeight * (right - left);
    maxAmount = Math.max(currentArea, maxAmount);
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }
  return maxAmount;

  //time: O(n);
  //space:O(1)
};

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  //receive a height array
  //return the max amount of water a container can store

  //[3, 4, 5, 1, 2]
  //4

  //brute force:
  //initialize a maxArea
  //iterate through the height array
  //then iterate through the second value of the height array
  //calculate the min Height
  //then calculate the width
  //update the area
  //return maxArea

  // let maxArea = 0;

  // for (let i = 0; i < height.length ;i++) {
  //     for (let j = i + 1; j < height.length; j++) {
  //     let area = Math.min(height[i], height[j]) * (j - i)
  //     maxArea = Math.max(area, maxArea)
  // }
  // }
  // return maxArea

  //time: O(n^2); space: O(1)

  //two pointers => O(n)

  //let left start at first value
  //let right pointer start from the end
  //while they are not equal to each other
  //calculate the area between them taking the minHeight
  //return max Area
  //move left pointer and right pointer depending on which one is the smallest one

  let left = 0;
  let right = height.length - 1;
  let maxArea = 0;

  while (left < right) {
    let area = Math.min(height[left], height[right]) * (right - left);
    maxArea = Math.max(area, maxArea);

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxArea;
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
 * @return {number[][]}
 */
var levelOrderBottom = function (root) {
  //receive a root node of a binary tree
  //return the level order traversal

  //edge case: if there is not root node, return an empty array

  //initialize a queue with the root added in it
  //while queue is not empty
  //initialize a current level array
  //capture the static size length of the queue
  //iterate until the end of the queue
  //pop off currentNode
  //add node into the array
  //add left and right child to queue if needed
  //then return array reverse

  if (!root) return [];

  let queue = [root];
  let array = [];

  while (queue.length > 0) {
    let currentLevel = [];
    let levelsize = queue.length;

    for (let i = 0; i < levelsize; i++) {
      const currentNode = queue.shift();
      currentLevel.push(currentNode.val);

      if (currentNode.left) queue.push(currentNode.left);
      if (currentNode.right) queue.push(currentNode.right);
    }
    array.push(currentLevel);
  }
  return array.reverse();
};

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  //receive an array of integers/ pos and negative
  //return the array of integers rotated by k amount

  //edge case: if array is empty, return empty array
  //if array only has one value, and K > nums

  //initialize a new array
  //start at the beginning of the array
  //pop off at the end
  //add to the beggininng
  //return array

  //    for (let i = 0; i < k; i++) {
  //     nums.unshift(nums.pop())
  //    }
  //    return nums;

  //reverse entire array
  //reverse from start to k,
  //reverse from k to end of the length array

  k = k % nums.length;

  function reverse(start, end) {
    while (start < end) {
      [nums[start], nums[end]] = [nums[end], nums[start]];
      start++;
      end--;
    }
  }
  reverse(0, nums.length - 1);
  reverse(0, k - 1);
  reverse(k, nums.length - 1);
};

/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function (chars) {
  //receive an array of characters,
  //return an array of strings back with it compressed
  //['a','a','b','b','b'] => ['2','a','3','b']

  //if array is empty, return an array of an empty string

  //keep track of an empty string
  //keep count of strings seen
  //iterate through chars
  //check if the next value is still same letter
  //increment count
  //else capture the current value
  //return array of values seen

  let answer = [];
  let i = 0;

  while (i < chars.length) {
    let char = chars[i];
    let count = 0;

    while (i < chars.length && chars[i] === char) {
      i++;
      count++;
    }
    answer.push(char);

    if (count > 1) {
      for (let digit of count.toString()) {
        answer.push(digit);
      }
    }
  }

  for (let j = 0; j < answer.length; j++) {
    chars[j] = answer[j];
  }
  return answer.length;
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  //receive an array of nums (possibly sorted), target (integer)
  //return the index of target in nums

  //[3,4,5,0,1,2] => 2 => 5

  //create a left pointer
  //create right pointer
  //find the middle index
  //check if the value at middle idx = target, return idx
  //check if the array is still sorted from left to middle
  //check if the target's value is in the left section
  //if so, move right pointer down, else move left pointer to the other half
  //else check if the target exists on the right side
  //left pointer moves up, else right pointer moves down

  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let middle = Math.floor((left + right) / 2);
    if (nums[middle] === target) {
      return middle;
    }

    if (nums[left] <= nums[middle]) {
      if (nums[left] <= target && target <= nums[middle]) {
        right = middle - 1;
      } else {
        left = middle + 1;
      }
    } else {
      if (nums[middle] < target && target <= nums[right]) {
        left = middle + 1;
      } else {
        right = middle - 1;
      }
    }
  }
  return -1;
};

function canFinish(numCourses, prerequisites) {
  // Create adjacency list
  const graph = new Map();

  // Initialize graph
  for (let i = 0; i < numCourses; i++) {
    graph.set(i, []);
  }

  // Build graph
  for (const [course, prereq] of prerequisites) {
    graph.get(course).push(prereq);
  }

  // Keep track of visited courses in current path
  const visiting = new Set();
  // Keep track of courses we've fully explored
  const visited = new Set();

  // DFS function to detect cycles
  function hasCycle(course) {
    // If we see a course we're currently exploring, we found a cycle
    if (visiting.has(course)) return true;
    // If we've already fully explored this course, no need to check again
    if (visited.has(course)) return false;

    // Mark course as being explored
    visiting.add(course);

    // Check all prerequisites
    for (const prereq of graph.get(course)) {
      if (hasCycle(prereq)) return true;
    }

    // Remove from current path
    visiting.delete(course);
    // Mark as fully explored
    visited.add(course);

    return false;
  }

  // Check each course
  for (let course = 0; course < numCourses; course++) {
    if (hasCycle(course)) return false;
  }

  return true;
}

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  //receive an array of integers
  //return an array of all products except the nums itself
  //[2, 3, 4] => [12, 8, 6]

  //initialize an array
  //iterate through nums creating a first pointer
  //create a multiplier set to 1
  //iterate through nums with a second poitner
  //check if the indexes are not equal to each other
  //multiiplier will be updated by the product of the value at second poitner
  //then update the position in the array
  //return array

  // let answers = [];
  // for (let i = 0; i < nums.length; i++) {
  //     let multiplier = 1;
  //     for (let j = 0; j < nums.length; j++) {
  //         if (i !== j) {
  //             multiplier *= nums[j]
  //         }
  //     }
  //     answers[i] = multiplier
  // }
  // return answers

  //time: O(n^2)
  //space: O(n)

  //optimized: iterate and update products of all the elements to the left
  //then update all the products starting from the right
  //return the array

  let answers = new Array(nums.length).fill(1);

  let leftMultiplier = 1;
  for (let i = 0; i < nums.length; i++) {
    answers[i] = leftMultiplier;
    console.log(answers[i]);
    leftMultiplier *= nums[i];
  }

  let rightMultiplier = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    answers[i] *= rightMultiplier;
    rightMultiplier *= nums[i];
  }

  return answers;
};

//time: O(2n) => O(n);
//space: O(n)

function arrayOfProducts(array) {
  //receive an array of integers
  //return an array back of products of the values in the array
  //[2,3 -1] => [-3, -2, 6]

  //intialize an empty array
  //iterate through the values int he array starting at the first index
  //creater another pointer that will point at the beginning of the array
  //create a multiplier of 1
  //while the indexs do not equal other
  //multiplier * the value at j
  //j * array[i]
  //push the product into the array
  //return array

  let answer = [];

  for (let i = 0; i < array.length; i++) {
    let multiplier = 1;
    for (let j = 0; j < array.length; j++) {
      if (i !== j) {
        multiplier *= array[j];
      }
    }
    answer[i] = multiplier;
  }
  return answer;
}

// Do not edit the line below.
exports.arrayOfProducts = arrayOfProducts;

// Do not edit the class below except for the
// populateSuffixTrieFrom and contains methods.
// Feel free to add new properties and methods
// to the class.
class SuffixTrie {
  constructor(string) {
    this.root = {};
    this.endSymbol = "*";
    this.populateSuffixTrieFrom(string);
  }

  populateSuffixTrieFrom(string) {
    for (let i = 0; i < string.length; i++) {
      this.insertSubString(i, string);
    }
  }

  insertSubString(i, string) {
    let node = this.root;
    for (let j = i; j < string.length; j++) {
      const letter = string[j];
      if (!(letter in node)) node[letter] = {};
      node = node[letter]; //update the green arrow in the tree; keep traversing
    }
    node[this.endSymbol] = true;
  }

  contains(string) {
    let node = this.root;
    for (const letter of string) {
      if (!(letter in node)) return false;
      node = node[letter]; //keep traversing down the suffix tree
    }
    return this.endSymbol in node;
  }
}

// Do not edit the line below.
exports.SuffixTrie = SuffixTrie;

function arrayOfProducts(array) {
  //initalize an array of the array's length set it to 1
  //create a multiplier of 1
  //iterate through the array with all the values of the left side
  //iterate through the answer array with all the values from the right side
  //multiple the values from the array with the values from right side

  let answer = new Array(array.length).fill(1);

  let leftMultiplier = 1;
  for (let i = 0; i < array.length; i++) {
    answer[i] = leftMultiplier;
    leftMultiplier *= array[i];
    console.log(answer);
  }

  let rightMultipler = 1;
  for (let i = array.length - 1; i >= 0; i--) {
    answer[i] *= rightMultipler;
    rightMultipler *= array[i];
  }

  return answer;
}

// Do not edit the line below.
exports.arrayOfProducts = arrayOfProducts;

console.log(arrayOfProducts([3, 4, 5]));
//answer of i gets updated from leftmultiplier
//left multiplier moves over to the next value and gets updated

function classPhotos(redShirtHeights, blueShirtHeights) {
  //receive two arrays of integers
  //return boolean; true if all shirts in the back row, else false
  //blue: [5, 8, 1, 4]
  //red: [3,8,1,7] => false b/c [8 ] & [8]

  //determine which color will be in back row
  //sort red & blue by tallest (biggest)
  //then iterate through one of the color shirts array
  //if the back row is red
  //then check if the blue is not taller than red, else false
  //vice versa
  //otherwise return true

  redShirtHeights.sort((a, b) => b - a);
  blueShirtHeights.sort((a, b) => b - a);

  let frontRow = redShirtHeights[0] > blueShirtHeights[0] ? "BLUE" : "RED";

  for (let i = 0; i < blueShirtHeights.length; i++) {
    if (frontRow === "BLUE") {
      if (redShirtHeights[i] <= blueShirtHeights[i]) return false;
    } else if (blueShirtHeights[i] <= redShirtHeights[i]) return false;
  }

  return true;
}

// Do not edit the line below.
exports.classPhotos = classPhotos;

// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function reverseLinkedList(head) {
  //receive the head of a LL
  //return the LL reversed in place
  // 1 -> 2 -> 3 -> null => 3 -> 2 -> 1 -> null;

  //edge case: if the head is empty, return null;
  //capture the current as the head
  if (!head) return null;

  let prev = null;
  let current = head;

  while (current !== null) {
    const next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev;
}

// Do not edit the lines below.
exports.LinkedList = LinkedList;
exports.reverseLinkedList = reverseLinkedList;

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

  return (
    validateBst(tree.left, min, tree.value) &&
    validateBst(tree.right, tree.value, max)
  );
}

// Do not edit the line below.
exports.BST = BST;
exports.validateBst = validateBst;

var RandomizedSet = function () {
  this.map = new Map();
};

/**
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function (val) {
  if (!val) {
    return false;
  } else {
    this.map.add(val);
    return true;
  }
};

/**
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function (val) {
  if (!val) {
    return false;
  } else {
    this.map.delete(val);
    return true;
  }
};

/**
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function () {
  return Math.random();
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */

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
    if (node == null) return;
    inOrderTraverse(node.left, sortedValues);
    sortedValues.push(node.value);
    inOrderTraverse(node.right, sortedValues);
  }
}

// Do not edit the lines below.
exports.BST = BST;
exports.findKthLargestValueInBst = findKthLargestValueInBst;

function cycleInGraph(edges) {
  //receive an array of integers
  //return true if cycle detected, else return false

  const visited = new Set(); //nodes that have been fully explored
  const inStack = new Set(); //nodes that are currently in the recurstion stack

  function dfs(node) {
    if (inStack.has(node)) return true;
    if (visited.has(node)) return false;

    visited.add(node);
    inStack.add(node);

    for (const neighbor of edges[node]) {
      if (dfs(neighbor)) return true;
    }
    inStack.delete(node);
    return false;
    //if node is found in the instack stack, then it's a cycle
  }

  for (let node = 0; node < edges.length; node++) {
    if (!visited.has(node) && dfs(node)) return true;
  }
  return false;
}

// Do not edit the line below.
exports.cycleInGraph = cycleInGraph;

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
  //start fast and slow pointer at head
  let fast = head;
  let slow = head;
  let tmp;
  let prev;

  //keep iterating and move fast 2x and slow by 1
  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
  }

  //while slow is traversing
  //move pointer to the previous pointer
  while (slow) {
    tmp = slow.next;
    slow.next = prev;
    prev = slow;
    slow = tmp;
  }

  //fast will start at head
  //slow will start at node
  fast = head;
  slow = prev;

  while (slow) {
    //if values don't equal eacho ther return false, otherwise check next nodes?
    if (fast.val !== slow.val) return false;
    fast = fast.next;
    slow = slow.next;
  }
  return true;
};

function removeIslands(matrix) {
  const rows = matrix.length;
  const cols = matrix[0].length;

  // Step 1: Use DFS to mark safe land cells
  function dfs(row, col) {
    // Boundary check
    if (
      row < 0 ||
      row >= rows ||
      col < 0 ||
      col >= cols ||
      matrix[row][col] !== 1
    ) {
      return;
    }
    matrix[row][col] = -1; // Mark as safe (land connected to border)

    // Explore all four directions (up, down, left, right)
    dfs(row + 1, col);
    dfs(row - 1, col);
    dfs(row, col + 1);
    dfs(row, col - 1);
  }

  // Apply DFS from all border land cells
  for (let i = 0; i < rows; i++) {
    if (matrix[i][0] === 1) dfs(i, 0); // Left column
    if (matrix[i][cols - 1] === 1) dfs(i, cols - 1); // Right column
  }
  for (let j = 0; j < cols; j++) {
    if (matrix[0][j] === 1) dfs(0, j); // Top row
    if (matrix[rows - 1][j] === 1) dfs(rows - 1, j); // Bottom row
  }

  // Step 2: Remove isolated islands (turn remaining 1s to 0s)
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (matrix[i][j] === 1) {
        matrix[i][j] = 0; // Convert isolated land to water
      }
    }
  }

  // Step 3: Restore safe land cells (turn -1s back to 1s)
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (matrix[i][j] === -1) {
        matrix[i][j] = 1; // Restore safe land back to 1
      }
    }
  }

  return matrix;
}

function riverSizes(matrix) {
  //receive a matrix
  //return the an array of where the river lies

  //use helper functions to traverse each river, count its size, and mark the cells as visited

  //create a visited matrix to track which cells have already been processed
  //loop through each cell in the matrix
  //if found an unvisited '1', initiate dfs or bfs to determine river size
  //and mark all connected cells as visited
  //add size of each river to the results array

  const sizes = [];
  const visited = matrix.map((row) => row.map(() => false));

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (visited[i][j]) continue;
      traverseNode(i, j, matrix, visited, sizes);
    }
  }
  return sizes;
}

function traverseNode(i, j, matrix, visited, sizes) {
  let currentRiverSize = 0;
  const nodesToExplore = [[i, j]]; //stack for DFS

  while (nodesToExplore.length) {
    const currentNode = nodesToExplore.pop();
    const [currentI, currentJ] = currentNode;

    if (visited[currentI][currentJ]) continue;
    visited[currentI][currentJ] = true;

    if (matrix[currentI][currentJ] === 0) continue; //skip non-river cells;
    currentRiverSize++;

    const unvisitedNeighbors = getUnvisitedNeighbors(
      currentI,
      currentJ,
      matrix,
      visited
    );
    for (const neighbor of unvisitedNeighbors) {
      nodesToExplore.push(neighbor);
    }
  }
  if (currentRiverSize > 0) sizes.push(currentRiverSize);
}

function getUnvisitedNeighbors(i, j, matrix, visited) {
  const unvisitedNeighbors = [];
  // Check neighbors: up, down, left, right
  if (i > 0 && !visited[i - 1][j]) unvisitedNeighbors.push([i - 1, j]); //up
  if (i < matrix.length - 1 && !visited[i + 1][j])
    unvisitedNeighbors.push([i + 1, j]); //down
  if (j > 0 && !visited[i][j - 1]) unvisitedNeighbors.push([i, j - 1]); //left
  if (j < matrix[0].length - 1 && !visited[i][j + 1])
    unvisitedNeighbors.push([i, j + 1]); //right
  return unvisitedNeighbors;
}

// Do not edit the line below.
exports.riverSizes = riverSizes;

function riverSizes(matrix) {
  const sizeArray = [];

  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[row].length; col++) {
      if (matrix[row][col] === 1) {
        const size = dfs(row, col, matrix);
        sizeArray.push(size);
      }
    }
  }
  return sizeArray;
}

function dfs(row, col, matrix) {
  if (
    row < 0 ||
    row >= matrix.length ||
    col < 0 ||
    col >= matrix[row].length ||
    matrix[row][col] !== 1
  ) {
    return 0;
  }

  matrix[row][col] = -1; //mark as visisted

  let size = 1;

  const directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  for (const [dx, dy] of directions) {
    const newRow = row + dx;
    const newCol = col + dy;
    size += dfs(newRow, newCol, matrix);
  }
  return size;
}

// Do not edit the line below.
exports.riverSizes = riverSizes;

function printerError(s) {
  //receive a string of lowercase letters
  //return the string of errors/length of string

  //'aabcccdddqrs' => "3/18"

  //initialize a count
  //capture the length of string
  //iterate through text of string
  //check if it's not a-m
  //increment count
  //return count / length

  let stringLength = s.length;
  let count = 0;

  let chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"];

  for (let i = 0; i < s.length; i++) {
    if (!chars.includes(s[i])) {
      count++;
    }
  }
  return `${count}/${stringLength}`;
}

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  //optimzed method = using two pointers
  //sort the array
  //create a pointer on the first value
  //create a left pointer after the first value, then create a pointer at the end

  //keep incrementing pointers if total > 0, right moves down, else left moves up

  let answer = [];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue; // Skip duplicates
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      if (nums[i] + nums[left] + nums[right] === 0) {
        answer.push([nums[i], nums[left], nums[right]]);
        left++;
        right--;
      } else if (nums[i] + nums[left] + nums[right] > 0) {
        right--;
      } else {
        left++;
      }
    }
  }
  return answer;
};

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  //receive an array of integers (pos and negtiaves - whole numbers)
  //return an array of arrays of integers that sum up to 0;

  //[-1, 4, -3, 8, 2, 0]
  //return [[-1, 4, -3]]

  //On^3

  //iterate through the entire array with 3 pointers
  //if the total of each === 0 and the values are not the same, add into the answer array
  //return array

  //edge case: if the array is empty, return []

  // let answer = [];

  // for (let i =0; i < nums.length - 2; i++) {
  //     for (let j = i + 1; j < nums.length - 1; j++) {
  //         for (let k = j + 1; k < nums.length; k++) {
  //             if (nums[i] + nums[j] + nums[k] === 0) {
  //                 const triplet = [nums[i], nums[j], nums[k]].sort((a,b) => a -b);

  //                 let isDuplicate = false;
  //                 for (const arr of answer) {
  //                    if (arr[0] === triplet[0] && arr[1] === triplet[1] && arr[2] === triplet[2]) {
  //                     isDuplicate = true;
  //                     break;
  //                    }
  //                 }
  //                 if (!isDuplicate) {
  //                     answer.push(triplet)
  //                 }
  //             }
  //         }
  //     }
  // }
  // return answer

  //optimized: sort the values in the array
  //create one pointer
  //do a left pointer and right pointer
  //check if the sums of all 3 are close to 0
  //if amount > 0 , right-- or else left++
  //add in the 3 numbers into the answer array if found total to 0

  let answer = [];

  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      let total = nums[i] + nums[left] + nums[right];
      if (total === 0) {
        answer.push([nums[i], nums[left], nums[right]]);

        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right + 1]) right++;
        left++;
        right--;
      } else if (total > 0) {
        right--;
      } else {
        left++;
      }
    }
  }
  return answer;
};

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  //receive an array of integers
  //return an array of arrays of triplets that total up to 0

  //brute force:
  //initialize an empty array that will hold all the triplets combinations
  //3 nested for loops
  //in the nested for loops, we will sort the values
  //verify if the values have already been found in the answer array
  //skip it, else we will add in new values
  //return answer

  // let answer = [];

  // for (let i = 0; i < nums.length - 2; i++) {
  //     for (let j = i + 1; j < nums.length - 1; j++) {
  //         for (let k = j + 1; k < nums.length; k++) {

  //             if (nums[i] + nums[j] + nums[k] === 0) {
  //                 let isDuplicate = false
  //                 let sum = [nums[i], nums[j], nums[k]].sort((a,b) => a - b)

  //                 for (const arr of answer) {
  //                     if (arr[0] === sum[0] && arr[1] === sum[1] && arr[2] === sum[2]) {
  //                        isDuplicate= true;
  //                         break;
  //                     }
  //                     }
  //                     if (!isDuplicate) {
  //                     answer.push(sum)
  //                 }
  //             }
  //         }
  //     }
  // }
  // return answer

  //time: O(n^3); space: O(n)

  //optimized = using a while loop with left and right pointer
  //sort the array by smallest to biggest
  //initialize an answer array
  //create a pointer on the first value of the array
  //then create a left pointer next to it
  //then create a righ tpointer to the right of the array
  //while left < right
  //if the values at all 3 pointers === 0
  //add to the answer array
  //else check if the next value is a duplicate of left, then increment left poitner
  //also check if the next value is a duplicate of right, then decrement right pointer
  //check if the sum < 0 , left++
  //else right++
  //return answer

  nums.sort((a, b) => a - b);
  let answer = [];

  for (let i = 0; i < nums.length; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue; // ! remember this
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      let total = nums[i] + nums[left] + nums[right];
      if (total === 0) {
        answer.push([nums[i], nums[left], nums[right]]);

        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;
        left++;
        right--; // ! still need to incrmeent to find other triplets
      } else if (total < 0) {
        left++;
      } else {
        right--;
      }
    }
  }
  return answer;
};

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
  //optimized method
  //initialize a new array to capture results
  //create a pointer at first index in each array
  //iterate through arrays
  //check to see if the values equal each other
  //ask if the results array does not includes the array value
  //if so push it in the arrays
  //return arrays

  let newResults = [];

  for (let i = 0; i < nums1.length; i++) {
    for (let j = 0; j < nums2.length; j++) {
      if (nums1[i] === nums2[j]) {
        if (!newResults.includes(nums1[i])) {
          newResults.push(nums1[i]);
        }
      }
    }
  }
  return newResults;
};

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function (nums, k) {
  //receive an array of integers of pos and neg, k amount of integer
  //return the max average value

  //[3, 5, 2, 5], 2 => 4

  //start at the first pointer
  //add all the numbers up to k index
  //then divide by k

  let maxAverage = -Infinity;

  //let left = 0;
  //let right start at first value;
  //iterate up to k amount, add all the values together
  //divide by k to find maxAverage
  //then update max average if it exceeds

  let left = 0;
  let right = 0;
  let sum = 0;

  while (right < nums.length) {
    sum += nums[right];
    let average = sum / k;

    if (right - left + 1 >= k) {
      maxAverage = Math.max(average, maxAverage);
      sum -= nums[left];
      left++;
    }
    right++;
  }

  return maxAverage;
};

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function (nums, k) {
  //receive an array of integers and an integer k of elements to check
  //return the max average value and return the max average value from k elements in array

  //[2, 3, 4, -4,] k= 2 =[5/2, 7/2, 0/2] =>

  //if array is empty or less than k, then can't find max average value
  //intialize a max average value to 0
  //iterate array starting from first index up to k
  //calc the total average of both
  //then increment by 1 to capture the next 4 newest elements
  //calc the average
  //return average found

  // let maxAverage = -Infinity;

  // for (let i = 0; i<= nums.length - k; i++) {
  //     let sum = 0
  //     for(let j = i; j < i + k;j ++) {
  //        sum += nums[j]
  //     }
  //      let average = sum/k
  //         maxAverage = Math.max(average, maxAverage)
  // }
  // return maxAverage

  //time complexity is O(n * k)

  //sliding window technique:
  //create two pointers of left and right starting at index 0
  //right increments until it hits k amount
  //calc the average
  //update the average
  //return average

  let maxAverage = -Infinity;

  let left = 0;
  let right = 0;
  let sum = 0;

  while (right < nums.length) {
    sum += nums[right];
    let average = sum / k;

    if (right - left + 1 >= k) {
      maxAverage = Math.max(average, maxAverage);
      sum -= nums[left];
      left++;
    }

    right++;
  }
  return maxAverage;
};

//sliding window starts at same index
//then right window moves until it reaches window size
//then it move left pointer up and decrement left pointer away
//then move right pointer to start a new window

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function (s, k) {
  //within the window of k, count how many vowels exist
  //initialize what vowles are
  //initialize a total
  //if s.length is empty, return
  //check if it is a vowel, then add to the sum
  //return max vowels

  let vowels = ["a", "e", "i", "o", "u"];

  if (!s) return;

  let maxSum = 0;
  let sum = 0;

  //calc for the first window
  for (let i = 0; i < k; i++) {
    if (vowels.includes(s[i])) {
      sum++;
      maxSum = sum;
    }
  }

  //calc for the rest
  for (let i = k; i < s.length; i++) {
    if (vowels.includes(s[i])) {
      sum++;
    }
    //subtract out k's if it was a vowel so we do not double count
    if (vowels.includes(s[i - k])) {
      sum--;
    }
    maxSum = Math.max(maxSum, sum);
  }
  return maxSum;
};

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function (s, k) {
  //receive  a string of lowercase letters, and k integers
  //return the max # of vowel letters in an any substring of s with length k
  //'aeiou', k= 2 => 'ae', 'ei'
  //'asassiou', k=3 => 'asa', 'sas', 'ass', 'sio', 'iou' => 3

  //edge case: if k > s.length, return 0

  //create an array of lowercase vowels
  //intialize a count to 0
  //iterate through each char of s up to k amount
  //check to see if window includes
  //increment a count ofvowels
  //return vowels

  //     let vowels = ['a','e','i','o','u']
  //     let maxCount = 0;

  //     for (let i = 0;i <= s.length - k; i++) {
  //         let count = 0
  //         for (let j = i; j < i + k; j++) {
  //             if (vowels.includes(s[j])) {
  //                 count++
  //             }
  //         }
  //         maxCount = Math.max(maxCount, count)
  //     }
  // return maxCount

  //time: O(n * k) space: O(1)

  //optimized: sliding window:
  //create a count, left and right pointer
  //increment right pointer until it hits the length of the array
  //check if the vowels exist,increment count
  //if j reaches the window size
  //take the windown count there

  let left = 0;
  let right = 0;
  let maxCount = 0;
  let count = 0;

  let vowels = ["a", "e", "i", "o", "u"];

  while (right < s.length) {
    if (vowels.includes(s[right])) {
      count++;
    }
    if (right - left + 1 > k) {
      if (vowels.includes(s[left])) {
        count--;
      }
      left++;
    }
    maxCount = Math.max(maxCount, count);
    right++;
  }
  return maxCount;
};

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function (head) {
  //input: head of SLL;
  //return the middle node;

  //test cases: 1 -> null => 1->
  // 1 -> 2 -> 3 -> null => 3->
  //1 -> 2 -> 3 ->4 -> null => 3 ->

  //edge case: if the SLL has only one node, return the node

  //brute force:
  //keep count to iterate through SLL
  //after udpating count, traverse through SLL up to what count stated, return the middle node

  // if (!head) return null;

  // let count = 0;
  // let current = head;

  // while (current !== null) {
  //     current = current.next;
  //     count++
  // }

  // let middleNode = head;
  // for (let i = 0; i < Math.floor(count/2); i++) {
  //     middleNode = middleNode.next;
  // }
  // return middleNode

  //cleaner code - fast and slow pointer

  //create two pointers - one called slow and fast

  //traverse through the SLL until it reaches null
  //slow is going to move by one node
  //fast is going to move by two nodes

  //1 -> 2 -> 3 ->4 -> null => 3 ->
  //slow
  //.        fast

  //   slow
  //                  fast

  let slow = head;
  let fast = head;

  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
};

//time: O(n);
//space: O(1);

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  //receive the head of two linked lists that are sorted
  //return head of one linked lists sorted
  //1 -> 3 -> null
  //1 -> 2 -> null
  // => 1 -> 1 -> 2 -> 3 -> null

  //if linked list1 empty, return list 2
  //if list2 empty, return ll1
  //if both empty, return null

  //create a dummy node
  //then check the value of both first nodes
  //check which one is smaller
  //have dummy's node point to the next node
  //else add in the the other node
  //return list

  if (!list1) return list2;
  if (!list2) return list1;
  if (!list1 && !list2) return null;

  let dummy = new ListNode();
  let tail = dummy;
  let current1 = list1;
  let current2 = list2;

  while (current1 !== null && current2 !== null) {
    if (current1.val < current2.val) {
      tail.next = current1;
      current1 = current1.next;
    } else {
      tail.next = current2;
      current2 = current2.next;
    }
    tail = tail.next;

    if (current1) tail.next = current1;
    if (current2) tail.next = current2;
  }
  return dummy.next;
};

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var swapNodes = function (head, k) {
  if (!head) return null;

  //use two pointers
  let current = head;

  //keep iterating up to k index
  for (i = 1; i < k; i++) {
    //move current to the right by 1
    current = current.next;
  }

  //current holds the left node
  let left = current;
  let right = head;

  //while current is not null
  while (current.next) {
    //move it by one
    current = current.next;
    right = right.next;
  }
  //swap the values
  let temp = left.val;
  //swap left value with right value
  left.val = right.val;
  right.val = temp;
  return head;
};

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function (headA, headB) {
  //receive two head of linked lists
  //return the node they are intersected at (where they share)
  //1 -> 2 -> 3 -> null
  //2 -> 4 -> null
  //=> 2

  //if headA empty or headB empty, return no intersection

  //iterate through both lists at the same time
  //then iterate through the other lists when done traversing with their own lists

  // if (!headA || !headB) return null;

  // let current1 = headA

  // while(current1 !== null) {
  //     let current2 = headB
  //     while (current2 !== null) {
  //         if (current1 === current2) {
  //             return current1
  //         }
  //         current2 = current2.next
  //     }
  //     current1 = current1.next
  // }
  // return null

  //time: O(m*n) ; space: O(1)

  //two pointers -
  //create pointers for headA and headB
  //iterate while both pointers are not null
  //if they are null: switch to the other linked lists to look at, else iterate to the next node
  //return current 1

  if (!headA || !headB) return null;

  let current1 = headA;
  let current2 = headB;

  while (current1 !== current2) {
    current1 = current1 === null ? headB : current1.next;
    current2 = current2 === null ? headA : current2.next;
  }
  return current1;
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let middle = Math.floor((left + right) / 2);
    if (nums[middle] === target) {
      return middle; // Target found, return its index
    } else if (target < nums[middle]) {
      // Compare target with value at middle
      right = middle - 1; // Search left
    } else {
      left = middle + 1; // Search right
    }
  }

  return left; // Return the insert position (left will be the position to insert the target)
};

/**
 * Definition for isBadVersion()
 *
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */

/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function (isBadVersion) {
  /**
   * @param {integer} n Total versions
   * @return {integer} The first bad version
   */
  return function (n) {
    //identify a low point
    //initialize a high point of n
    //bad occurs before n
    //find the middle
    //call the API call
    //return result

    //10 total
    //8

    let low = 1;
    let high = n;

    //know that n is already the bad version and the bad version occured before n

    while (low <= high) {
      let middle = Math.floor((low + high) / 2);
      if (!isBadVersion(middle)) {
        low = middle + 1;
      } else {
        high = middle - 1;
      }
    }
    return low;
  };
};

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  //initialize a low
  //initialize a high

  //brute force:
  //iterate through to x
  //look for all the number squared

  let left = 0;
  let right = x;

  while (left <= right) {
    let m = Math.floor((left + right) / 2);
    let sqr = m * m;

    if (sqr === x) {
      return m;
    } else if (sqr < x) {
      // 1 < 3
      left = m + 1;
    } else {
      right = m - 1;
    }
  }
  return right;
};

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  // Handle edge case for x = 0
  if (x === 0) return 0;

  let left = 1;
  let right = x;

  while (left <= right) {
    let middle = Math.floor((left + right) / 2);
    let sqr = middle * middle; // Calculating middle * middle (square)

    if (sqr === x) {
      return middle; // If exact square root is found
    } else if (sqr < x) {
      left = middle + 1; // The square root is larger, so move the left pointer up
    } else {
      right = middle - 1; // The square root is smaller, so move the right pointer down
    }
  }

  // The loop ends when left > right, and `right` will be the floor of the square root
  return right;
};

/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest = function (k, nums) {
  this.k = k;
  this.minHeap = new minHeap();

  for (let num of nums) {
    this.add(num);
  }
};

/**
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function (val) {
  //stream - keep adding more to the stream
  this.minHeap.add(val);

  if (this.minHeap.size() > this.k) {
    this.minHeap.poll();
  }

  return this.minHeap.peek();
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */

/**
 * @param {number[]} score
 * @return {string[]}
 */
var findRelativeRanks = function(score) {
  let pairs = score.map((value, index) => [value, index]);
  pairs.sort((a,b) => b[0] - a[0]);
  let result = new Array(score.length);

  for (let i = 0; i < pairs.length; i++) {
      const [value, originalIdx] = pairs[i];
      if (i === 0) { 
          result[originalIdx] = "Gold Medal";
      } else if (i === 1) {
          result[originalIdx] = "Silver Medal";
      } else if (i === 2) { 
          result[originalIdx] = "Bronze Medal"
      } else { 
          result[originalIdx] =(i + 1).toString();
      }
  }
  return result
};

Create an array of tuples pairs where each tuple is [score, index].
Sort pairs in descending order based on scores.
Create a result array of the same length as the input to store the ranks.
Iterate over the sorted pairs:
For index 0, assign "Gold Medal".
For index 1, assign "Silver Medal".
For index 2, assign "Bronze Medal".
For all other indices, assign the rank as a string (index + 1).
Return the result array.

function riverSizes(matrix) {
  //receive 2d matrix with 0's as land, and 1's as water
    //return an array back of the size of the rivers found
  
    //intialize an answer array
    //iterate through the rows and columns of the 2d matrix
    //if the cell value is 1, perform dfs to get a size of the river found
    //for dfs function, travel left, right, up down to count for 1's
    //update river size count
    //add size to the array
    //return array
  
    let riverCountArray = [];
  
    for (let row = 0; row < matrix.length; row++) {
      for (let col = 0; col < matrix[row].length; col++) {
        if (matrix[row][col] === 1) {
          let size = dfs(row, col)
          riverCountArray.push(size)
   }
          function dfs(row, col) {
            if (row >= matrix.length || row < 0 ||
               col >= matrix[row].length || col < 0 ||
              matrix[row][col] !== 1)  {
              return 0;
              }
            matrix[row][col] = -1
            let size = 1;
  
            const directions = [
              [0, 1],
              [0, -1],
              [1, 0],
              [-1, 0]
            ]
  
            for (const [dx, dy] of directions) {
              const newRow = row + dx;
              const newCol = col + dy;
              size += dfs(newRow, newCol)
            }
            return size
          } 
      
       
      }
    }
  
    return riverCountArray
  }
  
  // Do not edit the line below.
  exports.riverSizes = riverSizes;
  
  function riverSizes(matrix) {
    //receive a 2d matrix;
     //return an array of the sizes of all rivers in the input matrix
   
     //iterate through the rows and cols
     //check if the matrix value is equal to 1's
     //then perform dfs to check neighbors around it
     //markthe current cell as visited
     //increment count
     //add the count into the result array
     //return array
   
     let answer = []
   
     for (let row = 0; row < matrix.length; row++) {
       for (let col = 0; col < matrix[row].length; col++) {
         if (matrix[row][col] === 1) {
           let sizes = dfs(row, col)
           answer.push(sizes)
     
   function dfs(row, col) {
     if (row < 0 || row >= matrix.length ||
        col < 0 || col >= matrix[row].length ||
         matrix[row][col] !== 1
        ) {
       return 0;
        }
     matrix[row][col] = -1
   
     let sizes = 1
     const directions = [
       [0,1],
       [0, -1], 
       [1, 0],
       [-1,0]
     ]
   
     for (const [dx, dy] of directions) {
       const newRow = dx + row;
       const newCol = dy + col;
       sizes += dfs(newRow, newCol)
     }
     return sizes
   }
           
      
         }
       }
     }
     return answer
   }
   
   // Do not edit the line below.
   exports.riverSizes = riverSizes;
   
   function cycleInGraph(edges) {
    //receive an adjancey list
      //return true if cycle, else false;
    
      //create two sets - one for visited and one for stack
    
      //dfs function
      //check if visisted has the node, return false
      //if stack holds the node, return true
    
      //iterate through all the neighbors of the nodes
      //if dfs on neighbor returns true, return true
    
      //add to stack
      //add to visisted
      
      //delete from stack
    
      //iterate through the node edges
      //check if visisted does not have it and it's been dfs, return true
      //else return false
    
      let visited = new Set();
      let stack = new Set();
    
      function dfs(node) {
          if (stack.has(node)) return true;
        if (visited.has(node)) return false;
    
      visited.add(node)
        stack.add(node)
      
        for (const neighbor of edges[node]) {
          if (dfs(neighbor)) return true
        }
      stack.delete(node)
        return false;
      }
    
    
      for (let node = 0; node < edges.length; node++) {
        if (!visited.has(node) && dfs(node)) return true;
      }
      return false
    }
    
    // Do not edit the line below.
    exports.cycleInGraph = cycleInGraph;
    
    /**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  //receive an array of integers
  //return an array of arrays of triplets that total up to 0

  //brute force:
  //initialize an empty array that will hold all the triplets combinations
  //3 nested for loops
  //in the nested for loops, we will sort the values
  //verify if the values have already been found in the answer array
  //skip it, else we will add in new values
  //return answer

  // let answer = [];

  // for (let i = 0; i < nums.length - 2; i++) {
  //     for (let j = i + 1; j < nums.length - 1; j++) {
  //         for (let k = j + 1; k < nums.length; k++) {
          
  //             if (nums[i] + nums[j] + nums[k] === 0) {
  //                 let isDuplicate = false
  //                 let sum = [nums[i], nums[j], nums[k]].sort((a,b) => a - b)

  //                 for (const arr of answer) {
  //                     if (arr[0] === sum[0] && arr[1] === sum[1] && arr[2] === sum[2]) { 
  //                        isDuplicate= true;
  //                         break;
  //                     }
  //                     }
  //                     if (!isDuplicate) {
  //                     answer.push(sum)
  //                 } 
  //             }
  //         }
  //     }
  // }
  // return answer

//time: O(n^3); space: O(n)

//optimized = using a while loop with left and right pointer
//sort the array by smallest to biggest
//initialize an answer array
//create a pointer on the first value of the array
//then create a left pointer next to it
//then create a righ tpointer to the right of the array
//while left < right
//if the values at all 3 pointers === 0
//add to the answer array
//else check if the next value is a duplicate of left, then increment left poitner
//also check if the next value is a duplicate of right, then decrement right pointer
//check if the sum < 0 , left++
//else right++
//return answer

nums.sort((a,b) => a -b);
let answer = [];

for (let i = 0; i < nums.length - 2; i++) {  
  //Skip duplicates for the first number
  if (i > 0 && nums[i] === nums[i - 1]) continue; // ! remember this
let left = i + 1;
let right = nums.length - 1

while (left < right) { 
  let total = nums[i] + nums[left] + nums[right]
  if (total === 0) { 
      answer.push([nums[i], nums[left], nums[right]])

  while (left < right && nums[left] === nums[left + 1]) left++
  while (left < right && nums[right] === nums[right -1]) right--
  left++;
  right--; // ! still need to incrmeent to find other triplets
} else if (total < 0) { 
  left++
} else { 
  right--
}
 }
}
return answer
};

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
  //receive an array of integers
  //return the max average value of all categories
  
  //[3, 4, 2, -1], 5
  //edge case: if k > nums.length return 0

  //create a pointer and iterate at the first value
  //create a second pointer and iterate at the second value
  //intialize a sum
  //iterate up to k amount
  //calc the max average
  //then return the max average

// if (k > nums.length) return 0

//     let maxAverage = -Infinity

//     for (let i = 0; i <= nums.length - k; i++) {
//         let sum = 0;
//         for (let j = i; j < i + k ;j++) {
//             sum += nums[j]
//         }
//                 let average = sum /k
//                 maxAverage = Math.max(average, maxAverage)
//             }
      
//     return maxAverage
//time: O(n * k)

//sliding window technique: 
//create a left pointer and right pointer starting at the first value
//right pointer increment
//initiatlize a maxAverage and a sum

//increment right while it's less than the length of the array
//add each value
//then check if the window size is >= k
//then calc the maxaverage
//then increment left window up 
//and remove sum of the left window from max average
//return maxAverage

let left = 0;
let right = 0;
let maxAverage = -Infinity;
let sum = 0;

while (right < nums.length) {
  sum+= nums[right]
  if ((right - left + 1) >= k) {
      let average = sum/k
      maxAverage = Math.max(maxAverage, average)

     sum-= nums[left]
     left++
  }
  right++
  
}
return maxAverage

};

function classPhotos(redShirtHeights, blueShirtHeights) {
  //receive an even length of arrays for redshirts and blueshirts
    //return true if can take pics where one is not taller than the other and the same color shirts are all in the same row
    //[1, 2] = red
    //[3,4 ] = blue
    //return true; b/c all blue cna go to back 
  
    //dictate which color is front row
    //sort all the heights in each color
    //iterate through the red array
    //if the frontrow is red
    //then check if blue is not greater than red, then return false
    //likewise if frontrow color was blue
    //return false
  
    //otherwise, return true
  
    redShirtHeights.sort((a,b) => a - b);
    blueShirtHeights.sort((a,b) => a - b);
  
  const frontRow = redShirtHeights[0]< blueShirtHeights[0] ? "RED" : "BLUE"
  
    for (let i = 0; i < redShirtHeights.length; i++) {
      if (frontRow === 'RED') {
        if (redShirtHeights[i] >= blueShirtHeights[i]) return false;
      } else if (blueShirtHeights[i] >= redShirtHeights[i]) return false;
    }
  return true;
  }
  
  // Do not edit the line below.
  exports.classPhotos = classPhotos;
  
  function tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) {
    //receive two arrays of same length for red & blue shirtspeeds
      //return the maxSpeed if fastest is true, else return minSpeed if fastest is false
    
      //[1,2,3]    [3,2,1]   => 7
      //[2,3,4]    [4,3,2]
      //fastest = true
      //return maxspeed
    
      //if fastest = true
      //sort the arrays from biggest to smallest
      //else sort of the arrays from smallest to biggest
      //iterate through each speed
      //add the sum together
      //return maxSpeed seen
    
      if (fastest) ? redShirtSpeeds.sort((a,b))
      
    }
    
    // Do not edit the line below.
    exports.tandemBicycle = tandemBicycle;
    

var RandomizedSet = function() {
  this.map = new Map()
};

/** 
* @param {number} val
* @return {boolean}
*/
RandomizedSet.prototype.insert = function(val) {
  if (!val) {
      return false
  } else {
      this.map.add(val)
      return true
  }
};

/** 
* @param {number} val
* @return {boolean}
*/
RandomizedSet.prototype.remove = function(val) {
  if (!val) {
      return false
  } else {
      this.map.delete(val)
      return true;
  }
};

/**
* @return {number}
*/
RandomizedSet.prototype.getRandom = function() {
  return Math.random()
};

/** 
* Your RandomizedSet object will be instantiated and called as such:
* var obj = new RandomizedSet()
* var param_1 = obj.insert(val)
* var param_2 = obj.remove(val)
* var param_3 = obj.getRandom()
*/

/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
  let totalGas = 0;
  let totalCost = 0;
  let tank = 0;
  let start = 0;
  
      // Step 1: Calculate total gas and total cost
  for (let i = 0; i < gas.length; i++) {
      totalGas += gas[i]
      totalCost += cost[i]
  }
  
      // Step 2: If total gas is less than total cost, return -1
  if (totalGas < totalCost) {
      return -1
  }
  
   // Step 3: Find the starting index using a greedy approach
  for (let i = 0; i < gas.length;i++) {
      tank += gas[i] - cost[i]
  
  // If tank goes negative, move start to i + 1 and reset tank
      if (tank < 0){
          start = i + 1;
          tank = 0;
      }
  }
  
  return start
  };

  /**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
  let totalGas = 0;
  let totalCost = 0;
  let tank = 0
  let start = 0;

  for (let i = 0; i < gas.length;i++) {
      totalGas += gas[i]
      totalCost += cost[i]
  }

  if (totalGas < totalCost) {
      return -1;
  }

  for (let i =0; i < gas.length; i++) {
      tank += gas[i] - cost[i]
  

  if (tank < 0) {
      start = i + 1;
      tank = 0;
  }
}
  return start
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
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
  //receive the root of a node, and integer
  //return true if tree has a path, else false

  //check left and right
  //if total is targetSum, return true
  //else rturn false

//     if (!root) return false

// if (!root.left && !root.right) {
//     return root.val === targetSum
// }

//     return hasPathSum(root.left, targetSum - root.val) ||
//      hasPathSum(root.right, targetSum - root.val);

 
//brute force: initialize a sum
//create a function called checkPathSum taking in the node and currentSum
//if it's a leaf node, check if the path sum matches targetSum

if (!root) return false;

const checkPathSum = (node, currentSum) => {
  currentSum += node.val;
  if (!node.left && !node.right) {
      return currentSum === targetSum
  }


let leftHasPath = node.left ? checkPathSum(node.left, currentSum) : false;
let rightHasPath = noe.right ? checkPathSum(node.right, currentSum): false;

return leftHasPath || rightHasPath;
}
return hasPathSum(root, 0)

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
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
  //receive the root node of a tree, and an integer for target
  //return true if the tree has a root to leaf path
  
  //if tree is empty and targetSum === 0, return true;

  //dfs to the left side
  //add all the values together when there's no more right or left child nodes
  //check if sum === targetSum, return true
  //else return false

  if (!root) return false;

  function dfs(node, sum) {
      sum += node.val
      if (!node.left && !node.right) {
      return sum === targetSum
  }
  let leftHasPath = node.left ? dfs(node.left, sum) : false;
  let rightHasPath = node.right ? dfs(node.right, sum) : false;
  return leftHasPath || rightHasPath
  }

 return dfs(root, 0)
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
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
  //receive the root node of a tree, and an integer for target
  //return true if the tree has a root to leaf path
  
  //if tree is empty and targetSum === 0, return true;

  //dfs to the left side
  //add all the values together when there's no more right or left child nodes
  //check if sum === targetSum, return true
  //else return false

  if (!root) return false;

      if (!root.left && !root.right) {
      return root.val === targetSum
      }

return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val)
};

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
  //receive two arrays of individuals numbers
  //return an array of their intersection
  //[1,2,3,4], [3, 5] => [3]

  //iterate through each number in the longest one
  //check if the array has that value
  //then return the array back

  let output = [];

  for (let i = 0; i < nums1.length; i++) {
      if (nums1.includes(nums2[i])) {
          output.push(nums2[i])
      }
  }
  return output
};

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
  //receive two integer arrays of nums and nums
  //return an array of interestection points they have
  //nums1= [3,4,5] and nums2 = [1, 2] => [ ]
  //nums1 = [3,4,5] and nums=[3,5] => [3, 5]

  //edge cases: if either one of the array is empty, return an empty []

  //create a new array result
  //check if nums1's values exist in nums2 values
  //push in the values into the array result

  if (!nums1 || !nums2) return [ ]

nums1.sort((a,b) => a - b);
nums2.sort((a,b) => a -b );

let i =0;
let j = 0;

let result = new Set()

while (i < nums1.length && j < nums2.length) {
  if (nums1[i] === nums2[j]) {
      result.add(nums1[i])
      i++;
      j++
  } else if (nums1[i] < nums2[j]){
      i++
  } else {
      j++
  }
}

return Array.from(result)
};

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
  const set1 = new Set(nums1);
  const set2 = new Set(nums2);
  let result = []

  for (let nums of set1) {
      if (set2.has(nums)){
          result.push(nums)
      }
  }
return result 
};

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
  //start fast and slow pointer at head
  let fast = head
  let slow = head
  let tmp;
  let prev;

//keep iterating and move fast 2x and slow by 1
  while (fast && fast.next) {
      fast = fast.next.next
      slow = slow.next
  }

//while slow is traversing
//move pointer to the previous pointer
  while (slow) {
      tmp = slow.next;
      slow.next = prev;
      prev = slow
      slow = tmp
  }

//fast will start at head
//slow will start at node
  fast = head
  slow = prev

  while (slow) {
  //if values don't equal eacho ther return false, otherwise check next nodes?
      if (fast.val !== slow.val) return false
      fast = fast.next
      slow = slow.next
  } 
  return true
};

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
  //receive an array of integers, k = integer of top amount seen
  //return top k most frequenet elements
  //[2, 2, 3, 2, 5, 7]

  //frequency counter pattern
  //then sort the object.entries by most seen
  //return top k

//     let obj = {};

// for (let num of nums){
//     obj[num] = (obj[num] || 0) + 1
// }

// const array = Object.entries(obj)
// array.sort((a,b) => b[1] - a[1])

// return array.slice(0, k).map(entry => parseInt(entry[0]))

const freqMap = new Map();
for (let num of nums) { 
  freqMap.set(num, (freqMap.get(num) || 0) + 1);
}

const minHeap = [];
for (let [num, freq] of freqMap) {
  minHeap.push({num, freq});
  minHeap.sort((a,b) => a.freq - b.freq);

  if (minHeap.length > k) { 
      minHeap.shift();
  }
}
return minHeap.map(item => item.num)
};

/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest = function(k, nums) {
  this.k = k;
  this.minHeap = new MinPrioritiyQueue();

  for (let num of num) {
      this.add(num)
  }
};

/** 
* @param {number} val
* @return {number}
*/
KthLargest.prototype.add = function(val) {
  if (this.minHeap.size() < this.lk) { 
      this.minHeap.enqueue(val)
  } else if (val > this.minHeap.front().element) { 
      this.minHeap.dequeue();
      this.minHeap.enqueue(val)
  }
  return this.minHeap.front().element;
};

/** 
* Your KthLargest object will be instantiated and called as such:
* var obj = new KthLargest(k, nums)
* var param_1 = obj.add(val)
*/

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
  //receive an array of arrays
  //return an array of arrays where all overlapping intervals are merged
  //[[0,3], [4, 8], [5, 10]] => [[0,3], [4, 10]]

  //brute force:
  //iterate through each arrays
  //check if the start2 < end1 && end1 < end2
  //update the end with the max endtime
  //add it into the array answer

  let answer = [];
  for (let i = 0; i < intervals.length;i++) {
      for (let j = i + 1; j < intervals.length ;j++) {
       [start1, end1] = intervals[i];
       [start2, end2] = intervals[j]
       if (start2 < end1 && end1 < end2) {
          end = Math.max(end1, end2)
       }
  }
  answer.push(start, end)
  }
  
return answer
};

import {
  Interval,
} from '/opt/node/lib/lintcode/index.js';

/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

export class Solution {
  /**
   * @param intervals: an array of meeting time intervals
   * @return: if a person could attend all meetings
   */
  canAttendMeetings(intervals) {
//receive an array of arrays
//return true if person can attend all meetings, else false

//[[5, 8], [0, 3], [1, 4]] => false

//sort all intervals by start time
//check if the end time of the first interval <= start of next interval
//return false
//return true

intervals.sort((a,b) => a[0]-b[0])

for (let i = 0; i < intervals.length;i++) {
  for (let j = i + 1; j < intervals.length;j++) { 
    const [start1, end1] = intervals[i]
    const [start2, end2] = intervals[j]

    if (start2 <= end1) return false
  }
}
return true
  }
}

/**
 * @param {number[][]} firstList
 * @param {number[][]} secondList
 * @return {number[][]}
 */
var intervalIntersection = function(firstList, secondList) {
  let i = 0;
  let j = 0;
  let result = [];

  while (i < firstList.length && j < secondList.length) { 
      let [start1, end1] = firstList[i];
      let [start2, end2] = secondList[j];

      if (end1 >= start2 && end2 >= start1) { 
          result.push([Math.max(start1, start2), Math.min(end1, end2)])
      }
      if (end1 < end2) { 
          i++
      } else {
          j++
      }
  }
  return result
};

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
  //receive an integer
  //return the squart root of it rounddown

  //81 => output 9

  //left starts 1
  //right starts at x
  //while left < right
  //let's start in the middle to see if you are the sqrt
  //return middle value
  //else if square root < x, right moves down
  //else left moves up

  let left = 1;
  let right = x

  while (left <= right) { 
      let middle = Math.floor((left + right) /2)
      let sqr = middle * middle

      if (sqr === x) { 
          return middle
      } else if (sqr < x) {
             left = middle + 1
      } else { 
       
          right = middle - 1
      }
  }
  return right

//     For x = 8:
// middle = 4 → sqr = 16
// sqr > x, so right = middle - 1 = 3
// middle = 2 → sqr = 4
// sqr < x, so left = middle + 1 = 3
// middle = 3 → sqr = 9
// sqr > x, so right = middle - 1 = 2
// Now, left > right, so the loop ends and the return value is right = 2.
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
 * @return {number[][]}
 */
var pathSum = function(root, targetSum) {
  const results = []

  function dfs(node, remainingSum, currentPath) {
      if (!node) return
      currentPath.push(node.val);
      if (!node.left && !node.right && remainingSum === node.val) {
          results.push([...currentPath])
          //copy because pass by reference - pushing memory of currentPath
      }

      dfs(node.left, remainingSum - node.val, currentPath)
      dfs(node.right, remainingSum - node.val, currentPath)
      currentPath.pop();
  }
  dfs(root, targetSum,[])
  return results
};