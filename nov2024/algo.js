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
