// export class Solution {
//   /**
//    * @param intervals: an array of meeting time intervals
//    * @return: if a person could attend all meetings
//    */
//   canAttendMeetings(intervals) {
//     //receive an array of meetings (start and end)
//     //return boolean; true if they can make it; else, false;
//     //[(3, 15), (4, 8)] => false since 15 overlaps with 4 - 8

//     //sort start time
//     //iterate through the intervals
//     //check if the end time is >= start time
//     //return false
//     //else return true

//     intervals.sort((a, b) => a.start - b.start);

//     for (let i = 0; i < intervals.length; i++) {
//       const [end] = intervals[i].end;
//       const [nextStart] = intervals[i + 1].start;
//       if (end > nextStart) {
//         return false;
//       }
//     }
//     return true;
//   }
// }

// console.log(
//   canAttendMeetings([
//     [3, 15],
//     [4, 8],
//   ])
// );

function smallestDifference(arrayOne, arrayTwo) {
  //receive two arrays of integers
  //return a pair of integers that are closest to 0

  //[3, 5, 2, 1]
  //[7, 3, 2]

  //[3, 3] = 0 => expectation of the return

  //sort both arrays
  //initialize a total to 0;
  //create a pair array

  //edge case: if both arrays are empty, return [];
  //edge case: if one array is empty, return [];

  //create pointers in both arrays starting at the first index
  //check if sum is smaller than the current sum
  //if so, add it in the pair array
  //else check if value in the first array is greater than value in second array,
  //if so, move the pointer accordingly
  //return the pair

  //objective:  trying to find two numbers that are as close as possible in value.

  arrayOne.sort((a, b) => a - b);
  arrayTwo.sort((a, b) => a - b);

  let pair = [];
  let difference = Number.MAX_SAFE_INTEGER;

  let i = 0;
  let j = 0;

  while (i < arrayOne.length && j < arrayTwo.length) {
    const oneValue = arrayOne[i];
    const twoValue = arrayTwo[j];
    let tempSum = Math.abs(oneValue - twoValue);
    // console.log(tempSum, oneValue, twoValue);

    if (tempSum < difference) {
      difference = tempSum;
      pair = [oneValue, twoValue];
    }
    oneValue < twoValue ? i++ : j++; // ! bigger number to get the smaller difference
  }
  return pair;
}

// Do not edit the line below.
exports.smallestDifference = smallestDifference;

console.log(smallestDifference([3, 5, 2, 1], [7, 3, 2]));

function longestPeak(array) {
  //receive an array of integers 9pos and negative
  //return the length of longest peak (strictly increasing followed by a drop (decrease))

  //edge case: if values < 3, can't make a peak (increasing and then  a decrease)

  //best place to start with this algo is to find the peak;
  //then look left and right to figure out length

  //initialize peakTotal;
  //initialize a pointer;

  //iterate until we hit the last element

  //check if it is a peak (value before it is smaller && value after is lower)
  //use two pointer strategies
  //left to check if value is still decreasing
  //right to check if value is still decreasing
  //then take index at right - left to update the length
  //take the max version
  //return the length

  if (array.length < 3) return 0;

  let longestPeakLength = 0;
  let i = 1;

  while (i < array.length - 1) {
    const isPeak = array[i - 1] < array[i] && array[i] > array[i + 1];

    if (!isPeak) {
      i++;
      continue;
    }

    let left = i - 2;

    while (left >= 0 && array[left] < array[left + 1]) {
      left--;
    }

    let right = i + 2;

    while (right < array.length && array[right] < array[right - 1]) {
      right++;
    }

    //right - left - 1 b/c the left and right pointer are accounted by + 2 outside of the loop
    longestPeakLength = Math.max(longestPeakLength, right - left - 1);
    i = right;
  }

  return longestPeakLength;
}

// Do not edit the line below.
exports.longestPeak = longestPeak;

// Do not edit the class below except for the buildHeap,
// siftDown, siftUp, peek, remove, and insert methods.
// Feel free to add new properties and methods to the class.
class MinHeap {
  constructor(array) {
    this.heap = this.buildHeap(array);
  }

  buildHeap(array) {
    //
  }

  siftDown() {
    // Write your code here.
  }

  siftUp(currentIdx, heap) {
    //find the parent index
    //keep going while element hasn't reached the beginning of the array
    //and as long as the value is < parent
    //swap the newNode and parent
    //assign the newNode's temp and parent's value
    //newNode = parent's Idx
    //recalc parent's Idx if necessary

    let parentIdx = Math.floor((currentIdx - 1) / 2);
    while (currentIdx >= 0 && heap[currentIdx] < heap[parentIdx]) {
      this.heap.swap(currentIdx, parentIdx, heap);
      currentIdx = parentIdx;
      parentIdx = Math.floor((currentIdx - 1) / 2);
    }
  }

  peek() {
    this.heap[0];
  }

  remove() {
    // Write your code here.
  }

  insert(value) {
    //push the element
    //sift up if necessary to make sure nodes are correct
    this.heap.push(value);
    this.siftUp(this.heap.length - 1, this.heap);
  }

  swap(i, j, heap) {
    let temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
}

// Do not edit the line below.
exports.MinHeap = MinHeap;

function seatsInTheater(nCols, nRows, col, row) {
  //receive the total rows and totals, plus where I'm sitting (what row and col my seat is in)
  //return total of how many seats are behind me and to the left of me;

  //calc how many cols left taking total - where I'm sitting - 1;
  //calc how many rows taking total rows - where i'm sitting
  //multiply together and return the rows

  let colsLeft = nCols - (col - 1);
  let rowsLeft = nRows - row;
  return colsLeft * rowsLeft;
}

// add the value "codewars" to the websites array 1,000 times
var websites = [];
// const websites = new Array(1000).fill("codewars")

for (let i = 0; i < 1000; i++) {
  websites.push("codewars");
}
