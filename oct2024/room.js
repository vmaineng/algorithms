function minMeetingRooms(intervals) {
  // Write your code here

  //receive an array of arrays of (start, end)
  //return min conference rooms needed
  //[[0, 1], [1,3]] => return 1

  //initialize a count for rooms
  //iterate through intervals
  //check if the end time < start time of next intervals
  //increment rooms

  let count = 0;

  for (let i = 0; i < intervals.length; i++) {
    let roomsNeeded = 1;
    for (let j = i + 1; j < intervals.length; j++) {
      if (i !== j) {
        const [start1, end1] = intervals[i];
        const [start2, end2] = intervals[j];
        console.log(start1, end1, start2, end2);
        if (start1 < end2 && start2 < end1) {
          roomsNeeded++;
          console.log(start1, end1, start2, end2);
        }
      }
    }
    count = Math.max(count, roomsNeeded);
  }
  return count;
}

console.log(
  minMeetingRooms([
    [1, 3],
    [0, 1],
  ])
);
