# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# def goose_filter(birds):
    #receive a list of string of birds
    #return a filter list where all of the 'geese' animals are removed
    #ex: ['Pig', 'Pilgrim', 'Penguin'] => ['Pig', 'Penguin']
    
    #intitialize an empty list
    #iterate through all the bird names in the bird list,
    #check to see if their name is not in geese's list
    #add to empty list
    #return the list back
    
    #list comprehension
    #return nameofBird if bird is not in the geese list
    #return [name for name in birds if name not in geese]

#time: O(n)
#space: O(n)    

def stray(arr):
    #receive a list of integers
    #return an integer that is the odd one out
    #ex: [3,3,3,3, 2] => 2
    
    #initialize an empty dictionary
    #iterate through all the numbers in the list
    #increment the count that we see for each value
    #check which value has a count of 1 - it showed up once
    #return the num
    
    # dictionary = {}
    
    # for num in arr: 
    #     dictionary[num] = dictionary.get(num, 0) + 1
    
    # for [key, value] in dictionary.items():
    #     if dictionary[key] == 1:
    #         return key

    # for idx in range(1, len(arr)):
    #     if arr[idx] != arr[idx -1]:
    #         return arr[idx]
        
    #time: O(n) => n amount in list to traverse through
    #space: O(n) => n integers to be stored in the dictionary

    a = arr[0]
    b = None

    for idx in range(1, len(arr)):
        if arr[idx] != a:
            b = arr[idx]
    return b
    
print(stray([3,2,2,2]))
print(stray([2,2,2,3]))
         #  idx-1
         #    idx

#maxValue = first number; stray[0]
#traverse through
#keep track of the num I've seen
#if you are a new number, you are Odd one out
#return the num we are looking at

def persistence(n, count = 0):
    # receive an integer
    #return back an integer of the count of how many times to multiply the number until it becomes one
    #number
    
    #ex: 39 => 3 * 9 => 27 => 2 * 7 => 14 => 1 * 4 => 4 => return back 3
    
    #base case: 
    #if it's single digit
    #len == 1
    
    #recursive call
    #split the digits and multiply them together
    #keep track of count
    
#     count = 0
    
    if n < 10:
        return count
    
    total = 1
    for digit in str(n):
        total *= int(digit)
    return persistence(total, count + 1)
    
    
    def is_valid_walk(walk):
    #receive a list of lowercase letters representing directions
    #return boolean to see if we can walk in the meantime and return back to original position
    
    #ex: ['n','s','n','s','n','s','n','s','n','s'] = 0
    #1 letter= 1 min
    #return back to your original position
    
   #ex: ['w','e','w','e','w','e','w','e','w','e','w','e'] = 0
  #count:1.  -1  1   -1   1
    #total.  0    1    0
    
    #keep count of blocks ; initialize it to 0
    #once we move away, we add to count
    #if we come back, we minus from count
    #if we go N, add one
    #if we come back down south, - one
    #if we east, add one, if we go west -one
    
    if len(walk) > 10:
        return False
    
#     blocks = 0
#     currentPosition = 0
    
#     direction = { 
#         'n': 1,
#         's': -1, #n and s are opposite, 
#         'e': 1, #e and w are opposite
#         'w': -1
#     }
    
#     for char in walk:
#         if direction[char]:
#             blocks += direction[char]
#             print(blocks)
#     return blocks == currentPosition

    if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(walk) == 10:
        return True
    else:
        return False
    
    

def name_shuffler(str_):
    #receive a string of of two words
    #return the name swapped
    #ex: 'mary joe' => 'joe mary'
    
    splitName = str_.split(" ")
    return ' '.join(splitName[::-1])

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for char in s: #closing bracket
            if char in brackets:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack

     class Solution:
    def isValid(self, s: str) -> bool:
        #receive a string of opening and closing parens
        #return True if matching, else False
        #ex: ')()' => False

        #initialize an empty stack
        #iterate through char
        #check to see if it is a closing bracket
        #then check if stack's not empty and the last one is an opening that matches
        #then pop it off
        #else return False
        #else it is an opening, add to stack
        #return if stack's empty

        stack = []

        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in brackets:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
    def bestDigits(number, numDigits):
    # receive a string of integers
    #return the biggest number from the string of integers

    #ex: '342', 1 => '42'

    #iterate each num
    ##initialize a stack
    #check if the stack is not empty
    #and that the new number is greaterthan previous


    stack = []
    for num in number:
        while numDigits > 0 and len(stack) >0 and num > stack[len(stack) - 1]:
            numDigits -=1
            stack.pop()
        
        stack.append(num)

     while numDigits > 0:
        numDigits -=1
        stack.pop()
    return ''.join(stack)
def spiralTraverse(array):
    output = []

    startRows, endRows= 0, len(array)-1
    startCols, endCols = 0, len(array[0]) -1

    while startRows <= endRows and startCols <= endCols:
        for col in range(startCols, endCols + 1):
            output.append(array[startRows][col])
        startRows += 1

        for row in range(startRows, endRows + 1):
            output.append(array[row][endCols])
        endCols -= 1

        if startRows <= endRows:
            for col in range(endCols, startCols -1, -1):
                output.append(array[endRows][col])
            endRows -= 1

        if startCols <= endCols:
            for row in range(endRows, startRows -1, -1):
                output.append(array[row][startCols])
            startCols += 1

    return output

def sortStack(stack):
    # receive a list of integers
    #return the integers sorted using a stack

    #look at the top number
    #compare to the num i popped off
    #check if it's less

    #initialize a helperStack to hold values
    #stack keeps original sorted list

    helperStack = []

    while len(stack) > 0:
        temp = stack.pop()
        # helperStack.append(temp)

        while len(helperStack) > 0 and temp > helperStack[len(helperStack) -1]:
            stack.append(helperStack.pop())
    while len(helperStack) > 0:
        stack.append(helperStack.pop())
    return stack
    
def divisible_by(numbers, divisor):
    #receive a list of integers, and an integer
    #return a list where the num is divisible by the numbers in the list
    
    return [num for num in numbers if num % divisor == 0]

def solution(nums):
    #receive a list of integers
    #return the nums sorted in the list
    
    return sorted(nums) if nums else []

def pipe_fix(nums):
    #receive a list of integers
    #return a list where every num is included 
    
    return [num for num in range(nums[0], nums[-1] + 1)]

def arithmetic(a, b, operator):
    #receive integers
    #return the operation of a and b contingent on operator
    
    if operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a- b
    elif operator == 'multiply':
        return a * b
    else:
        return a/b
    
    def unique_in_order(sequence):
    #receive a string of integers or chars
    #return a list back where the same values are not next to it
    
    #intiialize an empty list
    #iterate through the sequence to check if the values are the same
    #then move the pointer if they are the same
    
    if not sequence:
        return []
    
    output = [sequence[0]]
    i = 0
    
    for item in range(1, len(sequence)):
        if sequence[item] != sequence[i]:
            output.append(sequence[item])
        i = item
    return output

def firstNonRepeatingCharacter(string):
    # receive a string of lowercase letters
    #return the index of first non-repeating char

    #ex: 'hello' => 0 'h'

    #iterate through the chars
    #kept track of how many chars seen
    #check to see if char has an occurence of 0

    dict = {}
    for char in string:
        dict[char] = dict.get(char, 0) + 1

    for i, char in enumerate(string):
        if dict[char] == 1:
            return i
    return -1

    # #set
    # #iterate through the string
    # #check if set already has char, 
    # #if so, delete, else add
    # #return the index position of what set has left

    # uniqueChar = set()
    # for char in string:
    #     if char not in uniqueChar:
    #         uniqueChar.add(char)
    #     else:
    #         uniqueChar.remove(char)
    # uniqueItem = string.index(uniqueChar[char])
    
def sum_numbers_recursive(numbers):
  #receive a list of integers
  #return the total recursively

  #ex: [3, 2, 1] => 3 + 2 = 5 + 1 =6
  if len(numbers) == 0:
    return 0
  for num in numbers:
    return numbers[0] + sum_numbers_recursive(numbers[1:])
  
  def plural(n):
    #receive an integer (pos, 0)
    #return a boolean - true if plural, else False if it's singular
    #ex: 4 => pluarl True
    
    #1 => False
    #2 => True
    
    #if n == 1: return False
    #else return True
    
#     if n == 1:
#         return False
#     else:
#         return True
    return False if n == 1 else True
  
def break_chocolate(n, m):
    #receive integers for n and m
    #return the min number of breaks needed
    #ex: 2, 1 => 1 [] []
    #ex: 2, 2 => [] []
     #           [] [] => 3
        
    #chocolate is 0,0, 1,1 => 0
    #2*2 => 4 - 1 = 3
    
    return (n * m) - 1 if n > 0 and m > 0 else 0

def narcissistic( value ):
    #receive an integer (postive and >0)
    #return True if narcisstic number else return False
    
    #ex: 7 ; 7 ^1 => 7 => True
    #ex: 122 ; length of 3
    #.  1 ^3 + 2 ^3 + 2^3 => 1 + 8 + 8 => 17 => False
    
    #edge cases: if value is 0
    
    #find the length of the integer
    #convert value into a string to find length of integer
    #calculate each num to the length of the integer
    #check the total to see if it's equal to the value
    #return True
    #else return False
    
    lengthNum = len(str(value))
    total = 0
    
    for num in str(value):
        total += int(num) ** lengthNum
#     if total == value:
#         return True
#     else:
#         return False
    return total == value

#time and space complexity:
#time: O(1) 
#space:O(1)
    
    class Solution:
    def reverseVowels(self, s: str) -> str:
        #receive a word of lowercase and uppercase
        #return a new string where the vowels are reversed
        #ex: 'hello' => 'holle'

        #initialize a new list
        #iterate through the list
        #check to see if it is a vowel
        #if it's not, we can append the char to list
        #

        #initialize a list of vowels that consist of uppercase and lowercase
        #iterate through each char
        #check if it is a vowel
        #then swap it
        #return the new string

        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O','U']
        s= list(s)
        # print(s)
        left = 0
        right = len(s) -1

        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -=1
            elif s[left] not in vowels:
                left += 1
            else:
                right -=1
        return ''.join(s)

def sale_hotdogs(n):
    #receive an integer
    #return terinary expression
    #ex: 4 => 100
    #ex: 8 => 95
    
    return n * 100 if n < 5 else ( n * 95 if n >=5 and n < 10 else n * 90)

def spiralTraverse(array):
    # receive a 2d array

    #iterate through top col and capture each item from row
    #then right
    #then bottom
    #thenleft

    output = []
    startRows, endRows = 0, len(array) -1
    startCols, endCols = 0, len(array[0]) - 1

    while startRows <= endRows and startCols <= endCols:
        for col in range(startCols, endCols + 1):
            output.append(array[startRows][col])
        startRows += 1

        for row in range(startRows, endRows +1):
            output.append(array[row][endCols])
        endCols -=1

        if startRows <= endRows:
            for col in range(endCols, startCols-1, -1):
                output.append(array[endRows][col])
            endRows -= 1

        if startCols <= endCols:
            for row in range(endRows, startRows -1, -1):
                output.append(array[row][startCols])
            startCols += 1
    return output

def firstNonRepeatingCharacter(string):
    # receive a string of lowercase chars
    #return the index of which value is 1

    dict = {}
    for char in string:
        dict[char] = dict.get(char,0) +1

    for idx, char in enumerate(string):
        if dict[char] == 1:
            return idx
    return -1

def problem(a):
    #receive a number
    #return the total
    #ex: 'yo' => 'Error'
    #return n * 50 + 6
    
    return 'Error' if a == str(a) else a * 50 +6

 try:
        return a * 50 + 6
    except TypeError:
        return "Error"

def check_alive(health):
#     if health <= 0:
#         return False
#     else:
#         return True
    return False if health <= 0 else True

def sort_by_length(arr):
    #receive a list of string in lowercase and uppercase letters
    #return the a list back where strings are ordered from shortest to longest
    
    #ex: ['hello', 'four', 'hi'] => ['hi', 'four', 'hello']
    
    #initialize an empty list
    #iterate through each word
    #check the length of each word
    #add it into the string
    
    #sort by string length
    return sorted(arr, key= lambda word: len(word))

def order(sentence):
  # receive a string of words with a number in it
#return the string back in order based on the number in it
    #ex: "Happy2 Monday1"
    
    #intiialize an empty list
    #iterate through each word
    #check for 1, then for 2, and add to the list
    #return it as a string

    
    stringWords = []
    
    words = list(sentence.split()) #['is2', 'Thi1s', 'T4est', '3a']
    
    for word in words: 
        if word.isdigit():
            if char == str(count):
                stringWords.append(sentence[word])
                count += 1
    return ' '.join(stringWords)

def add_five(num):
    total = num + 5
    return total

# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multiplier = 1):
    # receive a list of lists of numbers
    #return the total of all numbs together

    #[4[3,8]] => 4 + 2 * (8 +3) 4+ 22 => 26

    #iterate through each eelemnt of the list
    #check if it is a list
    #then add all the numbers, increase the multiplei
    #else, it's not a list, then add all the numbers together
    #add sum together

    total = 0
    if not array:
        return 0

    for element in array:
        if type(element) is list:
            total += productSum(element, multiplier + 1)
        else:
            total += element
    return total * multiplier
    
    def combat(health, damage):
    #receive integers for health and damage
    #return the player's new health
    
    #ex: 25, 10 => 25 - 10 = 15
    #ex: 25, 50 => 25- 50 = -25 , but we will return 0
    
    return 0 if health - damage < 0 else health - damage

def capitalize_word (word : str) -> str:
    #'hello'
    # 0,1,2,3,4,5
    word = word[0].upper() + word[1:] # 'a' , 'b' => 'ab'
    return word

    #receive a string of letters
    #return the first letter uppercase
    
    #ex: 'h' => 'H'
    #ex: 'hello' => 'Hello'
    
    #edge case: if length of the string is 1, captialize the letter
    #return the letter
    
    #intialize an empty list
    #iterate through each letter of the string
    #captialize the first letter of the word, add it in the list
    #add in the rest of the words into the list
    #join the list back together as a string
    
#     if len(word) == 1:
#         return word[0].upper()

#time: O(N)
#space: O(n)
    
def how_many_light_sabers_do_you_own(name=""):
    #receive a name
    #return total amount
    
  
    
    
    return 18 if name == 'Zach' else 0

def stringy(size):
    # receive an integer
    #return a string of 10
    
    #ex: 4, => '1010'
    
    #initialize an empty list
    #iterate up to size
    #add one 1 for odd position
    #add 0 for even position
    #return string back joined together
    
    numList = []
    
    for num in range(size):
        print(num)
        if num % 2 != 0:
            numList.append('0')
        else:
            numList.append('1')
    return ''.join(numList)

def distinct(seq):
#     return list(set(seq))

    #receive a list of integers
    #return a list where it removes duplicates
    #ex: [1,1, 2] => [1,2]
    
    #initialize a new list
    #sort the seq list
    #iterate through it
    #check if the next value is same value as last's
    #if it is, keep going forward
    #return new list
    
    
    
    
    seq = sorted(seq)
#     print(seq)
    
    uniqueList = [seq[0]]
    
    i = 0
    
    for idx,num in enumerate(seq):
        if seq[i] != num:
            uniqueList.append(num)
        i = idx
        print(seq[i], num)
    return uniqueLists

def distinct(seq):
#     return list(set(seq))

    #receive a list of integers
    #return a list where it removes duplicates
    #ex: [1,1, 2] => [1,2]
    
    #initialize a new list
    #sort the seq list
    #iterate through it
    #check if the next value is same value as last's
    #if it is, keep going forward
    #return new list
    
    if not seq:
        return []
    
    seq = sorted(seq)
#     print(seq)
    
    uniqueList = [seq[0]]
    
    i = seq[0]
    
    for num in seq[1:]:
        if num != i:
            uniqueList.append(num)
            i = num
#         print(seq[i], num)
    return uniqueList

def distinct(seq):
    #a list of integers positive
    #return the result of unique number
    #ex: [2, 3, 4,4, 5] => [2,3,4, 5]
    
    #.   i 
        #    j
    
    #initialize an empty list
    #have a pointer starting at the first number in the list
    #second pointer starting at the number next to the first pointer
    #check to see if they are the same numbers
    #if not, add in the number from the first pointer into the list
    #return the list
    
#     if not seq:
#         return []
    
#     uniqueList = []
#     i = 0
    
#     for j in range(len(seq)):
#         print(i, j)
# #         print(seq[i], seq[j])
#         if seq[i] != seq[j]: #if 2 != 3
#             uniqueList.append(seq[i])
#         i = j
#     return uniqueList

    uniqueList = []
    for num in seq:
        if num not in uniqueList:
            uniqueList.append(num)
    return uniqueList

def merge_arrays(arr1, arr2):
    #receive two lists of integers
    #return one list combined from the two lists - remove duplicates, and sorted in asecending order
    
    #ex: [1,2], [1] => [1, 2]
    #ex: [1], [] => [1]
    
    #ex: [], [2,3] => [2,3]
    
    #edge case: if both lists are empty, return []
    if not arr1 and not arr2:
        return []
    
    #if one list is empty, return the other list
    if not arr1:
        return arr2
    
    if not arr2:
        return arr1
    
    #initialize an empty list 
    #sort both lists
    
    #have a pointer in the first value in first array
    #have another pointer in the first value in second array
    #check to see which number is smaller
    #add in the number from the list
    #move pointers
    #else, move pointers if they are duplicates
    
    uniqueSet = set(arr1) | set(arr2)
    
    return sorted(list(uniqueSet))
#time: O(n)
#space: O(n)

def mouth_size(animal): 
    return 'small' if animal.lower() == 'alligator' else 'wide'

def replace_exclamation(st):
    #receive a string of characters
    #return a new string wehre vowels are replaced with '!'
    
    #ex: 'Yo' => 'Y!'
    
    #initialize a string with vowels
    #if char == vowels
    #replace with !
    #join back together as string
    
    word = []
    vowels = 'aeiouAEIOU'
    
    for char in st:
        if char in vowels:
            word.append('!')
        else:
            word.append(char)
    return ''.join(word)

def nb_dig(n, d):
    #receive integers for integer
    #return count of all squared nums that contains d
    
    count = 0
    
    for num in range (0, n + 1):
        squaredNum = num * num
        print(squaredNum)
        count += str(squaredNum).count(str(d))
    return count

  def nth_even(n):
    #receive an integer
    #return the even number of the 3rd
    
    #ex: 0 => 0
    #ex: 1 => 0
    #ex: 2=> 2
    #ex: 3 => 0, 2, 4
    
    #[0, 2, 4, 6,8]
    # 0 1   2. 3. 4
    
    #initialize a total to 0
    #iterate up to n
    #and add even number
    #return total
    
    total = 0
    for num in range(0, n-1):
        total += 2
    return total

def add_length(str_):
    #receive a string of lowercase words
    #return a list back with the word and length after it in one string
    #ex: 'hello world' => ['hello 5', 'world 5']
    
    #initialize an empty list
    #iterate through the string
    #calculate the length
    #add it to the list
    #return list back
    
    lengthList = []
    for word in str_.split():
        lengthOfWord = word +' ' + str(len(word))
        lengthList.append(lengthOfWord)
    return lengthList

    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]

def unusual_five():
    strLen = 'abcde'
    return len(strLen)

def warn_the_sheep(queue):
    #receive a list of strings of wolf and sheep
    #return 'pls go ' if wolf is closest animal
    #else return 'oi'sheep number n
    
    #ex: 
    
    count = 0
    for sheep in range(len(queue) -1, -1, -1):
        if queue[sheep] == 'wolf':
            return 'Pls go away and stop eating my sheep'
        elif queue[sheep] == 'sheep':
            count +=1
    return f"Oi! Sheep number {count}! You are about to be eaten by a wolf!"
            
    def well(x):
    #receive a list of strings of 'good' and 'bad'
    #return 'publish' on one or two good ideas, 'i smell a series', else 'fail'
    
#     for char in x:
    if x.count('good') == 0:
        return 'Fail!'
    elif x.count('good') <2 :
        return 'Publish!'
    else:
        return 'I smell a series!'
    def remove_url_anchor(url):
    # receive a string of a url
    #return anything before #
    
    #slice it out
    
    if '#' not in url:
        return url
    
    after = url.index('#')
    return url[:after] if url.index('#') else url

def chromosome_check(chromosome):
    return 'Congratulations! You\'re going to have a son.' if chromosome == 'XY' else 'Congratulations! You\'re going to have a daughter.'

def calculate_years(principal, interest, tax, desired):
#     raise NotImplementedError("TODO: calculate_years")
    #receive integers for all
    #return amount of years to wait for to achieve goals
    
    #initialize a count of years
    #iterate up to 100 years
    #if principal == desired
    #return years
    #else, add another year
    
    years = 0;
    
    while principal < desired:
        years += 1
        principal = principal + ((principal* interest) - principal*interest*tax)
    return years    

def hello(name=""):
    #receive a string of letters
    #return "Hello (name)" else return 'Hello, world'
    
    #ex: 'mark' => "Hello, Mark"
    #ex: 1234 => 'Hello, world'
    
    #check to see if name is a string
    #return 'Hello name'
    #else return 'Hello, World'
    
    if not name:
        return f"Hello, World!"
    
    if type(name) == str:
        name = name.capitalize()
        return f'Hello, {name}!'
    
    #time: O(1)
    #space: O(1) for only one name display

    def calculate_years(principal, interest, tax, desired):
    #receive all integers - floating nubmers
    #return the years it will take to turn principal amount into desired amount
    
    #ex: 100, 10%, 10%, 500 => 
    #initialize a years variable
    #while loop while principal < desired amount
    #add 1 to our years
    #calculate the interest accrued, and tax owed on the money
    #return years
    
    years = 0
    
    while principal < desired:
        years += 1
        #             1000 + 50 - 9
        principal = principal+ ((principal*interest) - (principal *interest*tax))
    return years

#time: O(n)
#space: O(1)

def no_boring_zeros(n):
    #receive an integer - pos or neg
    #return a new integer if a 0 is at the end
    
    #ex: 100 => 1
    
    #convert num to string
    #if the last num is 0 and length is > 1
    #slice it off? 
    #return num back as an integer
    
    
    stringNum = str(n)
    newString = ''
    
    if len(stringNum) == 1 and stringNum[0] == '0':
        return 0
    
#     for num in range(len(stringNum) -1, -1, -1):
# #         print('stringNum:', stringNum[num])
#         if stringNum[num] == '0':
# #             print('stringNum:', stringNum)
#             newString = stringNum[:num]
# #             print(newString)
#         else:
#             newString = stringNum[:num]
#     return int(newString)
    else:
        while stringNum[-1] == '0':
            stringNum = stringNum[:-1]
    return int(stringNum)
        
    def no_boring_zeros(n):
    #receive an integer - pos or neg
    #return a new integer if a 0 is at the end
    
    #ex: 100 => 1
    
    #convert num to string
    #if the last num is 0 and length is > 1
    #slice it off? 
    #return num back as an integer
    
    
    stringNum = str(n)
    newString = ''
    
    if len(stringNum) == 1 and stringNum[0] == '0':
        return 0
    
    for num in range(len(stringNum) -1, -1, -1):
#         print('stringNum:', stringNum[num])
        if stringNum[num] != '0':
#             print('stringNum:', stringNum)
#             newString = stringNum[:num]
#             print(newString)
            return int(stringNum[:num + 1])
#         else:
#             newString = stringNum[:num]
    return 0
#     else:
#         while stringNum[-1] == '0':
#             stringNum = stringNum[:-1]
#     return int(stringNum)
        
    def say_hello(name, city, state):
    #receive a string of [first name, last name] in a list, city, state
    #return string back
    #ex: ['Mary', 'the', 'Joseph'], 'SF', 'CA'
    
    return 'Hello, {}! Welcome to {}, {}!'.format(' '.join(name), city, state)
import re
def replace_dots(s):
    return re.sub(r"\.", "-", s)

def mango(quantity, price):
    #receive integers for quantity and price
    #return price
    #every 3rd mango is free
    
    #for every multiple of 3rds, subtract - 1
    #caclulcate price
    
    free = quantity // 3
    quantity = quantity - free
    return quantity * price

def remove(s):
    #receive a string of words
    #return words where '!' is removed at the end of the word
    #ex: 'Yo!' => "Yo"
    
    #check if last char is '!'
    #if so, slice off the ending
    
    if not s:
        return s
    if s[-1] == '!':
        return s[:-1]
    else:
        return s
    
    def get_size(w,h,d):
    #receive integers for w, h and d
    #return [area, volume]
    
    volume = w * h * d
    area = 2*((d* w) + (d*h) + (w*h))
    return [area, volume]

def capitals(word):
    #receive a string of words
    #return a list of index of where char is uppercase
    #ex: "hElLO" => [1, 3, 4]
    
    #check if char is uppercase
    #add index to list
    #return list
    return [idx for idx in range(len(word)) if word[idx] == word[idx].upper()]
#     output = []
#     for idx in range(len(word)):
#         if word[idx] == word[idx].upper():
#             output.append(idx)
#     return output

def small_enough(array, limit):
    #receive a list of integers and an integer for limit
    #return True if numbers in list is <= limit, else return False
    
    #iterate through each one of them
    #check if value is <= limit, return True, else return false
    
    for num in array:
        if num > limit:
            return False
    return True
#     return False if num > limit else True for num in array

    return all(num > limit for num in array)

def position(letter):
    #receive lowercase letter
    #return position of the alphabet
    
    #ex: 'a' => 1
    #ex: 'b' => 2
    
    #write out the entire alphabet in a string
    #find the index position in the string
    #return the index position plus 1
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     alphabet1= ['a','b','c']
    
    return f"Position of alphabet: {alphabet.index(letter) + 1}"
    
    def factorial(n, total = 1):
    #receive an integer
    #return a string that states the facorial and the total
    
    #ex: 1! 1 *0! 1 => 1 * 1 => 1
    
    #ex: 3! => 3*2*1 => 6
    
    #initialize a total to 0
    
    #edge case: if n == 0, return 1
    
    #iterate up to n
    #multiply each number
    #return the total
    
#     if n == 0:
#         return 1
    
#     total = 1;
#     for num in range(1, n + 1):
#         total *= num
#     return total

#time: O(n)
#space: O(1)

#base case: if the num reaches 0, it's 1; if the num reaches 1, it is 1
#recursive case: decrement n down by 1, add to the total
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     return n * factorial(n -1)

    if n == 0:
        return 1
    if n == 1:
        return total
    total *= n # 1 *= 3 => total = 3
    return factorial(n -1, total ) #factorial (2, 3)

#time: O(n) for number we have to visit up to n
#space: O(n) for the function call stack

def factorial(n, total = 1):
    #receive an integer
    #return a string that states the facorial and the total
    
    #ex: 1! 1 *0! 1 => 1 * 1 => 1
    
    #ex: 3! => 3*2*1 => 6
    
    #initialize a total to 0
    
    #edge case: if n == 0, return 1
    
    #iterate up to n
    #multiply each number
    #return the total
    
#     if n == 0:
#         return 1
    
#     total = 1;
#     for num in range(1, n + 1):
#         total *= num
#     return total

#time: O(n)
#space: O(1)

#base case: if the num reaches 0, it's 1; if the num reaches 1, it is 1
#recursive case: decrement n down by 1, add to the total
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     return n * factorial(n -1)

    if n < 0 or n > 12:
        raise ValueError("This is an invalid error")

    if n == 0:
        return 1
    if n == 1:
        return total
    total *= n # 1 *= 3 => total = 3
    return factorial(n -1, total ) #factorial (2, 3)

    total *= n
    return 1 if n <= 1 else factorial(n-1, total)

#time: O(n) for number we have to visit up to n
#space: O(n) for the function call stack

def factorial(n, total = 1):
    if n < 0 or n > 12:
        raise ValueError("This is invalid number.")
        
    if n == 0:
        return 1
    
    total *= n
    return total if n <=1 else factorial(n -1, total)

import re

def solution(s):
    #receive a string of lowercase characters
    #return a list of two characters in a string
    
    #ex: 'hello' => ['he', 'll', 'o_']

    ##initialize an empty list
    #iterate through string
    #with two pointers
    #one pointer moves - capturing window of two characters
    #add it the list
    #if character at the end is odd, add '_' afterwards
    #return the list
    
    return re.findall(r'.{2}', s + '_')
    
#     output = []
    
#     left = 0
#     right = 0
#     pairString = ''
    
#     while right < len(s):
#         rightChar = s[right]
#         pairString += rightChar
#         right += 1
        
#         while (right - left + 1) > 2:
# #             print(left, right)
#             output.append(pairString)
#             print(output)
#             leftChar = s[left]
#             left = right
#             pairString = ''
            
# #         else:
# #             if len(pairString) == 1:
# #                 pairString += '_'
# #                 output.append(pairString)

#     return output

output = []
if len(s) % 2:
    s + "_"

for i in range(0, len(s), 2):
    output.append(s[i: i+2])
return output

def take(arr,n):
    #receive a list of integers (pos and negative), n 
    #return a list back of the first n elements
    
    #ex: [-3, 5, 2, 8, 9] , 2 => [-3, 5]
    
    #initialize an empty list
    #iterate through the list up to n
    #return the list back
    
    return arr[:n]

def dont_give_me_five(start,end):
    # receive two integers (pos or negative)
    #return the count of elements between start and end where it does not have a 5 in it
    
    #ex: 4, 10 => 4, 6, 7, 8, 9, 10 => 6
    
    #initialize a count
    #increment starting from start all the way to end,
    #if the number does not include a 5
    #count will increment by 1
    #return the count
    
    count = 0
    skipNumber = 5
    for num in range(start, end + 1):
        if '5' not in str(num):
            count += 1
    return count

    return sum('5' not in str(num) for)

def dont_give_me_five(start,end):
    return sum('5' not in str(num) for num in range(start, end + 1))

def find_uniq(arr):
    #receive a list of integers
    #return the number that is unique
    #ex: [4,4,4,4,1, 4] => 1
    
    #brute force:
    #iterate through the list
    #check if the num next to it is the same num
    #else, return the num
    
    #optimized:
    #use a set to see if the num is different
    #return the num in the set
    
    uniqueNumbers = {}
    
    for num in arr:
        uniqueNumbers[num] = uniqueNumbers.get(num, 0) + 1
    
    for key,value in uniqueNumbers.items():
        if value == 1:
            return key
        
        def find_average(nums):
    #receive a list of integers
    #return the mean of a list of numbers in an array
    
    #ex: [3]=> 3
    #ex: [3,5] =8/2 => 4

    #find the sum of nums / len of nums
    
    return sum(nums)/len(nums) if nums else 0

const sumTree(root, total = 0) { 
    if (!root) return total
        
    if (root.left) { 
        total += root.val
    }
    if (root.right) { 
        total += root.val
    }
    return total
}

def whatday(num):
  #receive an integer
#return back what day of the week it is, else return "Wrong, please enter a number between 1 and 7"
#ex: 4 => ' Wednesday'

    #brute force: 
    #if else statements
    #check if num pass in is 1, return 'SUnday'
    #'else': "Wrong, please enter a number between 1 and 7"
    
#     if num == 1:
#         return 'Sunday'
#     elif num == 2:
#         return 'Monday'
#     elif num == 3:
#         return 'Tuesday'
#     elif num == 4:
#         return 'Wednesday'
#     elif num == 5:
#         return 'Thursday'
#     elif num == 6:
#         return 'Friday'
#     elif num == 7:
#         return 'Saturday'
#     else: 
#         return "Wrong, please enter a number between 1 and 7"

#time: O(n)
#space:O(1)

    date = { 
    1 : 'Sunday',
    2 : 'Monday',
    3 : 'Tuesday',
    4 : 'Wednesday',
    5 : 'Thursday',
    6 : 'Friday',
    7 : 'Saturday'
    }

    return date[num] if num > 0 and num < 8 else 'Wrong, please enter a number between 1 and 7'


 #another way to get this is:
 return date.get(num,'Wrong, please enter a number between 1 and 7' )


#time: O(1)
#space: O(1)

def reverse_letter(st):
    #receive a string of lowercase letters, digits and symbols
    #return a reversed string of the input excluding digits and symbols (! , 55)
    
    #ex: 'h35ell0o' => 'olleh'
    
    #initialize a list
    #iterate starting from the end all the wayt to the beginning
    #check the char to see if it is letter (char)
    #add it the list
    #return the list joined back as together as a string
    
    #built in function: isalpha() - check to see if it is alpha
    #reverse with slicing : [:: -1]
    #return it
    
    output = []
    
    for idx in range(len(st) -1, -1, -1):
        if st[idx].isalpha():
            output.append(st[idx])
    return ''.join(output)

#time: O(n)
#space: O(n)
            
    def dig_pow(n, p):
    # receive two integers
    #return an integer ; return k if n * k == taking each integer from n^1 + n^, else -1
    
    #ex: 8, 3 => 64
    #8^3 => 8 * 8 * 8 = 512
    #512/8 =64
    
    #calculate our total for n^p, n^p+1
    
    #the total of all the numbers powered, check if it is divisble by n, return -1
    
    total = 0
    for num in str(n):
        total += int(num) ** p
        p += 1
    return total /n if total /n % 1 == 0 else -1


    def remainder(a,b):
    #receive an integer of a and b
    #return the remainder

    
    larger = max(a,b)
    smaller = min(a,b)
    
    if smaller == 0:
        return None
    
    return larger % smaller

    class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #receive a string of lowercase letters
        #return the maxCount of vowel letters in the substring of s with the length of k

        #ex: 'hello', 2
        #'he' => 1
        #'el' => 1
        #'ll' => 0
        #'lo' => 1
        #return a 1

        #intialize a max count, set it 0
        #iterate through each letter in string, up to k size
        #check to see if the vowels exists in substring
        #if so, count the vowels in substring
        #if the count > max
        #update max to the current count
        #otherwise, keep looking
        #return the maxCount

        maxCount = 0
        vowels = 'aeiou'

        left = 0

        for idx in range(len(s)):
            right = s[idx]
            right += 1

            if (right - left + 1) >k:
                for char in word:
                    if char in vowels:
                        count += 1
                    if count > maxCount:
                        maxCount = count
            s[left] = -= 1
            left +=1
            
        return count
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #receive a string of lowercase chars, and an integer for k
        #return an integer of max vowels seen

        #ex: 'hiijilwo', 4 => 3 b/c of 'iiji'

        #create left and right pointer
        #iterate through strings
        #capture window of k size
        #check to see if a vowel exists
        #increment count
        #then decrement left side window
        #return count

        maxCount = 0
        left = 0
        vowels = ['a', 'u','i','e', 'o']
        count = 0

        for right in range(len(s)):
            if s[right] in vowels:
                count += 1

            if (right - left + 1) == k:

                maxCount = max(maxCount, count)
                if s[left] in vowels:
                    count -= 1
                left += 1

        return maxCount
        
        
        def correct_tail(body, tail):
#     sub = body[-1:]
#     if sub == tail:
#         return True
#     else:
#         return False
    return True if body[-1:] == tail else False

    return body[-1:] == tail

    def angle(n):
    #receive an integer
    #return sum of internal angels in degrees in a polygon
    #180/3 = 60 => 60 + 60 + 60
    #ex: 360/4 => 90
    
    #ex: 2 => 30 ; + 30
    #ex: 3 => 60
    #ex: 4=> 90 
    #ex: 5=> 120 ; 540 / 5 => 108
    #ex: 6: => 150
    #ex: 7
    
    
    #ex: 3
    #formula - (n-2) *180
    #3- 2 => 1 * 180 =180
    
    #iterate up to n
    #keep adding 30 to the total
    #return the total * n
    
    return (n-2) * 180
    
    
    
def cube_checker(volume, side):
    #receive two integers (pos or neg)
    #return True if equal sides, else False
    
    #ex: 8,2 => 2 * 2 *2 == 8 ==> True
    #ex: 10, 2 => 2 * 2 *2  == 10 => False
    
    if volume == 0 or side * side *side <= 0:
        return False
    
    
    return side * side * side == volume
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #receive a list of integers of net gain in altitude
        #return the highest altitude of point reached

        #ex: [-5, 1, 5, 0 , - 7]
#output = [0, -5, -4, 1, 1, -6] => max seen is 1

        #iterate through the list of gains
        #keep track of max altitude seen
        #keep adding from the previous number
        #add num to the list
        #return max seen

        maxAltitude = 0
        currentAlt = 0

        for num in gain:
            currentAlt += num
            maxAltitude = max(maxAltitude, currentAlt)
        return maxAltitude
    
    class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #receive a list of integers
        #return the pivot index where everything to the left of the index == everything to the right of the index
        #ex: []

        #binary search
        #start with index in the middle
        #add everything from left until middle point
        #add everything from right until middle point
        #check to see if they equal each other

        total = sum(nums)
        leftSum = 0

        for idx in range(len(nums)):
            rightSum = total - leftSum - nums[idx]
            if leftSum == rightSum:
                return idx
            leftSum += nums[idx]
        return -1

        def sum_of_differences(arr):
    #receive a list of integers
    #return the sum of list of integers in descending order
    #ex: [4, 2, 8] => [8, 4, 2] => (8-1) + (4 - 1)  + 2 = 12
    
    #initialize a total
    #sort list by biggest to smallest
    #iterate through until last integer
    #subtract it
    
    arr.sort(reverse=True)
    total = 0
    
    for idx in range(1, len(arr)):
        newTotal = (arr[idx - 1] - arr[idx] )
        total += newTotal
    return total

    return max(arr) - min(arr) if arr else 0

    class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #receive a list of integers
        #return a list of integers where the nums are overlapped

        #ex: 

        #sort the intervals by starting index
        #intiitalize a count
        #create a list starting with first pair of intervals
        #check if start time of next interval <= end time of previous interval
        #if so, merged, increment count
        #else, add in intervals
        #return count

        if not intervals:
            return 0

        count = 0

        intervals.sort(key=lambda x:x[1])
        prev_end = intervals[0][1]

        for idx in range(1, len(intervals)):
            start, end = intervals[idx]
            if start < prev_end:
                count += 1
            else:
                prev_end = intervals[idx][1]

        return count


        def how_many_dalmatians(number):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
    
    return dogs[0] if number <= 10 else (dogs[1] if number <= 50 else (dogs[3] if number == 101 else dogs[2]))

    Intervals:

    Overlapping vs Merging

    A = [1,3]
    B = [2,5]

    overlapping = occuring at same or current time
    overlapping = max(a1, b1) <= min(a2, b2)
    overlapping = max(1,2) <= min(3, 5) => do NOT overLAP

    merging = if two intervals overlap, you can "merge" them together
    new_start = min(a1, b1) => min(1,2) => 1
    new_end = max(a2, b2) => max(3, 5) => 5
    mergedInterval = [1, 5]
def string_clean(s):
    """
    Function will return the cleaned string
    """
    #receive a string of upper and lowercase chars
    #return words back where no chars are added
    #ex: 'h3ello0' => 'hello'
    
    
#     letters = []
#     for char in s:
#         if char.isalpha():
#             letters.append(char)
#     return ''.join(letters)
    return ''.join(char for char in s if not char.isdigit())
    def apple(x):
    return f"It's hotter than the sun!!" if int(x)**2 > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."

    class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #receive a list of integers
        #return a list of integers where the nums are overlapped

        #ex: 

        #sort the intervals by starting index
        #intiitalize a count
        #create a list starting with first pair of intervals
        #check if start time of next interval <= end time of previous interval
        #if so, merged, increment count
        #else, add in intervals
        #return count

        if not intervals:
            return 0

        count = 0

        intervals.sort(key=lambda x:x[1])
        prev_end = intervals[0][1]

        for idx in range(1, len(intervals)):
            start, end = intervals[idx]
            if start < prev_end:
                count += 1
            else:
                prev_end = intervals[idx][1]

        return count


        class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #receive a list of intervals
        #return count of how many intervals to be removed so they do not overlap

      
        intervals.sort(key=lambda x:x[1])
        count = 0

        prevInterval = intervals[0][1]
        print(prevInterval)

        for idx in range(1, len(intervals)):
            start, end = intervals[idx]
            if start < prevInterval:
                count += 1
            else:
                prevInterval = max(end, prevInterval)
        return count

        def sum_mul(n, m):
    #receive two positive integers
    #return sum of all the multiples from n to m
    
    #ex: (3, 9) => 3 + 6 => 9

    #initialize a total to 0
    #iterate up to m, increment by n
    #add each number to the total
    #return the total

    #edge cases if n == 0 or m == 0 or m is negative number
    if n < 1 or m < 1:
        return 'INVALID'
    
#     total = 0
    
#     for num in range(n, m, n):
#         total += num
#     return total
    return sum(range(n, m, n)) 

    import math

def round_to_next5(n):
    #receive a n integer - pos or neg or 0
    #return the next multiple of 5
    
    #ex: -1 => 0
    #ex: -8 => -10
    
    #ex:0    5 10 15 20
    #ex:   2
    
    return math.ceil(n /5 ) * 5

    def find_even_index(arr):
    
    for idx in range(len(arr)):
        if sum(arr[:idx]) == sum(arr[idx + 1:]):
            return idx
    return -1
    
    #receive a list of integers - pos and neg
    #return the index position where sum of all left and sum of all right == each other
    #else return -1
    
    #ex: [1,2,3,4,3,2,1] => idx 3 (4)
    #           x
    #.          i
    #ex: first round = 1 == 16
    #ex: 2nd = 3 == 13
    #ex: 3rd = 6 = 10
    #ex 4th = 10 = 6
    
    #ex: [1,2,3,4,3,2,1] => idx 3 (4)
    #ex:  x
    #ex:1st = 1 = ,2,3,4,3,2,1
    #ex: 2nd = 1,2 = 3,4,3,2,1
    #ex: 3rd = 1,2,3, = 4,3,2,1]
    #ex: 4th = 1,2,3,4 = 3,2,1
    
    
    #totalList = sum = 16
    #16 - 1 = 15 == sum([idx))
    #return that idx
    #return -1


    #initialize a total of 0
    #capture the total sum of list
    #iterate from the beginning
    #total - num = sumin the list of array
    #if so, return idx
    #else, add to total
    #after looking through the entire list, return -1
    
#     total = 0
#     arrSum = sum(arr)
    
#     for idx in range(len(arr)):
#         total = arrSum - arr[idx]
#         if total == arrSum:
#             return idx
#         else:
#             total += arr[idx]
#     return -1
    
    #currentSum
    #iterate through the list of integers
    #check if sum of slicing up to idx == sum of slicing after idx:
    #return idx if true
    #else return -1
    
    
    def find_even_index(arr):
    totalSum = sum(arr)
    currSum = 0
    
    for idx in range(len(arr)):
        rightSum = totalSum - currSum - arr[idx]
        if rightSum == currSum:
            return idx
        currSum += arr[idx]
            
    return -1

#     for idx in range(len(arr)):
#         if sum(arr[:idx]) == sum(arr[idx+1:]):
#             return idx
#     return -1
