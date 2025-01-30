def can_attend_meetings(intervals):

    if len(intervals) < 2:
        return False

    intervals.sort()
    for i in range(len(intervals)):
        print('current', intervals[i])
        if intervals[i][0] <= intervals[i + 1][1]:
            return False
    return True
print(can_attend_meetings([[3,6], [1, 4]]))

#time: O(n log n)
#space: O(1)