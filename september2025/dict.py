from collections import defaultdict
def findJudge(n: int, trust: list[list[int]]) -> int:
    #receive a list of lists where [a,b] a trusts b
    #return the number where they don't trust anyone

    #implement a key-value pair for incoming and outgoing
    #iterate through each num
    #check if the n exists in incoming and outgoing has none:
    #return the number
    #else return -1

    incoming = defaultdict(int)
    outgoing = defaultdict(int)
    print(incoming, outgoing)

    for src, dst in trust:
        outgoing[src] += 1
        incoming[dst] += 1
        print(incoming, outgoing)

    for person in range(1, n+1):
        if incoming[person] == n - 1 and outgoing[person] == 0:
            return person
    return -1

print(findJudge(4, [[1,3],[4,3],[2,3]]))

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #receive a m x n grid
        #return maxarea seen

        #initialize a count
        #iterate through each square
        #check if it is 1, then dfs traverse
        #return the max count seen 

        count = 0
        newMax = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if row > 0 or col > 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return 0
            grid[row][col] == 0
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col -1)
            dfs(row, col + 1)
            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    newMax = dfs(row, col)
                count = max(count, newMax)
        return count