/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

// export class Solution {
//   /**
//    * @param intervals: an array of meeting time intervals
//    * @return: if a person could attend all meetings
//    */
var canAttendMeetings = function (intervals) {
  //receive an array of arrays of start and end time
  //return true if they can attend all meetings, else return false
  //ex: [[0, 1], [2, 5], [2, 3]] => return false

  //         -----
  //         --------------
  //-----
  // 0   1.   2.  3.   4.  5

  //iterate through the entire intervals
  //set up pointers to look at the first intervals, and look at the second intervals
  //check if the start time of the second interval < end time
  //return false
  //else return true

  //if no intervals, return true
  if (!intervals) return true;

  for (let i = 0; i < intervals.length; i++) {
    //[2, 5]
    for (let j = i + 1; j < intervals.length; j++) {
      //[2,3]
      const [start1, end1] = intervals[i]; //[2,5]
      const [start2, end2] = intervals[j]; //[2, 3]

      if (start2 < end1 && start1 < end2) {
        console.log(start1, end1, start2, end2);
        //2 < 5 && 2< 3
        return false;
      }
    }
  }
  return true;
};
// }
// console.log(
//   canAttendMeetings([
//     [0, 1],
//     [2, 5],
//     [2, 3],
//   ])
// );

/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

//   export class Solution {
//     /**
//      * @param intervals: an array of meeting time intervals
//      * @return: the minimum number of conference rooms required
//      */
var minMeetingRooms = function (intervals) {
  //receive an array of arrays
  //return the minRoomsNeeded
  //ex: [[0, 1], [2, 5], [2, 3]]
  //      1      0   1. +    1 = 2

  //initialize a variable to track minRoomsNeeded
  //iterate through the entire intervals
  //keep track of the first interval, keep track of second interval
  //check if the start2 < end1,
  //add conference rooms
  //update minRoomsNeeded to the amount that we're currently seeing
  //return minRoomsNeeded

  let minRoomsNeeded = 0;

  for (let i = 0; i < intervals.length; i++) {
    let additionalRooms = 1;
    for (let j = i + 1; j < intervals.length; j++) {
      const [start1, end1] = intervals[i];
      const [start2, end2] = intervals[j];

      if (start1 < end2 && start2 < end1) {
        additionalRooms++;
      }
    }
    minRoomsNeeded = Math.max(minRoomsNeeded, additionalRooms);
  }

  return minRoomsNeeded;
};

// console.log(
//   minMeetingRooms([
//     [0, 1],
//     [2, 5],
//     [2, 3],
//   ])
// );

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  //receive an array of arrays
  //return a new array of arrays where overlapping intervals are combined together
  //ex: [[0, 1], [2, 5], [2, 3]] => [[0,1], [2, 5]]

  //         -----
  //         --------------
  //-----
  // 0   1.   2.  3.   4.  5

  //initialize a variable to hold the first interval
  //iterate starting at the first index
  //check if the end time of the second interval < end time of the first interval
  //if so, update end interval to the max value seen
  //else, just add in the interval

  //if overlapinteral is empty, return an array of array

  // if (!intervals) return [[]]
  console.log("intervals before sort:", intervals);
  intervals.sort((a, b) => a[0] - b[0]);
  console.log(intervals);

  let overlapInterval = [intervals[0]]; //[2, 5]

  for (let i = 1; i < intervals.length; i++) {
    const [start1, end1] = intervals[i]; //[2,3]
    const results = overlapInterval[overlapInterval.length - 1]; //[[2,5]]

    //ex: [[0, 1], [2, 5], [2, 3]] => [[0,1], [2, 5]]
    if (results[1] >= start1) {
      //5 < 2
      console.log(results[1]);
      results[1] = Math.max(end1, results[1]);
    } else {
      overlapInterval.push(intervals[i]);
    }
  }
  return overlapInterval;

  //time: O(n)
  //space: O(n)
};

console.log(
  merge([
    [1, 4],
    [0, 1],
  ])
);
