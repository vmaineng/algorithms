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
