def longest_word(sentence):
  #receive a string of lowercase letters
  #return longest word found

  #ex: 'hello my name is' => 'hello'

  #split the words
  #iterate through each word to see longest length
  #return longest length found

  longWord = ''
  longWordLen = float("-inf")

  words = sentence.split()

  for char in range(len(words)):
    print(words[char])
    if len(words[char]) >= longWordLen:
      longWordLen = len(words[char])
      longWord = words[char]
  return longWord


from math import sqrt, floor
def is_prime(n):
  #receive an integer
  #return True if is_prime, else false
  #ex: 4 => False, b/c 2 and 1 goes in it

  #iterate up to n amount
  #if n mods by every number, return False
  #else return True

  # count = 0

  # for num in range(2, n + 1):
  #   print(num, n, count)
  #   if n % num == 0:
  #     print(num, n, count)
  #     count += 1

  # if count > 1:
  #   return False
  # else:
  #   return True

  if n < 2:
    return False

  for num in range(2, floor(sqrt(n)) + 1):
    if n % num == 0:
      print(n, num)
      return False
  return True


def is_prime(n):
  #receive an integer
  #return boolean True if it is a prime, else false

  #ex: 4 => false

  #iterate up to n
  #check if it's divisble by another number, return false
  #after checking everything, return True

  if n < 2:
    return False

  for i in range(2, n):
    if n % i == 0:
      return False

  return True


from math import sqrt, floor

def is_prime(n):
  #receive an integer
  #return boolean True if it is a prime, else false

  #ex: 4 => false

  #iterate up to n
  #check if it's divisble by another number, return false
  #after checking everything, return True

  if n < 2:
    return False

  # for i in range(2, n):
  #   if n % i == 0:
  #     return False

  # return True

  for i in range(2, floor(sqrt( n)) + 1):
    if n % i == 0:
      return False
  return True

def pairs(elements):
  #receive a list of unique elements
  #return a pair of elements

  #iterate starting from beginning
  #iterate next to it
  #add it to the pair

  result = []

  for i in range(0, len(elements)):
    for j in range(i + 1, len(elements)):
      pair = [elements[i], elements[j]]
      result.append(pair)
  return result

def anagrams(s1, s2):
  #receive two strings lowercase
  #return True if same amount of letters are used,e lse False

  #ex: 'happy', 'fish' => False

  # return sorted(s1) == sorted(s2)
  #time: O(n log n )
  #space: O(n)

  #use object to count frequency

  chars = {}

  for char in s1:
    if char not in chars:
      chars[char] = 1
    chars[char] += 1

  for char in s2:
    if char in chars:
      chars[char] -= 1

  return True if chars.values() == 0 else False #wrong

def anagrams(s1, s2):

  if len(s1) != len(s2):
    return False
    
  chars = {}

  for char in s1:
    chars[char] = chars.get(char, 0) + 1

  for char in s2:
    if char not in chars:
      return False
    chars[char] -= 1
    if chars[char] < 0:
      return False
  return True
    
  #time: O(n + m)
  #space: O(n + m)

  def most_frequent_char(s):
  #receive a string of lowercasea chars
  #return most seen chars
  #ex: 'hello' => 'l'

  #iterate through the string
  #keep count of how many letters seen
  #iterate through object to find most seen chars

  count = 0
  letter= ''
  chars = {}

  for char in s:
    chars[char] = chars.get(char, 0) + 1

  for key in chars:
    if chars[key] > count:
      count = chars[key]
      letter = key
  return letter


def pair_sum(numbers, target_sum):
  #receive a list of integers and atarget integers
  #return the index of first two indices found

  #ex: [0, 1,2] , 2 => (0, 2)

  #iterate through numbers in range:
  #iterate thorugh numbers in range 
  #check if they add up to target
  #return indices

  # for i in range(len(numbers) - 1):
  #   for j in range(i + 1, len(numbers)):
  #     if numbers[i] + numbers[j] == target_sum:
  #       return (i, j)
  # return (-1, -1)

  #time: O(n ^ 2)
 #space: O(n)

  #keep track of the index found at the element

  integers_map = {}

  for num in range(len(numbers)):
    difference = target_sum - numbers[num]
    # print(difference) #5
    
    if difference in integers_map:
      # print(difference, num) #{3: 0}
      return (integers_map[difference], num) 
      
    integers_map[numbers[num]] = num
    # print(integers_map)
  return (-1, -1)
    

  def pair_product(numbers, target_product):
  # for i in range(len(numbers) -1):
  #   for j in range(i + 1, len(numbers)):
  #     if numbers[i] * numbers[j] == target_product:
  #       return (i, j)
  # return (-1, -1)

  #time:O(n ^2)
  #space:O(n^2)

  count = {}

  for i in range(len(numbers)):
    difference = target_product //  numbers[i]

    if difference in count:
      return (i, count[difference])

    count[numbers[i]] = i
  return (-1, -1)

  
  def intersection(a, b):
  #receive two list of integers
  #return a list of matching elements from other list
  #ex: [0,2,3], [3, 5, 6] => [3]

  #sort both lists and check from beginning and add it to the output

  sorted(a)
  sorted(b)
  output = []
  j = 0

  for num in range(len(a)):
    if a[num] == b[j]:
      output.append(num[a])
      j += 1
      
  return output #wrong

def intersection(a, b):
  #receive two lists of arguments
  #return a list of matching pairs

  #create a set of list in a
  #iteratethrough b

  unique_a = set(a)
  result = []

  for num in b:
    if num in unique_a:
      result.append(num)
  return result

def all_unique(items):
  #receive a list of items
  #return True if all unique, else False
  #ex: ['h','q','r'] => True

  #check in set
  unique_items = set(items)

  # if len(unique_items) != len(items):
  #   return False
  # else:
  #   return True

  return len(unique_items) == len(items)

  # for item in items:
  #   if item in unique_items:
  #     return False
  # return True

  # #time: O(n)
  # #space:O(n)

  def intersection_with_dupes(a, b):
  #receive a list of lowercase chars
  #return a list of matching letters
  #ex: ['h','i'], ['i', 'i','j'] => ['i']

  #iterate through each char, add up to the count
  #then iterate through the second list
  #grab the letter add to the list
  #return the letter

  chars = {}
  result = []

  for char in a:
    if char not in chars:
      chars[char] = 1
    else:
      chars[char] += 1

  for char in b:
    if char in chars and chars[char] > 0:
      result.append(char)
      chars[char] -= 1
  
  return result

def countdown(n):
  if n == 0:
    return
  print(n)
  countdown(n - 1)

def factorial(n):
  #receive an integer
  #return the product from integers
  #ex: 4 => 4 * 3 * 2 * 1 => 24

  #base case: if n == 1: return total
  #recursive case: call n until it's 1

  total = 0

  if n == 1:
    return total
  total *= factorial(n - 1)

  def sum_of_lengths(strings):
  #receive a list of strings
  #return the total sum of all lengths 
  #ex: 

  #add to the total
  if len(strings) == 0:
    return 0

  return len(strings[0]) + sum_of_lengths(strings[1:])


def sum_numbers_recursive(numbers):
  #receive a list of integers
  #return a sum of all integers
  #ex: [4, 3, 2] => 4 + 3 + 2 => 9

  #slice out the first number and add it to the previous call

  if len(numbers) == 0:
    return 0

  return numbers[0] + sum_numbers_recursive(numbers[1:])

def factorial(n):
  #receive an integer
  #return a product of multiple integers
  #ex: 4 *  3 * 2* 1 => 24

  #if n == 0 : return 1
  #factorial of O == 1

  #return n * previous call

  if n == 0:
    return 1

  return n * factorial(n - 1)
  
  def reverse_string(s):
  #receive a string of lowercase chars
  #return the words reversed
  #ex: 'hello' => 'olleh'

  #if the string's length is 0: return ""
  #take the last letter, add to the string, 


  if len(s) == 0:
    return ""
  return reverse_string(s[1:]) + s[0]


def palindrome(s):
  #receive a string of lowercase letters
  #return a boolean if it is True or False if palinddrome 
  #ex: 'hello' => make a reversed 'olleh' => False

  #create a reversed palindrome
  #check if s == reversed palindrome
  
  return reverse_string(s) == s

def reverse_string(s):
  if s == "":
    return ""
  return reverse_string(s[1:]) + s[0]

def palindrome(s):
  if len(s) <= 1:
    return True

  if s[0] != s[-1]:
    return False

  return palindrome(s[1:-1])
  

  def fibonacci(n):
  #receive an integer
  #return the nth number for fibonacci

  #ex: 3 => 0, 1, 1, 2 => 3

  if n == 1:
    return 1

  if n == 0:
    return 0

  return fibonacci(n - 1) + fibonacci(n-2)


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node('A')
b = Node('B')
c = Node('C')


a.next = b
b.next = c

def print_list(head):
  current = head
  while current is not None:
    print(current.val)
    current = current.next
print_list(a)

  if head is None:
    return 
  print(head.val)
  return print_list(head.next)
print_list(a)

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  #receive a head of linked_list_values
  #return a list of all linked_list_values

  #ex: a -> b -> c => [a, b, c]

  #initialize an empty list
  #iterate through head as current until null
  #add each value into list

  result = []

  current = head
  while current:
    result.append(current.val)
    current = current.next
  return result

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_values(head):
  #receive a head of linked_list_values
  #return a list of all linked_list_values

  #ex: a -> b -> c => [a, b, c]

  #initialize an empty list
  #iterate through head as current until null
  #add each value into list

  # result = []

  # current = head
  # while current:
  #   result.append(current.val)
  #   current = current.next
  # return result

  #recursive:
  #if head is empty, return empty list
  #iterate through head.next and add head's value into list
  result = []
  fill_values(head, result)
  return result

def fill_values(head, result):
  if head is None:
    return
  result.append(head.val)
  fill_values(head.next, result)

  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
  #receive a head of ll
  #return total of all values
  #ex: 4 -> 4  -> 3 => 4 + 4 + 3=> 11

  #intialize a total for integer
  #iterate through while it's None
  #add each values
  #return total

  # total = 0
  # current = head
  # while current:
  #   total += current.val
  #   current = current.next

  # return total

  #time: O(n); space= O(1)

  #recursive
  #base case: if head is None: return 0
  #iterate through next value and add to total

  if head is None:
    return 0
  return head.val + sum_list(head.next)

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_find(head, target):
  #receive a head node and a target value,
  #return boolean 
  #ex: a-> b -> c, 'f' => False

  # current = head
  # while current:
  #   if current.val == target:
  #     return True
  #   current = current.next
  # return False

  #time: O(n); space: O(1)
  #recursive:

  if head is None:
    return False

  if head.val == target:
    return True
  return linked_list_find(head.next, target)
  

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
  #receive a head of LL, and an index num
  #return the value found at position
  #ex: a -> b -> c => 1 => 'b'

  #iterate while current is not null
  #decrement index
  #if index is 0
  #return the val
  #else return None

  # current = head
  # while current:
  #   if index == 0:
  #     return current.val
  #   index -= 1
  #   current = current.next
  # return None

  #recursive: 
  #base case if head is empty, return None
  #iterate through and decrement count

  if head is None:
    return None
  
  if index == 0:
    return head.val
  return get_node_value(head.next, index - 1)

  
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head, prev = None):
  #receive the head of LL
  #return a reversed linked reverse_list
  #ex: a -> b -> c => c -> b -> a

  #start at the head
  #capture the next node 
  #point it to prev
  #move current pointer up to next
  #move prev to current
  #return prev

  # current = head
  # prev = None

  # while current: 
  #   next = current.next
  #   current.next = prev
  #   prev = current
  #   current = next
  # return prev

  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)
  
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):
  #receive two heads of ll
  #return one linkedlist with alternating nodes

  #add it the first list; if even , add form second list; if odd, add from first list

  count = 0

  current1 = head_1.next
  current2 = head_2
  tail = head_1

  while current1 and current2:
    if count % 2 == 0:
      tail.next = current2
      current2 = current2.next
    else:
      tail.next = current1
      current1 = current1.next
    tail = tail.next
    count += 1

  if current1:
    tail.next = current1
  else:
    tail.next = current2

  return head_1


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
  #receive two head of a linked merge_lists
  #return one linked list where it's sorted


  #ex: 

  #create a dummy Node
  #iterate through head 1 and head 2
  #compare values
  #if extra, return head 1
  #exlse, return head 2


  dummy = Node(None);
  tail = dummy
  current1 = head_1
  current2 = head_2

  while current1 and current2:
    if current1.val < current2.val:
      tail.next = current1;
      current1 = current1.next
    else:
      tail.next = current2;
      current2 = current2.next
    tail = tail.next

  if current1:
    tail.next = current1

  if current2:
    tail.next = current2

  return dummy.next


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):
  #receive the head of a linkedlist
  #return True if all one value else False
  #ex: 4 -> 4 -> 3 -> null ; False

  #iterate through each node and check if the node is same as head's val
  #if not, return False
  #else return True

  current = head
  while current:
    if current.val != head.val:
      return False
    current = current.next
  return True

 if head is None:
    return True

  if prev_val is not None and head.val != prev_val:
    return False

  return is_univalue_list(head.next, head.val)
    

    # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
  #receive the head of linkedlist
  #return the streak of longest same num together
  #ex: 4 -> 4 -> 3 -> 3 -> 3 -> null => 3

  #keep count
  #keep track of val seen
  #iterate through each Node
  #check if same node's seen
  #increment count

  max_count = 0
  prev_val = None
  current = head
  count = 0
  
  while current:
    
    if current.val == prev_val:
      count += 1
      node_val= current.val
     
    else:
      count = 1
      
    prev_val = current.val

    if count > max_count:
      max_count = count
    
    current = current.next
   
  return max_count
      

  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def remove_node(head, target_val):
  #receive a head of a LL
  #return the linkedlist remove_node
  #ex: 

  #iterate until target_val has been found
  #point to tnext the node after iterate

  if head.val == target_val:
    return head.next

  current = head
  prev = None
  
  while current:
    if current.val == target_val:
      prev.next = current.next
      break

    prev = current
    current = current.next
  return head

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):
  #receive a head of LL
  #return True if it's all same value 
  #else: return False

  #ex: 2 -> 3 -> 3 => False

  #iterate through each node until null
  #check if value is the same as previous
  #if not, return False
  #else, we traverse through everything
  #return True

  current = head
  
  while current is not None:
    if current.val != head.val:
      return False
    current = current.next
  return True


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):
  #receive head of a LL
  #return length of longest matching Node
  #ex: 3 -> 3 -> 3 -> 2 -> null => (3) b/c of 3s

  #keep track of longest length we've seen
  #iterate through head
  #check if prev val is same current's val
  #increment count
  #else reset count
  #if count > maxcount, update max count with current count
  #move to next Node
  #return maxcount

  max_count = 0
  count = 0
  prev = None

  current = head
 
  while current:
    if current.val == prev:
      count += 1
    else:
      count = 1

    prev = current.val

    if count > max_count:
      max_count = count

    current = current.next

  return max_count

      
      # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def remove_node(head, target_val):
  #receive a head a of LL, and target val to remove_node
  #return the ll back where target_val is remove_node
  #ex: 2 -> 3 -> 4, 3 => 2 -> 4 

  #initialize current to head
  #intialize a prev

  #edge case if head is target_val:
  #return head.next afterwards

  #iterate through until target_val is found
  #then point to the next next node after
  #return head

  if head.val == target_val:
    return head.next

  current = head
  prev = None

  while current:
    if current.val == target_val:
      prev.next = current.next
      break
    prev = current
    current = current.next
    
  return head


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  #receive head of a ll
  #return a ll where value has been added
  #ex: 4 -> 3 -> 2; 1, 0 => 1 -> 4 -> 3 -> 2

  #if its the head, add value first and link it to the next of head

  #iterate until index is 0
  #current.val = value
  #otherwise decrement index 
  #return head

  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head

  current = head
  count = 0

  while current:
    if count == index- 1:
      temp = current.next
      current.next = Node(value)
      current.next.next = temp
    count += 1
    current = current.next
  return head


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  #dfs = stack 
  #receive root Node
  #return a stack of dfs list

  #intitalize an empty list
  #start stack with root Node
  #iterate until stack is empty
  #if left node, add left node
  #repeat for right
  ##return list

  if not root:
    return []

  stack = [ root ]
  result = []

  while stack:
    current = stack.pop()
    result.append(current.val)

    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)
  return result

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  #dfs = stack 
  #receive root Node
  #return a stack of dfs list

  #intitalize an empty list
  #start stack with root Node
  #iterate until stack is empty
  #if left node, add left node
  #repeat for right
  ##return list

  if not root:
    return []

  left_values = depth_first_values(root.left)
  right_values = depth_first_values(root.right)
  return [root.val, *left_values, *right_values]


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def breadth_first_values(root):
  #receive root Node
  #return bfs breadth_first_values

  #ex: 

  #import deque
  #iterate while left node, add left
  #same for right node
  #return list

  if not root:
    return []

  result = []

  queue = deque([root])

  while queue:
    current = queue.popleft()
    result.append(current.val)

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return result
    
  
  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
  #receive root node, target value
  #return boolean, True if right value, else False

  #ex: 

  #search through dfs

  if not root:
    return False

  if root.val == target:
    return True

  return tree_includes(root.left, target) or tree_includes(root.right, target)

  # stack = [ root ]

  # while stack:
  #   current = stack.pop()
  #   if current.val == target:
  #     return True
  #   if current.left:
  #     stack.append(current.left)
  #   if current.right:
  #     stack.append(current.right)
  # return False


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  #receive root node 
  #return min value seen 
  #ex: 

  #initialize a min set to infinity
  #iterate through tree-tree_min_value left and right to find smallest value

  if not root:
    return float('inf')

  left_val = tree_min_value(root.left) 
  right_val = tree_min_value(root.right)
 

  return min(root.val, left_val, right_val)

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):
  #receive root Node
  #return max sum seen

  #dfs

  #initialize a total
  #iterate through left
  #iterate through right

  #if no children, then return sum
  #if no left or right, then return sum

  if not root:
    return float("-inf")

  if not root.left and not root.right:
    return root.val

  left_total = max_path_sum(root.left)
  right_total = max_path_sum(root.right)

  return root.val + max(left_total, right_total)

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  if not root:
    return []

  left_vals = depth_first_values(root.left)
  right_vals = depth_first_values(root.right)
  return [root.val, *left_vals, *right_vals]

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  #receive root node of tree
  #return total sum of tree nodes
  #ex: 

  #initialize a sum 
  #if not root return 0

  ##iterate through left and iterate through right to add values

  if not root:
    return 0

  left_vals = tree_sum(root.left)
  right_vals = tree_sum(root.right)

  return root.val + left_vals + right_vals

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
  #receive a root Node
  #return boolean if root node exists in tree_includes

  #ex: 

  if not root:
    return False

  if root.val == target:
    return True

  return tree_includes(root.left, target) or tree_includes(root.right, target)


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  #receive root node of a tree_min_value
  #return smallest value seen 

  #ex: 

  if not root:
    return float('inf')

  min_left = tree_min_value(root.left)
  min_right = tree_min_value(root.right)

  return min(root.val, min_left, min_right)


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):
  #receive root Node
  #return max total 

  #ex: 

  if not root:
    return float("-inf")

  if not root.left and not root.right:
    return root.val
  
  return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def path_finder(root, target):
  #receive a root Node
  #return a list back of root nodes in a list

  #ex: 

  #base case: if root == target, return [root]
  #iteratively
  #keep iterating until node is found
  #add the node into the list:

  if not root:
    return None

  if root.val == target:
    return [root.val]

  left_vals = path_finder(root.left, target)

  if left_vals is not None: 
    return [ root.val, *left_vals]
    
  right_vals = path_finder(root.right, target)
  if right_vals is not None:
    return [root.val, *right_vals]
  
  return None


  # stack = [ root ]
  # result = []

  # while stack:
  #   current = stack.pop()
  #   result.append(current.val)
    
  #   if current.val == target:
  #     return result

  #   if current.right:
  #     stack.append(current.right)
  #   if current.left:
  #     stack.append(current.left)
  # return result
    

    # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_value_count(root, target):
  #receive the root node of a tree, and a target tree_value_count
  #return count of target's value in tree 

  #ex: 

  if not root:
    return 0

  match = 1 if root.val == target else 0
  return match + tree_value_count(root.left, target) + tree_value_count(root.right, target)

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def path_finder(root, target):
  #receive a root of a binary tree
  #return find the path of a target's value

  #ex: 

  #base case: if no root, return None
  #if root == target, return [ root ]
  #itereate through left values
  #iterate through right values

  
  if not root:
    return None

  if root.val == target:
    return [ root.val ]

  left_vals = path_finder(root.left, target)
  if left_vals is not None:
    return [root.val, *left_vals]
    
  right_vals = path_finder(root.right, target)
  if right_vals is not None:
    return [root.val, *right_vals]
  return None
  

  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_value_count(root, target):
  #receive the root of a tree, and a target tree_value_count
  #return count of how many times the value occurred

  if not root:
    return 0

  count = 1 if root.val == target else 0
  return count + tree_value_count(root.left, target) + tree_value_count(root.right, target)

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def how_high(root):
  #receive a root node of a binary tree
  #return the levels

  #ex: 

  #bfs: 
  #iterate through each node
  #increment count of level 
  #return levels

  if not root:
    return -1

  levels = -1
  queue = deque([root])

  while queue:
    level_size = len(queue)
    levels += 1
    for node in range(level_size):
      current = queue.popleft()

      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
  return levels

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def how_high(root):

  if not root:
    return -1
  left_size = how_high(root.left)
  right_size = how_high(root.right)
  return 1 + max(left_size, right_size)



# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def bottom_right_value(root):
  #receive the root node of a tree
  #return the bottom right bottom_right_value

  #ex: 

  #if not root, return -1

  # if not root:
  #   return -1

  # right_val = bottom_right_value(root.right)
  # return right_val

  queue = deque([root])
  while queue:
    current = queue.popleft()

    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
  return current.val
    

  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_value_count(root, target):
  #receive the root node and a target node
  #return the count of occurence of target's node
  #ex: 

  #if root.val == target, increment count
  #iterate through left and iterate through right

  if not root:
    return 0

  count = 1 if root.val == target else 0

  left_seen = tree_value_count(root.left, target)
  right_seen = tree_value_count(root.right, target)

  return count + left_seen + right_seen

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def how_high(root):
  if not root:
    return -1

  return 1 + max(how_high(root.left), how_high(root.right))

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def bottom_right_value(root):
  queue = deque([root])

  while queue:
    current = queue.popleft()

    if current.left:
      queue.append(current.left)

    if current.right:
      queue.append(current.right)
  return current.val

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  paths = _all_tree_paths(root)
  for path in paths:
    path.reverse()
  return paths

def _all_tree_paths(root):
  #receive the root node of a all_tree_paths
  #return all paths from it in a 2D list

  #ex: 

  #initalize an empty list
  #iterate through left, add in root val
  #iterate through right, add in root val
  #

  if not root:
    return []

  if not root.left and not root.right:
    return [ [root. val] ]

  all_paths = []

  left_paths = all_tree_paths(root.left)
  for path in left_paths:
    path.append(root.val)
    all_paths.append(path)

  right_paths = all_tree_paths(root.right)
  for path in right_paths:
    path.append(root.val)
    all_paths.append(path)
      
  return all_paths
    
    # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


from collections import deque

def tree_levels(root):
  #receive the root node of a tree_levels
  #return nodes level by level via bfs

  #ex: 

  #for each node popped off, add them tot he result, then add result to the paths

  if not root:
    return [ ]

  result = []

  queue = deque([root])
  while queue:
    
    levels = len(queue)
    current_level = []
    
    for node in range(levels):
      current = queue.popleft()
      current_level.append(current.val)
    
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)

    result.append(current_level)

  return result
    

    # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def level_averages(root):
  #receive the root node 
  #return a list of averages by level_averages
  #ex: 

  if not root:
    return []

  queue = deque([root])
  result = [ ]
  total = 0
  while queue: 
    levels = len(queue)
    current_level = []
    
    for current in range(levels):
      current = queue.popleft() 
      current_level.append(current.val)
      total = sum(current_level)/len(current_level)

      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
        
    result.append(total)
  return result
      

  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  paths = _all_tree_paths(root)
  for path in paths:
    path.reverse()
  return paths

def _all_tree_paths(root):
  #receive the root node of a all_tree_paths
  #return all paths connected in None
  #ex: 

  if not root:
    return []

  if not root.left and not root.right:
    return [ [ root.val] ]

  all_paths = []
  left_subpaths = _all_tree_paths(root.left)
  for path in left_subpaths:
    path.append(root.val)
    all_paths.append(path)

  right_subpaths = _all_tree_paths(root.right)
  for path in right_subpaths:
    path.append(root.val)
    all_paths.append(path)
  return all_paths

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def tree_levels(root):

  if not root:
    return []
    
  queue = deque([root])
  result = []
  
  while queue:
    levels  = len(queue)
    nodes_level = []
    
    for node in range(levels):
      current = queue.popleft()
      nodes_level.append(current.val)

      if current.left:
        queue.append(current.left)

      if current.right:
        queue.append(current.right)
        
    result.append(nodes_level)
  return result

def is_palindrome(s):
  #receive a string of lowercase chars
  #return a boolean if it is a palindrome, else False
  #ex: 'yo' => 'oy' => False

  #reverse the words and check to see if they are the is_palindrome

  # return s == s[::-1]

  #two pointers with a while loop
  #one starts at beginning, and the other starts at last one
  #check to see if they are same letter

  i = 0
  j = len(s) - 1

  while i < j:
    if s[i] != s[j]:
      return False
    i += 1
    j-=1
  return True

def uncompress(s):
  #receive a case of lower strings
  #return the uncompress version
  #ex: '4a2b' => 'aaaabb'

  #keep a pointerfirst number nad a letter
  #return a string added

  result = ''
  i =0
  j = 0
  numbers = '0123456789'

  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      num = int(s[i:j])
      result += s[j] * num
      j += 1
      i = j
  return result
    
    def uncompress(s):
  #receive a case of lower strings
  #return the uncompress version
  #ex: '4a2b' => 'aaaabb'

  #keep a pointerfirst number nad a letter
  #return a string added

  result = []
  i =0
  j = 0
  numbers = '0123456789'

  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:
      num = int(s[i:j])
      result.append(s[j] * num)
      j += 1
      i = j
  return ''.join(result)

def compress(s):
  #receive a string of lowercase chars
  #return a compressed version
  #ex: 

  #keep count of how many letters seen
  #j will keep going and you will keep comparing to the value of what i has
  #then add the count + letter to the string out put

  s += '!'

  result = []
  i = 0
  j = 0
  
  while j < len(s):
    if s[i] == s[j]:
      j += 1
    else:
      count = j - i

      if count > 1:
        result.append(f"{str(count)}{s[i]}")
      else:
        result.append(s[i])
      i = j
      
  return ''.join(result)
      
    def five_sort(nums):
  #receive a list of integers
  #return lists back where all 5's go to the end

  #i = 0
  #j = last one
  #while they do not pass each other
  #check if i == 5
  #swap them
  #return list back


  i = 0
  j = len(nums) - 1

  while i <= j:
    if nums[j] == 5:
      j -=1
    elif nums[i] == 5:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
    else:
      i += 1
  return nums
  
  
    def largest_component(graph):
  #receive a graph
  #return size of largest_component

  #ex: 

  #itereate through each node in graph:
  #check size 
  #return largest size found

  largest = 0
  visited = set()

  for node in graph:
    size = explore(graph, node, visited)
    if size > largest:
      largest = size
  return largest

def explore(graph, node, visited):
  if node in visited:
    return 0

  visited.add(node)

  size = 1
  for neighbor in graph[node]:
    size += explore(graph, neighbor, visited)
  return size
    
    from collections import deque

def shortest_path(edges, node_A, node_B):
  #receive an edges
  #return shortest path to from a to b
  #ex: 

  #do it via bfs using a queue
  #modify edges into graph 


  graph = build_graph(edges)
  visited = set([node_A])
  queue = deque( [(node_A, 0 )] )

  while queue:
    current, dist = queue.popleft()

    if current == node_B:
      return dist

    for neighbor in graph[current]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, dist + 1))
    
  return -1
  

def build_graph(edges):
  graph = {}

  for a,b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph 
  
  def island_count(grid):
  #receive a m x n grid
  #return count of islands by L

  #ex: 

  #iterate through rows and cols
  #check if it is a L
  #then traverse and mark it as seen
  #return count

  size = 0
  visited = set()

  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if dfs(grid, row, col, visited) == True:
        size += 1
  return size

def dfs(grid, row, col, visited):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 'W' or (row, col) in visited:
    return False

  visited.add((row, col))

  dfs(grid, row +1, col, visited)
  dfs(grid, row -1, col, visited)
  dfs(grid, row, col +1, visited)
  dfs(grid, row, col -1, visited)
  return True

def minimum_island(grid):
  #receive a m x n grid
  #return smallest size seen
  #ex: 

  smallest = float('inf')
  visited = set()

  for row in range(len(grid)):
    for col in range(len(grid[0])):
      size = dfs(grid, row, col, visited)
      if size < smallest and size > 0:
        smallest = size
  return smallest


def dfs(grid, row, col, visited):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in visited or grid[row][col] == 'W':
    return 0

  visited.add((row, col))
  
  size = 1

  size += dfs(grid, row -1, col, visited)
  size += dfs(grid, row + 1, col, visited)
  size += dfs(grid, row, col - 1, visited)
  size += dfs(grid, row, col + 1, visited)
  return size

  
from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  #receive a grid and coordinates
  #return bfs

  #ex: 

  #throw them into a set of visited for r and c
  #put them into a queue with dist 
  #iterate through all directions
  #if any of them reaches a 'C', return the dist

  visited = set([ (starting_row, starting_col )])
  queue = deque([ (starting_row, starting_col, 0)])

  directions = [(0,1), (1,0), (-1,0), (0, -1)]

  while queue:
    r, c, dist = queue.popleft()

    if grid[r][c] == 'C':
      return dist

    for dr, dc in directions:
      nr, nc = dr+ r, dc + c

      row_bounds = 0 <= nr < len(grid)
      col_bounds = 0 <= nc < len(grid[0])

      if row_bounds and col_bounds and grid[nr][nc] != 'X' and (nr, nc) not in visited:
        visited.add((nr, nc))
        queue.append((nr, nc, dist + 1))
  return -1

    def tribonacci(n):
  return _tribonacci(n, {})
  #receive an integer
  #return the sum of tribonacci
  #ex: 

  #base cases: if n == 0 or n ==1, return n 
  

def _tribonacci(n, memo):

  if n in memo:
    return memo[n]
    
  if n == 0 or n == 1:
    return 0

  if n == 2:
    return 1

  memo[n] = _tribonacci(n- 1, memo) + _tribonacci(n- 2, memo) + _tribonacci(n - 3, memo)
  return memo[n]

def minimum_island(grid):
  #receive a grid of m x n
  #return size of smallest minimum_island
  #ex: 

  #iterate through each row and col
  #check if size is smaller than what we currently have
  #update smallest

  smallest = float('inf')
  visited = set()

  for row in range(len(grid)):
    for col in range(len(grid[0])):
      size = dfs(grid, row, col, visited)
      if size < smallest and size > 0:
        smallest = size
  return smallest

def dfs(grid, row, col, visited):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 'W':
    return 0
  
  pos = (row, col)
  if pos in visited:
    return 0

  visited.add(pos)

  size = 1

  size += dfs(grid, row + 1, col, visited)
  size += dfs(grid, row - 1, col, visited)
  size += dfs(grid, row, col + 1, visited)
  size += dfs(grid, row, col - 1, visited)
  return size


from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  #receive a grid , starting position
  #return the amount of steps taken to reach closest_carrot
  #ex: 

  #using bfs
  #iterate through

  visited = set([(starting_row, starting_col)])
  queue = deque([(starting_row, starting_col, 0)])

  directions = [(1,0), (0, 1), (-1,0), (0, -1)]

  while queue:
    row, col, dist = queue.popleft()

    if grid[row][col] == 'C':
      return dist

    for dr, dc, in directions:
      nr, nc = dr + row, dc + col

      row_inbounds = 0 <= nr < len(grid)
      col_inbounds = 0 <= nc < len(grid[0])
      pos = (nr, nc)

      if row_inbounds and col_inbounds and pos not in visited and grid[nr][nc] != 'X':
        visited.add(pos)
        queue.append((nr, nc, dist + 1))
  return -1

from collections import deque

def best_bridge(grid):
  main_island = None
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      potential_island = traverse_island(grid, row, col, set())
      if len(potential_island) > 0:
        main_island = potential_island

  visited = set(main_island)
  queue = deque([])
  for pos in main_island:
    r,c = pos
    queue.append((r, c, 0))

  while queue:
    r,c, dist = queue.popleft()
    if grid[r][c] == "L" and (r,c) not in main_island:
      return dist -1 

    directions = [(1,0), (-1,0), (0,1), (0, -1)]

    for dr,dc in directions: 
      nr,nc = dr+ r, dc + c
      if is_inbounds(grid, nr, nc) and (nr, nc) not in visited:
        visited.add((nr,nc))
        queue.append((nr, nc, dist + 1))
      
      

def is_inbounds(grid, row, col):
  row_inbounds = 0 <= row < len(grid)
  col_inbounds = 0 <= col < len(grid[0])
  return row_inbounds and col_inbounds
      
def traverse_island(grid, row, col, visited):

  if not is_inbounds(grid, row, col) or grid[row][col] == 'W':
    return visited
    
  pos = (row, col)
  if pos in visited:
    return visited
    
  visited.add(pos)

  traverse_island(grid, row - 1, col, visited)
  traverse_island(grid, row + 1, col, visited)
  traverse_island(grid, row, col - 1, visited)
  traverse_island(grid, row, col + 1, visited)
  return visited

  class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #receive a m x n grid
        #return the count (int) of the path a robot can take going down and right only

        #ex: 
        # [[X, 0,0],
        #  [0, 0,0,]
        #  [0, 1, 0]]
        
        #if it is marked as 1, do not go in that area
        #if the area is marked as 0, we can go ahead and mark it

        #keep track of path
        #iterate through the rows and cols
        #check to see if it is marked as 0,
        #perform a dfs, go right, and bottom
        #mark as a path and return true, increment path count
        #return the path

        path = 0

        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                path = self.dfs(obstacleGrid, row, col)
        return path

    def dfs(self, obstacleGrid, row, col):
        if row < 0 or row >= len(obstacleGrid) or col < 0 or col >= len(obstacleGrid[0]) or obstacleGrid[row][col] == 1:
            return 0

        if obstacleGrid[row-1][col-1] == 1:
            return 1
            
        path = 1 

        path += self.dfs(obstacleGrid, row +1 , col)
        path += self.dfs(obstacleGrid, row, col + 1)

        return path

        #ex: 
        # [[X, 0,0],
        #  [0, 0,1,]
        #  [0, 1, 0]]
        
  class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #receive a m x n grid
        #return the count (int) of the path a robot can take going down and right only

        #ex: 
        # [[X, 0,0],
        #  [0, 0,0,]
        #  [0, 1, 0]]
        
        #if it is marked as 1, do not go in that area
        #if the area is marked as 0, we can go ahead and mark it

        #keep track of path
        #iterate through the rows and cols
        #check to see if it is marked as 0,
        #perform a dfs, go right, and bottom
        #mark as a path and return true, increment path count
        #return the path

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            
            if obstacleGrid[r][c] == 1:
                return 0
            
            if r == rows-1 and c == cols-1:
                return 1

            return dfs(r + 1, c) + dfs(r, c + 1)

        return dfs(0, 0)
        

   from collections import deque

def best_bridge(grid):
  #receive a m x n grid
  #return the min steps needed to cross from one land to another land
  #ex: 

  #iterate through to get all of the islands
  #then iterate via bfs to get dist
  #return dist

  for row in range(len(grid)):
    for col in range(len(grid[0])):
      potential_island = dfs(grid, row, col, set())
      if len(potential_island) > 0:
        main_island = potential_island

  
  while queue:
    

def is_inbound(grid, row, col):
  row_inbounds = 0 < row <= len(grid)
  col_inbounds = 0 < col <= len(grid[0])
  return row_inbounds and col_inbounds

def dfs(grid, row, col, visited):
  if not is_inbound(grid, row, col) or grid[row][col] == "W":
    return visited

  pos = (row,col)
  if pos in visited:
    return visited

  visited.add(pos)

  dfs(grid, row - 1, col, visited)
  dfs(grid, row + 1, col, visited)
  dfs(grid, row, col-1, visited)
  dfs(grid, row, col+1, visited)
  return visited

  from collections import deque

def best_bridge(grid):
  #receive a m x n grid
  #return count of distance
  #ex: 

  #achieve all of the islands
  #iterate through the islands and do a bfs to check which one is closest


  for row in range(len(grid)):
    for col in range(len(grid[0])):
      potential_island = explore(grid, row, col, set())
      if len(potential_island) > 0:
        main_island = potential_island

  visited = set(main_island)
  queue = deque([ ])
  for pos in main_island:
    r, c = pos
    queue.append((r, c, 0))

  while queue:
    row, col, distance = queue.popleft()
    if grid[row][col] == "L" and (row, col) not in main_island:
      return distance - 1

    directions = [(0,1), (1,0), (-1,0), (0, -1)]

    for dr, dc in directions:
      nr, nc = dr + row, dc + col

      if is_inbounds(grid, nr, nc) and (nr, nc) not in visited:
        visited.add((nr, nc))
        queue.append((nr, nc, distance + 1))
      
  
def is_inbounds(grid, row, col):
  row_inbounds = 0 <= row < len(grid)
  col_inbounds = 0 <= col < len(grid[0])
  return row_inbounds and col_inbounds

def explore(grid, row, col, visited):
  if not is_inbounds(grid, row, col) or grid[row][col] == 'W':
    return visited

  pos = (row, col)
  if pos in visited:
    return visited

  visited.add(pos)

  explore(grid, row + 1, col, visited)
  explore(grid, row - 1, col, visited)
  explore(grid, row, col + 1, visited)
  explore(grid, row, col - 1, visited)
  return visited
  

  def has_cycle(graph):
  #receive an adj matrix
  #return boolean if it is connected

  #ex:

  #iterate through each node and check if it's in the phase of visiting

  visited = set()
  visiting = set()

  for node in graph:
    if cycle_detect(graph, node, visiting, visited) == True:
      return True
  return False

def cycle_detect(graph, node, visiting, visited):
  if node in visited:
    return False

  if node in visiting:
    return True

  visiting.add(node)

  for neighbor in graph[node]:
    if cycle_detect(graph, neighbor, visiting, visited):
      return True
  

  visiting.remove(node)
  visited.add(node)

  return False

def reverse_some_chars(s, chars):
  #receive a string  of lowercase chars, and a list of chars 
  #return the string reversed if the char is in list
  #ex: 'apple', ['a', 'e'] => 'eppla'

  #initialize an empty list
  #iterate through each char to check if it is in chars
  #add it to a separate list (can add to stack)
  #return new string

  stack = []
  result = []

  for char in s:
    if char in chars:
      stack.append(char)
    # print(stack) ['o', 'u', 'e'] 

  for char in s:
    if char in chars:
      result.append(stack.pop())
    else:
      result.append(char)
  print(result)
      
  return ''.join(result)
      

      def reverse_some_chars(s, chars):
  #receive a string  of lowercase chars, and a list of chars 
  #return the string reversed if the char is in list
  #ex: 'apple', ['a', 'e'] => 'eppla'

  #initialize an empty list
  #iterate through each char to check if it is in chars
  #add it to a separate list (can add to stack)
  #iterate through string again and pop off chars off stack if the char belonged in chars
  #return new string

  stack = []
  result = []

  for char in s:
    if char in chars:
      stack.append(char)
    # print(stack) ['o', 'u', 'e'] 

  for char in s:
    if char in chars:
      result.append(stack.pop())
    else:
      result.append(char)
  print(result)
      
  return ''.join(result)
    
    def prereqs_possible(num_courses, prereqs):
  graph = build_graph(num_courses, prereqs)

  visiting = set()
  visited = set()

  for node in graph:
    if has_cycle(graph, node, visited, visiting):
      return False
  return True

def has_cycle(graph, node, visited, visiting):
  if node in visited:
    return False

  if node in visiting:
    return True

  visiting.add(node)

  for neighbor in graph[node]:
    if has_cycle(graph, neighbor, visited, visiting) #node is connected to neighbor
    return True

  visiting.remove(node)
  visited.add(node)
  return False

def build_graph(num_courses, prereqs):
  graph = {}

  for i in range(0, num_courses):
    graph[i] = []

    for prereq in prereqs:
      course_a, course_b = prereq
      graph[course_a].append(course_b)

  return graph

  def has_cycle(graph):
  #receive an adj matrix
  #return boolean if has a cycle, else False

  #ex: 

  visiting = set()
  visited = set()

  for node in graph:
    if cycle_detect(graph, node, visiting, visited) == True:
      return True
  return False

def cycle_detect(graph, node, visiting, visited):
  if node in visited:
    return False

  if node in visiting:
    return True

  visiting.add(node)

  for neighbor in graph[node]:
    if cycle_detect(graph, neighbor, visiting, visited) == True:
      return True

  visiting.remove(node)
  visited.add(node)
  return False
  
  
def prereqs_possible(num_courses, prereqs):
  #receive an adj list
  #return True if can take all courses, else false

  #ex:

  #create a graph of num courses and preqs to iterate through
  #check if it's in the visited, return False, else return True

  graph = build_graph(num_courses, prereqs)
  visited = set()
  visiting = set()

  for node in graph:
    if has_cycle(graph, node, visiting, visited): #found acycle so can't get take all courses
      return False
  return True

def has_cycle(graph, node, visiting, visited):
  if node in visited:
    return False
    
  if node in visiting:
    return True

  visiting.add(node)

  for neighbor in graph[node]:
    if has_cycle(graph, neighbor, visiting, visited):
      return True

  visiting.remove(node)
  visited.add(node)
  return False

def build_graph(num_courses, prereqs):
  graph = {}

  for i in range(0, num_courses):
    graph[i]= []

  for prereq in prereqs:
    a,b = prereq
    graph[a].append(b)

  return graph  
  
      
       def sum_possible(amount, numbers):
  return _sum_possible(amount, numbers, {})


def _sum_possible(amount, numbers, memo):
  #receive an int, and a list of integers
  #return boolean

  #ex:

  if amount in memo:
    return memo[amount]

  if amount == 0:
    return True

  if amount < 0:
    return False

  for num in numbers:
    if _sum_possible(amount - num, numbers, memo):
      memo[amount] = True
      return True

    memo[amount] = False

  return False

def min_change(amount, coins):
  ans= _min_change(amount, coins, {})

  return -1 if ans == float('inf') else ans


def _min_change(amount, coins, memo):
  if amount in memo:
    return memo[amount]

  if amount < 0:
    return float("inf")

  if amount == 0:
    return 0

  min_coins = float("inf")
  
  for coin in coins:
    num_coins = 1 + _min_change(amount - coin, coins, memo)
    if num_coins < min_coins:
      min_coins = num_coins

  memo[amount] = min_coins
  return min_coins
      

      def paired_parentheses(string):
  #receive a string of lowercase chars and paired_parentheses
  #return boolean, True if equal amount of closing and opening paired_parentheses
  #ex: '(()' => False

  #initialize a string with paren 
  #iterate through string
  #check if it is a paren 
  #add it to the stack
  #iterate through stack 
  #check if it is an openin 
  #look for closing 
  #else return False
  #else after looking everything, return True 


  parens = '()'
  stack = []

  for char in string:
    if char in parens:
      stack.append(char)

  while len(stack) > 0:
    item = stack.pop()
    if item == '(':
      return False

  return True
      
      
def paired_parentheses(string):
  #receive a string of lowercase chars and paired_parentheses
  #return boolean, True if equal amount of closing and opening paired_parentheses
  #ex: '(()' => False

  #initialize a string with paren 
  #iterate through string
  #check if it is a paren 
  #add it to the stack
  #iterate through stack 
  #check if it is an openin 
  #look for closing 
  #else return False
  #else after looking everything, return True 


  count = 0

  for char in string:
    if char == '(':
      count += 1
    elif char == ')':
      if count == 0:
        return False
      count -= 1

  return count  == 0
      
      
      def count_paths(grid):
  return _count_paths(grid, 0, 0, {})

def _count_paths(grid, r ,c, memo):
  pos = (r,c)
  if pos in memo:
    return memo[pos]
  
  if r == len(grid) or c == len(grid[0]) or grid[r][c] == "X":
    return 0

  if r == len(grid) -1 and c == len(grid[0]) -1:
    return 1

  down_paths = _count_paths(grid, r + 1, c, memo)
  right_paths = _count_paths(grid, r, c + 1, memo)

  memo[pos] = down_paths + right_paths
  return memo[pos]

def max_path_sum(grid):
  return _max_path_sum(grid, 0,0, {})

def _max_path_sum(grid, r, c, memo):
  pos = (r, c)
  if pos in memo:
    return memo[pos]
    
  if r == len(grid) or c == len(grid[0]):
    return float("-inf")

  if r == len(grid) -1  and c == len(grid[0]) -1:
    return grid[r][c]

  down_paths = _max_path_sum(grid, r + 1, c, memo)
  right_paths = _max_path_sum(grid, r, c + 1, memo)
  memo[pos] = grid[r][c] + max(down_paths, right_paths)
  return memo[pos]

def non_adjacent_sum(nums):
  if len(nums) == 0:
    return 0

  include = nums[0] + non_adjacent_sum(nums[2:])
  exclude = non_adjacent_sum(nums[1:])
  return max(include, exclude)

  class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #receive an integer for numcourses, and we have a list for prereqs
        #return a boolean, True if we can take all of the courses, else False
        #ex: 3, prereqs: [[0,1], [1, 2], [2, 3]] =>
        #                  a, b
        #  { [1]: 0, 
        #.  [2], 1,
        #. [3]: 2,
        #} => True


        #numCourses = 2, prerequisites = [[0,1],[1,0]]
        #{ [1]: 0,
        # [0] : 1
        #} => False

        #black-white-grey algo => 2 sets to track which node you've visited

        #build out a graph
        #iterate through the graph and check if there is a cycle
        #if there is, return False
        #else, return True that we can go ahead and finsih all

        visited = set()
        visiting = set()

        graph = build_graph(self, numCourses, prerequisites)
        for node in graph:
            if cycle_detect(graph, node, visiting, visited):
                return False
        return True

def cycle_detect(graph, node, visiting, visited):
    if node in visiting:
        return True

    if node in visited:
        return False
    
    visiting.add(node)

    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited) == True:
            return False
    
    visiting.remove(node)
    visited.add(node)

    return True

def build_graph(self, numCourses: int,prerequisites: List[List[int]]): 
    graph ={}

    for i in range(0, numCourses):
        graph[i] = []

    for a,b in prerequisites:
        graph[a].append(b)

    return graph 

import math

def summing_squares(n):
  return _summing_squares(n, {})

def _summing_squares(n, memo):
  if n== 0:
    return 0

  if n in memo:
    return memo[n]

  min_squares = float('inf')
  
  for i in range(1, math.floor(math.sqrt(n)) + 1):
    square = i * i
    num_squares = 1 + _summing_squares(n - square, memo)
    min_squares = min(min_squares, num_squares)
  memo[n] = min_squares
  return min_squares

def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})


def _counting_change(amount, coins, i, memo):
  key = (amount, i)
  if key in memo:
    return memo[key]
    
  if amount == 0:
    return 1

  if i == len(coins):
    return 0

  coin = coins[i]
  total_ways = 0
  for qty in range(0, (amount // coin) + 1):
    remainder = amount - (qty * coin)
    total_ways += _counting_change(remainder, coins, i + 1, memo)
  memo[key] =total_ways
  return total_ways

  
def array_stepper(numbers):
  return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, i, memo):
  if i in memo:
    return memo[i]
    
  if i >= len(numbers) -1:
    return True

  max_step = numbers[i]
  for step in range(1, max_step + 1):
    if _array_stepper(numbers, i + step, memo):
      memo[i] = True
      return True
  memo[i] = False
  return False
    
def array_stepper(numbers):
  #receive a list of integers
  #return a boolean of true or false
  #ex:
  #iterate starting at the first index
  #base case: if we reached the end of the list, return true
  #iterate through each array_stepper (idx)
  #if we traverse through all and never reached, return false
  return _array_stepper(numbers, 0, {})

def _array_stepper(numbers, idx, memo):
  if idx in memo:
    return memo[idx]
    
  if idx >= len(numbers) - 1:
    return True

  max_step = numbers[idx]
  for step in range(1, max_step + 1):
    if _array_stepper(numbers, step + idx, memo):
      memo[idx] = True
      return True
      
  memo[idx] = False
  return False

def max_palin_subsequence(string):
  return _max_palin_subsequence(string, 0, len(string) - 1,{})

def _max_palin_subsequence(string, i , j, memo):
  key = (i,j)
  if key in memo:
    return memo[key]
  
  if i == j:
    return 1

  if i > j:
    return 0

  if string[i] == string[j]:
    memo[key] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo) #represents length
    #2 to match the current two chars that match
  else:
    memo[key] = max( _max_palin_subsequence(string, i + 1,j, memo),
    _max_palin_subsequence(string, i,j -1, memo))
  return memo[key]

def overlap_subsequence(string_1, string_2):
  return _overlap_subsequence(string_1, string_2, 0, 0, {})

def _overlap_subsequence(string_1, string_2, i, j, memo):
  #base case: if i or j ever reaches end of string, return count
  key = (i, j)
  if key in memo:
    return memo[key]

  if i == len(string_1) or j == len(string_2):
    return 0

  if string_1[i] == string_2[j]:
    memo[key] =  1 + _overlap_subsequence(string_1, string_2, i + 1, j + 1, memo)
  else:
   memo[key] =  max(
      _overlap_subsequence(string_1, string_2, i + 1, j, memo),
      _overlap_subsequence(string_1, string_2, i, j + 1, memo))
  return memo[key]

  
def can_concat(s, words):
  return _can_concat(s, words, {})

def _can_concat(s, words, memo):
  if s in memo:
    return memo[s]
    
  if s == "":
    return True

  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      if _can_concat(suffix, words, memo) == True:
        memo[s] = True
        return True
        
  memo[s] = False
  return False
      
  def can_concat(s, words):
  return _can_concat(s, words, 0, {})

def _can_concat(s, words,i, memo):
  if i in memo:
    return memo[i]
    
  if i == len(s):
    return True

  for word in words:
    if s.startswith(word, i):
      if _can_concat(s, words, i + len(word), memo) == True:
        memo[i] = True
        return True
        
  memo[i] = False
  return False
      

      def quickest_concat(s, words):
  result = _quickest_concat(s, words, {})
  if result == float('inf'):
    return -1
  else:
    return result

def _quickest_concat(s, words, memo):
  if s in memo:
    return memo[s]
  
  if s == "":
    return 0

  min_words = float('inf')
  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      attempt = 1 + _quickest_concat(suffix, words, memo)
      min_words = min(attempt, min_words)
  memo[s] = min_words
  return min_words
      

  def valid_compound(compound, elements):
  return _valid_compound(compound, elements, 0, {})

def _valid_compound(compound, elements, idx, memo):

  if idx in memo:
    return memo[idx]
  if idx == len(compound):
    return True

  for word in elements:
    if compound.startswith(word.lower(), idx):
      if _valid_compound(compound, elements, idx + len(word), memo) == True:
        memo[idx] = True
        return True

  memo[idx] = False
  return False

def count_compounds(compound, elements):
  return _count_compunds(compound, elements, 0, {})

def _count_compunds(compound, elements, idx, memo):

  if idx in memo:
    return memo[idx]
  if idx == len(compound):
    return 1

  count = 0
  for ele in elements:
    if compound.startswith(ele.lower(), idx):
      count += _count_compunds(compound, elements, idx + len(ele), memo)
  memo[idx] = count
  return count

def longest_path(graph):
  distance = {}

  for node in graph:
    if len(graph[node]) == 0:
      distance[node]  = 0

  for node in graph:
    traverse_distance(graph, node, distance)
  return max(distance.values())

def traverse_distance(graph, node, distance):
  if node in distance:
    return distance[node]

  max_length = 0
  for neighbor in graph[node]:
    attempt = traverse_distance(graph, neighbor, distance)
    if attempt > max_length:
      max_length = attempt
  distance[node] = 1 + max_length

  return distance[node]
    

    def semesters_required(num_courses, prereqs):
  #receive a num course, and a prereqs
  #return min number of semesters required to complete all n  num_courses
  #ex: 

  #convert graph into adj matrix
  #check terminal node
  #revert back

  graph = build_graph(num_courses, prereqs)

  distance = {}
  
  for course in graph:
    if len(graph[course]) == 0:
      distance[course] = 1

  for course in graph:
    traverse_graph(graph, course, distance)

  return max(distance.values())

def traverse_graph(graph, course, distance):
  if course in distance:
    return distance[course]

  max_length = 0
  for neighbor in graph[course]:
    attempt = traverse_graph(graph, neighbor, distance)
    if attempt > max_length:
      max_length = attempt

  distance[course] = 1 + max_length
  return distance[course]


def build_graph(num_courses, prereqs):
  graph = {}

  for course in range(0, num_courses):
    graph[course] = [] #keys

  for prereq in prereqs:
    a,b = prereq
    graph[a].append(b)

  return graph

def reverse_some_chars(s, chars):
  #receive a computer and chars list
  #return a list of chars with the chars list reversed
  #ex: 'hello', ['r', 'e', 'o'] => 'holle'

  #iterate through s and add in the char in chars list to a stack
  #iterate through the s again
  #add in the chars from the stack
  #return the result back as a string

  result = []
  stack = []

  for char in s:
    if char in chars:
      stack.append(char)

  for char in s:
    if char in chars:
      result.append(stack.pop())
    else:
      result.append(char)
      
  return ''.join(result)

def paired_parentheses(string):
  #receive a string of paired_parentheses
  #return boolean, True if paired (), else false
  #ex: '(char))'=> false

  #iterate through string
  #check if it is an opening paren, add 1 to count
  #else, it's closing, subtract 1 from count

  #return True if count == 0, else false

  count = 0
  for char in string:
    if char == "(":
      count += 1
    elif char == ')':
      if count == 0:
        return False
      else:
        count -=1

  return count == 0

def befitting_brackets(string):
  #receive a string of brackets 
  #return boolean , True if matching brackets, else False
  #ex: '({}' => False

  brackets = {
    '(': ')',
    '[': ']',
    '{': '}'
  }

  stack = []
  for char in string:
    if char in brackets:
      stack.append(brackets[char])
    else:
      if stack and stack[-1] == char:
        stack.pop()
      else:
        return False
  return len(stack) == 0

def decompress_braces(string):
  #receive a string
  #return the decompressed version

  #ex: '3{ft5{i}}' => 'ftftftiiiiii'

  #use a stack
  #add in stack
  #if it's a closing paren
  #then pop off previous until integer
  #return the string back

  stack = []
  numbers = '123456789'

  for char in string:
    if char in numbers:
      stack.append(int(char))
    else:
      if char == '}':
        segment = ""
        while not isistance(stack[-1], int):
          popped = stack.pop()
          segment = popped + segment
        num = stack.pop()
        stack.append(segement * num)
      elif char != '{':
        stack.append(char)

  return ''.join(stack)
    
def nesting_score(string):
  #receive a string of brackets
  #return total nesting_score
  #ex: [[]] => 2 b/c of 1 * 2


  #use a stack
  #if opening bracket, push a 0 to stack
  #if matching pair, add 1
  #if closing bracket, check last total to see if not zero, then * 2
  #return total

  stack = [0]

  for char in string:
    if char == '[':
      stack.append(0)
    else:
      popped = stack.pop()
      if popped == 0:
        stack[-1] += 1
      else:
        stack[-1] += popped * 2
  return stack[0]

  
  def has_subarray_sum(numbers, target_sum):
  for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers) + 1):
      total = sum(numbers[i:j])
      if total == target_sum:
        return True

  return False


def has_subarray_sum(numbers, target_sum):
  prefix_sums = [0]
  total = 0 
  for num in numbers:
    total += num
    prefix_sums.append(total)

  seen = set()
  for num in prefix_sums:
    difference = num - target_sum
    if difference in seen:
      return True
    seen.add(num)
  return False

from collections import Counter

def subarray_sum_count(numbers, target_sum):
  #receive a list of integers, and a target_sum
  #return the count of subarray_sum_count
  #ex: 

  #iterate through using a prefix sum 
  #

  prefix_sums = [0]
  total = 0
  for num in numbers:
    total += num
    prefix_sums.append(total)

  seen = Counter()
  count = 0
  for num in prefix_sums:
    difference = num - target_sum
    count += seen[difference]
    seen[num] += 1
  return count
      
    from collections import deque

def merge_sort(nums):
  if len(nums) <= 1:
    return nums

  mid = len(nums) //2
  left_list = merge_sort(nums[:mid])
  right_list = merge_sort(nums[mid:])
  return merge(left_list, right_list)


def merge(list1, list2):
  deque1 = deque(list1)
  deque2 = deque(list2)
  merged = []

  while deque1 and deque2:
    if deque1[0] < deque2[0]:
      merged.append(deque1.popleft())
    else:
      merged.append(deque2.popleft())

  merged += deque1
  merged += deque2

  return merged

def combine_intervals(intervals):
  #receive a list of tuple
  #return a list of intervals back 

  #ex: 

  sorted_intervals = sorted(intervals, key=lambda interval:interval[0])

  result = [ sorted_intervals[0]]

  for interval in sorted_intervals[1:]:
    start, end = interval
    last_start, last_end = result[-1]
    if last_end >= start: #check starts
      if end >last_end: #check the end
        result[-1] = (last_start, end)
    else:
      result.append(interval)
  return result
    
    def binary_search(numbers, target):
  left = 0
  right = len(numbers)  - 1
 

  while left <= right:
    mid = (left + right) // 2

    if target < numbers[mid]:
      right = mid -1
    elif numbers[mid] < target:
      left = mid + 1
    else:
      return mid

  return -1

def lexical_order(word_1, word_2, alphabet):
  #receive two string of lowers case chars, and an alphabet
  #return True if word1 < word_2
  #ex: 'app', 'apple' => True


  #iterate through longest string
  #obtain each char in the string as long as they are not out of bounds
  #check the index position of them in alphabet
  #if word_1 char < word_2 char, return True, else return False

  max_length = max(len(word_1), len(word_2))

  for i in range(0, max_length):
    value_1 = alphabet.index(word_1[i]) if i < len(word_1) else float('-inf')
    value_2 = alphabet.index(word_2[i]) if i < len(word_2) else float('-inf')
    if value_1 < value_2:
      return True
    elif value_2 < value_1:
      return False
  return True

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_palindrome(head):
  #receive a head of ll
  #return boolean if linked list is linked_palindrome
  #ex: 

  #intialize an empty list to store
  #iterate through each Node
  #add to the list
  #check if rev list == current list

  result = []
  current = head
  while current:
    result.append(current.val)
    current = current.next

  return result == result[::-1]
    

    # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def middle_value(head):
  #receive a head of LL
  #return middle value of the LL
  #ex: 

  #initialize a result
  #add in all the nodes
  #calc middle
  #return the middle


  result = []
  current = head

  while current:
    result.append(current.val)
    current = current.next

  mid = len(result) // 2

  return result[mid]

    
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def middle_value(head):
  #receive a head of LL
  #return middle value of the LL
  #ex: 

  #initialize a result
  #add in all the nodes
  #calc middle
  #return the middle


  # result = []
  # current = head

  # while current:
  #   result.append(current.val)
  #   current = current.next

  # mid = len(result) // 2

  # return result[mid]

  #using tortoise and hare

  slow = head
  fast = head

  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

  return slow.val

  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_cycle(head):
  #receive a head of ll 
  #return True if cycle exists, else False
  #ex: 

  #using slow and fast
  #if slow and fast meet, return True, else False

  slow = head
  fast = head
  first_iteration = True
  while not (fast is None or fast.next is None):
    if slow is fast and not first_iteration:
      return True
    slow = slow.next
    fast = fast.next.next
    first_iteration = False
  return False


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def undupe_sorted_linked_list(head):
  #receive a head of ll
  #return a new  ll of no duplicates
  #ex: 

  #check next Node to see if same val
  #then point to next next Node
  #return head

  current = head
  dummy = Node(None)
  tail = dummy
  
  while current:
    if current.val != tail.val:
      tail.next = Node(current.val)
      tail = tail.next
    
    current = current.next #update current every single iteration

  return dummy.next
  
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  #receive a list of items
  #return a LL 
  #ex: 

  #iterate through each item
  #create a new node for them
  #add them to the tail
  #return head

  dummy = Node(None)
  tail = dummy

  for item in values:
    current = Node(item)
    tail.next = current
    tail = tail.next

  return dummy.next

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
    
  def enqueue(self, val):
    if self.size == 0:
      self.head = Node(val)
      self.tail = self.head
    else:
      self.tail.next = Node(val)
      self.tail = self.tail.next
    self.size += 1
    
  def dequeue(self):
    if self.size == 0:
      return None
      
    value = self.head.val
    if self.size == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
      
    self.size -= 1
    return value
    
      
  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def flip_tree(root):
  if not root:
    return None

  left_path=flip_tree(root.left)
  right_path=flip_tree(root.right)
  root.left = right_path
  root.right = left_path

  return root


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def lowest_common_ancestor(root, val1, val2):
  #find all the paths
  #find the same node in __init__
  left_path = get_path(root, val1)
  right_path = get_path(root, val2)
  set2 = set(right_path)
  
  for val in left_path:
    if val in set2:
      return val
    

def get_path(root, target_val):
  if root is None:
    return []

  if root.val == target_val:
    return [ root.val ]

  left_path = get_path(root.left, target_val)
  if left_path:
    left_path.append(root.val)
    return left_path


  right_path = get_path(root.right, target_val)
  if right_path:
    right_path.append(root.val)
    return right_path
  return None
    
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def flip_tree(root):
  if not root:
    return None

  left_path = flip_tree(root.left)
  right_path = flip_tree(root.right)
  root.left = right_path
  root.right = left_path
  return root
  

  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def lefty_nodes(root):
  if not root:
    return []

  values = []
  traverse(root, 0, values)
  return values

def traverse(root, level, values):
  if not root:
    return 0

  if len(values) == level:
    values.append(root.val)

  traverse(root.left, level + 1, values)
  traverse(root.right, level + 1, values)

 # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def binary_search_tree_includes(root, target):
  #receive the root node, check if the target node exists
  #return boolean

  #ex:

  #traverse through left if target's val < root, else go right

  if root is None:
    return False

  if root.val == target:
    return True

  if target < root.val:
    return binary_search_tree_includes(root.left, target)
  else:
    return binary_search_tree_includes(root.right, target)
  
    # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def is_binary_search_tree(root):
  values = []
  in_order_traversal(root, values)
  return is_sorted(values)


def in_order_traversal(root, values):
  if not root:
    return

  in_order_traversal(root.left, values)
  values.append(root.val)
  in_order_traversal(root.right, values)

def is_sorted(numbers):
  for i in range(0, len(numbers) - 1):
    current = numbers[i]
    next = numbers[i + 1]

    if next < current:
      return False

  return True

      

  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def post_order(root):
  values = []
  traverse(root, values)
  return values


def traverse(root, values):
  if not root:
    return

  traverse(root.left, values)
  traverse(root.right, values)
  values.append(root.val)

  

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_post(in_order, post_order):
  #root node is end of post_order
  #find root node in the in_order
  #everything to left is added on left side
  #everythign on right is added on right side

  if len(post_order) == 0:
    return None

  last_node = post_order[-1]
  root = Node(last_node)

  #find the index of it in_order
  mid = in_order.index(last_node)
  left_side = in_order[:mid]
  right_side = in_order[mid + 1:]

  left_post=post_order[:len(left_side)]
  right_post = post_order[len(left_side):-1]

  root.left = build_tree_in_post(left_side,left_post)
  root.right =build_tree_in_post(right_side, right_post)

  return root

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_pre(in_order, pre_order):
  #grab first node in beginning
  #find it in in order, left of it isin left 
  #else everything in right

  if len(in_order) == 0:
    return None

  val = pre_order[0]
  root = Node(val)

  mid = in_order.index(val)
  left_in = in_order[:mid]
  right_in = in_order[mid + 1:]

  post_left = pre_order[1: 1 + len(left_in)]
  post_right=pre_order[1 + len(left_in):]

  root.left = build_tree_in_pre(left_in, post_left)
  root.right = build_tree_in_pre(right_in, post_right)

  return root
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def check_balanced_tree(root):
  if not root:
    return 0

  left = check_balanced_tree(root.left)
  if left == -1:
    return -1

  right = check_balanced_tree(root.right)
  if right == -1:
    return -1


  if abs(left - right) > 1:
    return -1
  else:
    return 1 + max(left, right)

def is_tree_balanced(root):
  return check_balanced_tree(root) > -1

class MinHeap:
  def __init__(self):
    self.list = []
    
  def is_empty(self):
    return len(self.list) == 0

  def size(self):
    return len(self.list)

  def swap(self, idx1, idx2):
    self.list[idx1], self.list[idx2] = self.list[idx2],  self.list[idx1]

  def sift_up(self, idx):
    current_idx = idx
    while current_idx > 0:
      parent_idx = (current_idx - 1) // 2
      if self.list[current_idx] < self.list[parent_idx]:
        self.swap(current_idx, parent_idx)
        current_idx = parent_idx #might have to sift up further so update new index
      else:
        break;
      
  def insert(self, val):
    self.list.append(val)
    self.sift_up(len(self.list) - 1)
    

    def kth_largest(numbers, k):
  sorted_nums = sorted(numbers)
  return sorted_nums[-k]
    

    import heapq

def k_smallest(nums, k):
  # result = []
  # sorted_nums = sorted(nums)

  # for num in sorted_nums:
  #   if len(result) == k:
  #     return result
  #   else:
  #     result.append(num)
  # return result

  heap = []
  for num in nums:
    item = (-num, num)
    heapq.heappush(heap, item)
    if len(heap) > k:
      heapq.heappop(heap)
  result = []
  while len(heap) > 0:
    item = heapq.heappop(heap)
    element = item[1]
    result.append(element)

  return result[::-1]
      

def subsets(elements):
  #receive a list of elements
  #return a subset of it

  #if list is empty return an empty list


  if not elements:
    return [[]]

  first = elements[0]
  remaining = elements[1:]
  without_first_subsets = subsets(remaining)

  subsets_with_first = []
  for sub in without_first_subsets:
    subsets_with_first.append([first, *sub])
    
  return subsets_with_first + without_first_subsets

def permutations(items):
  if len(items) == 0:
    return [ [] ]


  first = items[0]

  full_perm = []
  for perm in permutations(items[1:]):
    for i in range(len(perm) + 1):
      full = perm[:i] + [first] + perm[i:]
      full_perm.append(full)
  return full_perm
  
  def create_combinations(items, k):
  if len(items) < k:
    return [ ]

  if k == 0:
    return [[]]

  result = []
  first = items[0]

  partial_combos = create_combinations(items[1:], k-1)

  for combo in partial_combos:
    result.append([first, *combo])


  combos_no_first = create_combinations(items[1:], k)

  return result + combos_no_first

def grocery_budget(grocery_list, budget):
  #receive a list and a budget

  if budget < 0:
    return []

  if not grocery_list:
    return [[]]


  #include first
  first_item, money = grocery_list[0]
  result = []
  for item in grocery_budget(grocery_list[1:], budget - money):
    item.append(first_item)
    result.append(item)
    

  #create without the first one
  result += grocery_budget(grocery_list[1:], budget)

  return result


  def grocery_budget(grocery_list, budget):
  if budget < 0:
    return []

  if len(grocery_list) == 0:
    return [ [] ]

  item, money = grocery_list[0]
  remaining = grocery_list[1:]

  result = []
  for grocery in grocery_budget(remaining, budget - money):
    grocery.append(item)
    result.append(grocery)


  rest_of_items = grocery_budget(remaining, budget)

  return result + rest_of_items
  

  def lining_up(people, capacity):
  if capacity > len(people):
    return []

  
  if capacity == 0:
    return [[]]

  first = people[0]
  remaining = people[1:]

  all_ways = []

  for peep in lining_up(remaining, capacity - 1):
    for i in range(0, len(peep)+ 1):
      all_ways.append([*peep[:i], first, *peep[i:]])


  all_ways += lining_up(remaining, capacity)

  return all_ways
      
      def possible_paths(graph, src, dst):
  if src == dst:
    return [ [src]]

  paths = []
  for neighbor in graph[src]:
    neighbor_paths = possible_paths(graph, neighbor, dst) #grab remaining
    for neighbor_path in neighbor_paths:
      neighbor_path.insert(0, src) #then add back in src node
      paths.append(neighbor_path)


  return paths
  
  def parenthetical_possibilities(s):
  if len(s) == 0:
    return [""]

  choices, remainder = get_choices(s)

  all_pos = []
  for choice in choices:
    reminder_poss = parenthetical_possibilities(remainder)
    for poss in reminder_poss:
      all_pos.append(choice + poss) #lets add back the first letter (choice)
  return all_pos

  
def get_choices(s):
  if s[0] == '(':
    end = s.index(')')
    choices = s[1:end]
    remainder = s[end + 1:]
    return (choices, remainder)
  else:
    return (s[0], s[1:])
  

  def substitute_synonyms(sentence, synonyms):
  words = sentence.split(" ")
  subarrays = generate(words, synonyms)
  final_result = []

  for subarray in subarrays:
    final_result.append(' '.join(subarray))

  return final_result



def generate(words, synonyms):
  if len(words) == 0:
    return [[]]
  
  first = words[0]
  remaining = words[1:]
  subarrays = generate(remaining, synonyms)

  if first in synonyms:
    result = []
    for syn in synonyms[first]:
      for subarray in subarrays:
        result.append([syn, *subarray])
    return result
  else:
    result = []
    for subarray in subarrays:
      result.append([first, *subarray])
    return result
    
      
from collections import deque

def knight_attack(n, kr, kc, pr, pc):
  #receive a n length of board, positions for knight and positions for pawn
  #return the min moves
  #ex: 

  #do it via bfs
  #start with a queue with knights positions

  queue = deque([ (kr, kc, 0) ])
  visited = set()
  visited.add((kr, kc))
  while queue:
    r,c,step = queue.popleft()
    if (r,c) == (pr, pc):
      return step

    neighbor_positions = get_knight_positions(n, r, c)

    for neighbor_pos in neighbor_positions:
      if neighbor_pos not in visited:
        neighbor_row, neighbor_col = neighbor_pos
        visited.add((neighbor_row, neighbor_col))
        queue.append((neighbor_row, neighbor_col, step + 1))
  return None
      
def get_knight_positions(n, kr, kc):
  positions = [
    (kr + 2, kc + 1),
    (kr-2, kc + 1),
    (kr + 2, kc -1),
    (kr-2, kc -1),
    (kr + 1, kc + 2),
    (kr +1, kc -2 ),
    (kr -1, kc + 2 ),
    (kr -1, kc -2)
  ]

  valid_positions = []
  for pos in positions:
    r,c = pos
    if 0 <= r < n and 0 <= c < n:
      valid_positions.append(pos)
  return valid_positions
    
    def can_color(graph):
  #receive an adj list
  #return boolean if can color all nodes of graphs in two colors
  #ex: 

  coloring = {}
  for node in graph:
    if node not in coloring:
      if validate(graph, node, coloring, False) == False:
        return False
  return True


def validate(graph, node, coloring, current_color):
  if node in coloring:
    return current_color == coloring[node]

  coloring[node] = current_color

  for neighbor in graph[node]:
    if validate(graph, neighbor, coloring, not current_color) == False:
      return False

  return True
  
    
    def tolerant_teams(rivalries):
  #receive a list of tuples
  #return boolean if can separate people into two teams 
  #ex: 

  #build a graph
  #iterate through it
  #color it



  graph = build_graph(rivalries)
  coloring = {}

  for node in graph:
    if node not in coloring:
      if validate(graph, node, coloring, False) == False:
        return False
  return True

def validate(graph, node, coloring, current_color):
  if node in coloring:
    return coloring[node] == current_color

  coloring[node] = current_color
    
  for neighbor in graph[node]:
    if validate(graph, neighbor, coloring, not current_color) == False:
      return False
  return True


def build_graph(rivalries):
  graph = {}

  for edge in rivalries:
    a,b = edge

    if a not in graph:
      graph[a] = []

    if b not in graph:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

  return graph

def tolerant_teams(rivalries):
  #receive a list of names
  #return boolean
  #ex:

  #build a graph
  graph = build_graph(rivalries)
  coloring ={}

  for node in graph:
    if node not in coloring:
      if validate(graph, node, coloring, False) == False:
        return False

  return True

def validate(graph, node, coloring, current_color):
  if node in coloring:
    return coloring[node] == current_color

  coloring[node] = current_color

  for neighbor in graph[node]:
    if validate(graph, neighbor, coloring, not current_color) == False:
        return False
  return True
    

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
  

  def rare_routing(n, roads):
  #receive n int, and (list)
  #return boolean

  graph = build_graph(n, roads)

  visited = set()
  valid = validate(graph, 0, visited, None)
  return valid and len(visited) == n

def validate(graph, node, visited, last_node):
  if node in visited:
    return False

  visited.add(node)

  for neighbor in graph[node]:
    if neighbor != last_node and validate(graph, neighbor, visited, node) == False:
        return False
  return True

def build_graph(n, roads):
  graph = {}

  for city in range(0, n):
    graph[city] = []

  for road in roads:
    a,b = road
    graph[a].append(b)
    graph[b].append(a)


  return graph
  
  def topological_order(graph):
  #receive an adj list
  #return a list of nodes in order 
  #ex: 

  #go through and add them into edges
  #go through the parents value is none
  #add to a ready nodes
  #process it
  #and return the list
  num_parents = {}
  for node in graph:
    num_parents[node] = 0

  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1

  ready = [node for node in num_parents if num_parents[node] == 0 ]

  order = []
  while ready:
    node = ready.pop()
    order.append(node)

    for child in graph[node]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        ready.append(child)
    
  return order

  
      
def topological_order(graph):
  #receive an adj list
  #return the nodes in top order from parents to childs
  #ex: 

  #create a parent node obj
  #iterate through ready list with no kids
  #then pop them off
  #then decrement their kids

  parents = {}
  for node in graph:
    parents[node] = 0

  for node in graph:
    for child in graph[node]:
      parents[child] += 1

  ready = [node for node in parents if parents[node] == 0]
  #who does nobody point to

  result = []
  while ready:
    node = ready.pop()
    result.append(node)
    for child in graph[node]:
      print(child, graph[node], parents[child])
      parents[child] -= 1
      if parents[child] == 0:
        ready.append(child)
  print(result)
  return result
    
    
  
    
  
    
  
  
  

  

      

