matrix = [
    [0, 1, 1, 0],  # Node 0
    [1, 0, 1, 0],  # Node 1
    [1, 1, 0, 1],  # Node 2
    [0, 0, 1, 0]   # Node 3
]

node_values = [5, 3, 7, 2] #arbitary values
#              0  1  2  3
# Print node values
print("Node values:")
for i in range(len(matrix)):
    print(f"Node {i}: {node_values[i]}")

# Print connections
print("\nConnections:")
for i in range(len(matrix)):
    connections = [j for j in range(len(matrix[i])) if matrix[i][j] == 1]
    print(f"Node {i} connects to: {connections}")

const breadthFirstSearch = (graph, startNode) => {
  const queue = [startNode]
  while queue.length > 0 { 
    const current = queue.shift()
    console.log(current)
    for (const neighbor of graph[current]) {
      queue.push(neighbor)
    }   
  }
}

def has_path(graph, src, dst):
  #dfs
  #receives a graph, node, and distance
  #return True if path from src to destination nodes
  #ex: graph = { 
  #  'f': ['g']
  #   'h': []
  #}

  #graph, 'f', 'g' => True
  #graph, 'f', 'h' => False

  #base case: 
  #if src == dist, return True
  #else recursively call to it's next neighbors

  # if src == dist:
  #   return True
  # for neighbor in graph[src]:
  #  if(has_path(graph, neighbor, dist) == True):
  #    return True
  # return False

  #bfs
  from collections import dequeue

  dequeue = [src]
  while dequeue.length > 0:
    current = dequeue.popleft()

    if current == dst:
      return True
      
    for neighbor in graph[current]:
      queue.push(neighbor)
    return False
       
       def how_much_i_love_you(nb_petals):
    #receive a flower of x amount of petals
    #return the saying that the last petal struck on 
    #ex: '3' => 'a lot'
    #ex: '10' => 'madly'
    
    #edge cases: if flower with no petal
    
    #take the # of petals % length of array
    
    sayings= ["I love you", 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    
    return sayings[nb_petals % (len(sayings)) - 1]

    def reverse_list(l):
    #receive a list of integers
    #return the the lists of the elemnts in reversed
    #ex: [0,2,3,4] => [4, 3, 2,0]
    #ex: [1] => [1]
    #ex: [] => []
    
    #initialize an empty list
    #iterate through element, starting from the end to the first index number
    #push it into the empty list
    #return the list
    
#     reversedList = []
#     for ele in range(len(l) - 1, -1, -1):
#         reversedList.append(l[ele])
#     return reversedList
        

    #time: O(n) n for each ele in list
    #space: O(n) n for each ele in list
    
    return l[::-1]
#time:O(n) for n amount of ele in list
#space:O(1)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #receive a list a of integers, and an integer for extra candies
        #return back a list of boolean where if the kid has more candy than the max, return true, else return False

        #ex: [2, 3, 5, 1, 3] , extracandies = 3
        #maxCandy = 5

        #adding 3 = [5, 6, 8, 4, 6]
        #ex:        [True, True, True, False, True]

        #find the current maxCandy

        #ex: [4, 2, 1, 1,2], extracandies = 1
        #maxCandy: 4

        #add the extraCandies of 1
        #new [ 5, 3, 2, 2, 3]
        #answer = [True, False, False, False, False]

        #find the maxcandy in the candies list
        #initialize a newTotal List
        #iterate through the candies list, add extraCandies to the new total
        #add the new total into the newTotal list
        #iterate through each ele in the newTotal
        #check if newTotal >= maxCandy
        #if it is, return True, else Return False

        # newTotal = []
        # result = []
        # maxCandy = max(candies)

        # for value in candies:
        #     value += extraCandies
        #     newTotal.append(value)

        
        # for value in newTotal:
        #     if value >= maxCandy:
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result

        # return [True if value >= maxCandy else False for value in newTotal]

        #time: O(2n) => O(n) n how many kids in list
        #space: O(n) => n how many kids in list

        maxCandy = max(candies)
        return [candy + extraCandies >= maxCandy for candy in candies]