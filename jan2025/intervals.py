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
    
    class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #receive a list of lists
        #return the list where the lists are merged in

        #ex: [[1,3], [7,8]] => [[1,3], [7,8]]

        #sort the lists by start time
        #initialize a result list to with the first interval from intervals
        #iterate through the intervals
        #check if the start time of current interval <= end time
        #if so, update the the end time to max end time
        #else
        #add in the interval b/c no cnflict
        #return results

        intervals.sort(key=lambda x:x[0])

        results = [intervals[0]]

        for i in range(1, len(intervals)):
            currentStart, currentEnd = intervals[i]
            prevStart, prevEnd = results[-1]
            if currentStart <= prevEnd:
                results[-1][1]= max(currentEnd, prevEnd)
            else:
                results.append(intervals[i])
        return results
        

        #insert intervals:
        def insert_interval(intervals, new_interval):
            result = []
            i = 0
            
            while i < len(intervals) and intervals[i][1] < new_interval[0]:
                result.append(intervals[i])
                i += 1

            while i < len(intervals) and intervals[i][0] <= new_interval[1]:
                newInterval[0]= min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                i += 1
            result.append(new_interval)

            while i < len(interval):
                result.append(intervals[i])
                i += 1
            return result

            class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #receive a list of lists
        #return a new list inserting in the newInterval
        #ex: [[3,5], [1,3]], [6,8] => [[1,5], [6,8]]

        #sort the intervals based on start time
        #iterate through the list
        #have an i pointer
        #iterate through the intervals
        #check if the interval is less than the new interval start
        #update the start and end time of new interval
        #return the new list

        # result = []
        # i = 0

        # while i < len(intervals) and intervals[i][1] < newInterval[0]:
        #     result.append(intervals[i])
        #     i += 1
        
        # while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        #     newInterval[0] = min(intervals[i][0], newInterval[0])
        #     newInterval[1] = max(intervals[i][1], newInterval[1])
        #     i += 1
        # result.append(newInterval)

        # while i < len(intervals):
        #     result.append(intervals[i])
        #     i += 1

        # return result

        
        intervals.append(newInterval)
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res

        

import heapq

def min_meeting_rooms(interval):
    if not intervals:
        return 0
    
    intervals.sort(key = lambda x:x[0])
    heap = []
    heapq.heappush(heap, intervals[0][1])

    for interval in intervals[1:]:
        if interval[0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])
    return len(heap)