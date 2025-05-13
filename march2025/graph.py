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

        class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #receive a list of nums ranging from postive to negative
        #return max average from nums list that is equal to k
        #ex: [3, 5, 6, -3, 2], k = 3 
        #.   [3, 5, 6]         sum(of 3)/3  14/3 = 4.66667 max = 4.66667
        #       [5, ,6, -3].     8/3 =2.66667
        #          [ 6, -3, 2]   5/3 =1.66667

        #initialize a max variable -inf
        #iterate through nums list, starting at the first index, iterate up to k amount
        #find the average
        #check if the average > max
        #update max
        #else, move on to the next set

        if len(nums) < 2:
            return nums[0]

        maxAvg = float("-inf")
        average = 0
        avg = 0

        # left = 0
        # right = k

        # while (right < len(nums)): 
        #     average += nums[left]
        #     print(average)
        #     if average/k > max:
        #         max = average/k
        #     left = right
        #     right += 1
        # return max

        left = 0
        right = 0

        while (right < len(nums)):
            average += nums[right]
            right += 1
            # print(average)

            # print(right - left)

            if (right - left) == k:
                
                avg = average/k
                # print(avg)
                if avg > maxAvg:
                    maxAvg = avg
                average -= nums[left]
                left += 1
        return maxAvg
    
    def has_path(graph, src, dst):
  #receive a adj matrix
  #return True if src node connects to dst, else False

  #dfs recursive:
  #base case: if src == dst, return True
  #else call it on neighbor node in src
  #else return False
  if src==dst:
    return True
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst):
      return True
  return False
  

from collections import deque

def has_path(graph, src, dst):
  #recieve a graph, src, and dst
  #return True if path between src, dst, else False

  #bfs:
  #initialize graph into a queue
  #while queue's length > 0
  #pop off currentNode
  #then iterate through it's children
  #add to queue
  #if currentNode = dst, return True
  #else return False

  # if not graph:
  #   return False
  queue = deque([src])
  while queue:
    currentNode = queue.popleft()
    if currentNode == dst:
      return True
    for neighbor in graph[currentNode]:
      queue.append(currentNode)
  return False
      
  def undirected_path(edges, node_A, node_B):
  #receive an edges adj list, two sep nodes
  #returnn True if path exists between the two nodes, else False

  #convert into adj matrix
  #then dfs, check if it's neighbors exists

  graph = build_graph(edges)
  return has_path(graph, node_A, node_B)

def has_path(graph, src, dst):
  if src==dst:
    return True
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst):
      return True
  return False
  
def build_graph(edges):
  graph = {}
 
  for edge in edges: 
    a,b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph
  
