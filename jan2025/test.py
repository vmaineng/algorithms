from typing import List

def attend_meeting(self, intervals: List[Interval]) -> bool:
    if len(intervals) <=1:
        return True
    
    intervals.sort(key=lambda x: x.start)

    for i in range(len(intervals) - 1): 
        if intervals[i].end <= intervals[i + 1].start:
            return False
    return True

print(attend_meeting([(1,3), (2,5)]))