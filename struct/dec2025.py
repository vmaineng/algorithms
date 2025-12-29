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