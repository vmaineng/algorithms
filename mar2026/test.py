def addTree(root):
    if not root:
        return 0
    
    return root.value + addTree(root.left) + addTree(root.right)
def intersection(a, b):
  #receive a two list o fintegers
  #return a list back of items that exist in both

  #iterate through each item in the list
  #check if it's in second list
  #add to the result
  #return result

  # result = []
  # for item in a:
  #   if item in b:
  #     result.append(item) 
  # return result

  #time: O(n * m)
  #space:O(min(n,m))

  #create a unique set of a
  #iterate through b
  #check if set has it
  #return item sin a result

  result = []
  uniqueA = set(a)
  for item in b:
    if item in uniqueA:
      result.append(item)
  return result

  #time: O(n +m)

  def exclusive_items(a, b):
  #receive two list of integers
  #return a list back of integers that do not exist in other

  #ex: 

  #initialize a result
  #iterate through a
  #check if it's not in b
  #add in list

  # result = []
  # for item in a:
  #   if item not in b:
  #     result.append(item)

  # for item in b:
  #   if item not in a:
  #     result.append(item)
  # return result

  #time: O(n * m)
  #space:O(n + m)

  #create a set of both
  uniqueA = set(a)
  uniqueB = set(b)

  result = []
  for num in a:
    if num not in uniqueB:
      result.append(num)

  for num in b:
    if num not in uniqueA:
      result.append(num)
  return result
