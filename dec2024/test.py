# def each_const(lst, n):
#     result = []
#     for i in range(len(lst) - n + 1):
#         result.append(lst[i:i+n])
#     return result

# print(each_const([12,3,4,5,6], 2))

def traverse_spiral(lst):
    result = []
    startRow, endRow = 0, len(lst) - 1
    startCol, endCol = 0, len(lst[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(lst[startRow][col])
        col +=1

        for row in range(startRow +1, endRow + 1):
            result.append(lst[row][endCol])
    
    
    return result

print(traverse_spiral([[1,2,3], 
[4, 5, 6]]))