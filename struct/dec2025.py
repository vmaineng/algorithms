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
    
