// Description
// Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
//find the minimum number of conference rooms required.

// (0,8),(8,10) is not conflict at 8

// Example
// Example1

// Input: intervals = [(0,30),(5,10),(15,20)]
// Output: 2
// Explanation:
// We need two meeting rooms
// room1: (0,30)
// room2: (5,10),(15,20)

//receive an array of arrays (intervals: [start, end])
//return an integer back of min rooms needed

//ex: [[3,8], [1, 4], [9, 10]] =>
//[[1,4], [3,8], [9,10]]

//startArrays = [1, 3, 9]
//                     i     minrooms = 2, maxRoom = 2
//endArrays = [4, 8, 10]
//         j
//initialize a variable minMeetingROom = 0
//break out start and end times in their own separate arrays
//while loop with pointers in both arrays that are < the length
//traverse through the start array
//every time we need a room, increment minMeeting room
//else check if the end time is less than the next start time
//decrement the room
//return the max meeting room found

function minMeetingRooms(intervals) {
  let startArray = intervals.sort((a, b) => a[0] - b[0]).map((num) => num[0]);
  let endArray = intervals.sort((a, b) => a[1] - b[1]).map((num) => num[1]);
  //   console.log("startArray", startArray);
  //   console.log("endArray", endArray);
  let minRooms = 0;
  let maxRooms = 0;
  let startPtr = 0;
  let endPtr = 0;

  while (startPtr < intervals.length) {
    if (startArray[startPtr] < endArray[endPtr]) {
      minRooms++;
      startPtr++;
    } else {
      minRooms--;
      endPtr++;
    }
    maxRooms = Math.max(minRooms, maxRooms);
  }
  return maxRooms;
}

console.log(
  minMeetingRooms([
    [3, 8],
    [1, 4],
    [9, 10],
  ])
);
