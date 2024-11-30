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

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  //receive an array of integers
  //return an array of arrays of triplets that total 0

  //iterate through nums.length 3 times
  //check if the sum === 0;
  //if they do, then sort the tree values
  //check if isDuplicate true, then break out of the loop and do not add it in
  //else add in isDuplicate
  //return output array

  // let output = [];
  // for (let i = 0; i < nums.length - 2; i++) {
  //     for (let j = i + 1; j < nums.length - 1; j++) {
  //         for (k = j + 1; k < nums.length; k++) {
  //             if (nums[i] + nums[j] + nums[k] === 0) {
  //                 let isDuplicate = false;

  //                 const triplet = [nums[i], nums[j], nums[k]].sort((a,b) => a - b);

  //                 for (const arr of output) {
  //                     if (arr[0] === triplet[0] && arr[1] === triplet[1] && arr[2] === triplet[2]){
  //                         isDuplicate = true;
  //                         break;
  //                     }
  //                 }
  //                 if (!isDuplicate) {
  //                     output.push(triplet)
  //                 }
  //             }
  //         }
  //     }
  // }
  // return output
  nums.sort((a, b) => a - b);
  let output = [];

  for (let i = 0; i < nums.length; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      let total = nums[i] + nums[left] + nums[right];
      if (total === 0) {
        output.push([nums[i], nums[left], nums[right]]);

        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;
        left++;
        right--;
      } else if (total < 0) {
        left++;
      } else {
        right--;
      }
    }
  }
  return output;
};

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  //receve an array of integers - including positive and negative numbers
  //return back an array of array of triplets that sums up to 0;

  //ex: [1,1, -3, -5,8, 20] =>
  //.          i
  //.             j
  ///                k

  //create 3 pointers
  //check the total to make sure they do add up to 0
  //sort the triplets answers
  //check if the triplet answer in our answer array to see if there
  // is triplet already
  //if exist, skip it
  //add it into our answer array

  let answer = [];
  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        if (nums[i] + nums[j] + nums[k] === 0) {
          const triplet = [nums[i], nums[j], nums[k]].sort((a, b) => a - b);
          let isDuplicate = false;
          for (let arr of answer) {
            if (
              arr[0] === triplet[i] &&
              arr[1] === triplet[j] &&
              arr[2] === triplet[k]
            ) {
              isDuplicate = true;
              break;
            }
          }
          if (!isDupliate) {
            answer.push(triplet);
          }
        }
      }
    }
  }
  return answer;
};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  //receive an array of integers, and an integer
  //return the index positions of the first two numbers that adds up to target
  //[0, 2, 45, 6], 45 => [0, 2]

  //look through each num and see if it adds up to the target
  // for (let i = 0; i < nums.length; i++) {
  //     for(let j = i + 1; j < nums.length; j++) {
  //         if (nums[i] + nums[j] === target) {
  //             return [i , j]
  //         }
  //     }
  // }

  //optimized
  //create an object
  //store the index position as the value as continue through the nums
  //find the difference between target and current value
  //if we found it, return the key index position

  let answer = {};

  for (let i = 0; i < nums.length; i++) {
    let difference = target - nums[i];
    if (answer.hasOwnProperty(difference)) {
      return [answer[difference], i];
    } else {
      answer[nums[i]] = i;
    }
  }
};
