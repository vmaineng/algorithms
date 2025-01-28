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

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #receive a list of list of integers
        #return a list where all intervals overlapping merged together

        #ex: [[1,4], [2, 5], [7,8]] => [[1,5], [7,8]]

        #sort the list of integers based on start time
        #create an empty list set with the first list from intervals
        #iterate through the list of arrays starting at the second interval
        #check if end time > start time
        #update the end time of the interval
        #else merge in the interval
        #return new result

        intervals.sort(key = lambda x:x[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            [start, end] = intervals[i]
            [prevStart, prevEnd] = result[-1]
            if prevEnd >= start:
                result[-1][1] = max(prevEnd, end)
            else:
                result.append(intervals[i]) 
        return result
        