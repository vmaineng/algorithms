from typing import List

def attend_meeting(intervals: List[List[int]]) -> bool:
    if len(intervals) <=1:
        return True
    
    intervals.sort(key=lambda x: x[0])

    for i in range(len(intervals) - 1): 
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    return True

# print(attend_meeting([(1,3), (2,5)]))

class Interval:
    def __init__(self, start: int, end:int):
        self.start = start
        self.end = end

def min_meeting(intervals: List[List[int]]) -> int:
    #receive a list of integers
    #return min amount of rooms needed
     #ex: [(1,3), (2, 5), (6, 7)] => 2
    
    #keep track of rooms needed
    #sort start times, end times

    #iterate through the list with start and end pointer
    #if end > start, increment rooms, move start pointer
    #else subtract rooms, increment end pointer
    #return min rooms

    minRooms = 0

    start = sorted(intervals.start for interval in intervals)
    end = intervals[i].sort(intervals.end for interval in intervals)

    startPtr, endPtr = 0,0

    while startPtr < len(start) and endPtr < len(end):
        if start[startPtr] < end[endPtr]:
            minRooms += 1
            startPtr += 1
        else:
            minRooms -=1
            endPtr += 1
    return minRooms
