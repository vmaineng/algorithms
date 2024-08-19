export class Solution {
  /**
   * @param intervals: an array of meeting time intervals
   * @return: if a person could attend all meetings
   */
  canAttendMeetings(intervals) {
    //receive an array of meetings (start and end)
    //return boolean; true if they can make it; else, false;
    //[(3, 15), (4, 8)] => false since 15 overlaps with 4 - 8

    //sort start time
    //iterate through the intervals
    //check if the end time is >= start time
    //return false
    //else return true

    intervals.sort((a, b) => a.start - b.start);

    for (let i = 0; i < intervals.length; i++) {
      const [end] = intervals[i].end;
      const [nextStart] = intervals[i + 1].start;
      if (end > nextStart) {
        return false;
      }
    }
    return true;
  }
}

console.log(
  canAttendMeetings([
    [3, 15],
    [4, 8],
  ])
);
