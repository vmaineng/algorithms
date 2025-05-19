def anagrams(s1, s2):
  #receive two strings
  #return True if anagrams if each other, else false
  #ex: 'hello', 'fish' => false
  #ex: 'elbow', 'below' => True

  #brute force: split, sort and compare if they are equal to each other
  # return sorted(list(s1)) == sorted(list(s2))
  #return sorted(s1) == sorted(s2)

  #create a dictionary for first string
  #iterate through the second string
  #subtract the values seen
  #if dictionary is empty, return True
  #else return false

  dict = {}
  for char in s1:
    if char not in dict:
      dict[char] = 0
    dict[char] += 1

  for char in s2:
    print(dict)
    if char not in dict:
      return False
    dict[char] -=1
    if dict[char] < 0:
      return False
  return True
    
print(anagrams('paper', 'reapa'))

def most_frequent_char(s):
  #receive a string of lowercase chars
  #return the most frequent letter most_frequent_ch
  #ex: 'hello' =>> 'l'

  #keep track of letters seend
  #if value is > max
  #update letter 

  letter = ''
  maxSeen = 0
  dict = {}
  for char in s:
    dict[char] = dict.get(char, 0) + 1
  for key,value in dict.items():
    if value > maxSeen:
      maxSeen = value
      letter = key
  return letter

def pair_product(numbers, target_product):
  dict = {}
  for idx, num in enumerate(numbers):
    divisor = target_product// num
    if divisor in dict:
      return (idx, dict[divisor])
    dict[num] = idx