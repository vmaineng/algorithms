def spiral(matrix):
    output= []

    startRow, endRow = 0, len(matrix) -1
    startCol, endCol = 0, len(matrix[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            output.append(matrix[startRow][col])
        startRow += 1

        # for row in range(startRow, endRow + 1):
        #     output.append(matrix[row][endCol])
        # endCol -=1
    return output



print(spiral([[1,2]]))