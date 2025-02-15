def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

        def get_count(sentence):
    vowels = 'aeiou'
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count
    def number_to_string(num):
    #receive a number
    # Return a string of the number here!
    
    #ex: 42 => '42'
    #ex: -5 => '-5'
    
    return str(num)

    def opposite(number):
  # receive a number
# return the opposite of the number passed in
#ex: 14 => -14
#ex: -280 => 280
    return (-number)

    def solution(string):
    #receive a string of lowercase letters
    #return the string back in reversed
    
    #ex: 'yo' => 'oy'
    #ex: 'apple' => 'elppa'
    
    #create a new string
    #iterate through string starting at the end
    #add on to the new string
    #return new string
    
    revString = ''
    for i in range(len(string)-1, -1, -1):
        revString += string[i]
    return revString


    #range(start, stop, step)
    return str[::-1]

    def bool_to_word(boolean):
    return "Yes" if boolean else "No"

    def summation(num):
    #receive a number
    #return the sum of each number up to num
    #ex: 5 => 1 + 2 + 3 +4 +5 =15
    
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum
    
      return sum(range(num+1))
#use python's built in sum function with a range
def no_space(x):
    #receive a string of characters with spaces
    #return a string back with no spaces
    
    #ex: 'jum d p j' => 'jumdpj'
    
    return x.replace(" ", "")
    return "".join(x.split())

    def double_integer(i):
    #receive an integer
    #return the double amount of i
    #ex: 2 => 4
    #ex: 8 => 16
    
    return i * 2
    def count_sheeps(sheep):
  # receive an array of true and false
#return a count of how many true exists in array
#ex: [T, F , F, F, F] => 1

#initialize a count
#iterate through sheep
#check if the value is equal to true
#increment count
#return count

    count = 0
    for s in sheep:
        if s:
            count += 1
    return count

    def find_smallest_int(arr):
    # receive an array of integers
    # return the smallest number
    # [33, 5, 62, 1, -3] => -3
    
    #using min function on arr
    #or could keep track of smallest number and iterate through entire array
    
    
    #return min(arr)
    smallest = arr[0]
    for ele in arr:
        if ele < smallest:
            smallest = ele
    return smallest

    def get_middle(s):
    #receive a string of letters, uppercase and lowercase
    #return the middle letter
    #if odd return only one letter
    #if even return two letters
    
    #ex: 'apple' => 'p'
    #ex: 'ford' => 'or'
    
    #brute force:
    #calc the length of s string
    #return the string's slice of middle numbers
    
    length = len(s)
    if length % 2 == 1:
        return s[length //2]
    else:
        return s[length //2 -1 :length //2 + 1]

        def string_to_number(s):
    return int(s)
    
    def summation(num):
    #receive a number
    #return total sum from 1 up to num
    #ex: 4 => 1 + 2 + 3 +4 => 10
    
#     sum = 0
#     for number in range(1, num+1):
#         sum = sum + number
#     return sum

    return sum(range(1, num +1))
    
    # Write a function `greet` that returns "hello world!"
def greet():
    return 'hello world!'
    
    def find_smallest_int(arr):
    return min(arr)
def sum_two_smallest_numbers(numbers):
    #receive a list of integers
    #return sum of the two lest positive numbers
    #ex: [3, 32, 6, 7] => [3, 6, 7, 32] => 3 + 6 => 9
    
    #sort the numbers list
    #add sum of first and second number
    
    numbers.sort();
    return numbers[0] + numbers[1]
    return sum(sorted(numbers)[:2])

#time: O(n logn)
#space: O(1)

def boolean_to_string(b):
    #receive a boolean value
    #return string boolean value
    #True => 'True'
    
    return str(b)

    def friend(x):
    #receive a list of string of names
    #return a list of string of names with length of 4
    
    #ex: ['joe', 'jerry', 'boby'] => ['boby']
    
    #initialize an output of list
    #iterate through the list of names
    #check of len is 4
    #add to list
    #return list
    
    #using a for loop
    output = []
    for friend in x:
        if (len(friend)) == 4:
            output.append(friend)
    return output

    #list comprehension
    return [f for f in x if len(4) == 4]

    #!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        if i % 3 ==0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)

    def twoNumberSum(array, targetSum):
    #receive an array of integers, and a target integer
    #return the two values an array back that totals target
    #ex: [3, 5,1, -1, 3], 6 => [5,1]

    #iterate through with outer loop at i
    #iterate inner loop at j
    #if the two values equal targetsum
    #return in a pair
    #else return [-1, -1]

    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #receive a list of integers and a target number
        #return the two indices that add up to target
        #[3, 4, 5, 6, -1], target = 3 => [1, 4]

        #iterate through the list starting at idx 1
        #then have an inner loop loop through the rest of the array
        #check if they are equal to the target, then return the list of two indices found
        #else return a list of [-1, -1]

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
        
        def twoNumberSum(array, targetSum):
    #initialize a dictionary
    #iterate through the array
    #check if the difference is found in the array's value
    #if not add it in dictionary
    #else return the values found

    dict = {}
    for i,num in enumerate(array):
        difference = targetSum - num
        if difference in dict:
            return [difference, array[i]]
        dict[num] = i
    return []

    def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx+=1
        arrIdx+=1
    return seqIdx == len(sequence)

def isValidSubsequence(array, sequence):
    # receive a list of numbers, and a list of sequence
    #return true if each value in sequence is found in array
    #ex: array= [34, 2, 5, 6, -8], seq = [3, 5, 6, 1]
    #return false

    #create an i pointer
    #iterate through the array
    #if the values are the same
    #move the i pointer in sequence's list
    #if pointer reached the end of sequence's list
    #return true, else return false

    i = 0

    for value in array:
        if i == len(sequence):
            break
        if value == sequence[i]:
            i+=1
    return i == len(sequence)


competitions = [["Team A", "Team B"], ["Team C", "Team D"], ["Team E", "Team F"]]
results = [1, 0, 1]

#grab value: iterates through competitions list, and compeition holds each value
#in the list during each iteration
for competition in competitions:

#grab index: iterates through indices of the competitions list(0 to len(compeitions)-1)
for idx in range(len(compeitions))

#grab value and index:
#enumerates the competitions list, returning both the idx and value of each element
#during the iteration
for idx,compeition in enumerate(compeitions)

#zip function: pairs element from the compeitions list and the result list at the 
#same index.
# The for loop unpacks these pairs into variables compeition and result
for competition, result in zip(competitions, results):

def paperwork(n, m):
    # receive an int for classmates and an int for m pages
    #return how many blank pages needed
    
    #ex: 3 people, 3 paperwork => 3 * 3 =9
    
    if n < 0 or m < 0:
        return 0
    return n * m

    return n * m if n > 0 and m > 0 else 0

    return 0 if n < 0 or m < 0 else n *m

    return true if condition else false

    def make_upper_case(s):
    #receive a lowercase string
    #return an uppercase String
    
    #ex: 'jump' => "JUMP"
    #ex: 'robot' => 'ROBOT'
    
    if len(s) == 0:
        return ""
    
    upperCaseString = s.upper()
    return upperCaseString

    def abbrev_name(name):
    #input: two words with one space in between
    #return uppercase letters of the first two letters in each word
    #ex: 'santa clause' => 'S.C'
    #ex: 'Mrs Clause' => 'M.C'
    
    #split the name into two words
    #grab the firstletter in each word
    #return the firs two letters uppercase
    
    output = ''
    splitNames = name.split() #=> ['santa', 'clause']
    
#     for word in splitNames:
#         firstLetter = word[0]
#         output += firstLetter

    output = splitNames[0][0].upper() +'.' + splitNames[1][0].upper()
    return output
    
    
    return [ele*2 for ele in a]
    
    def twoNumberSum(array, targetSum):
    # receive a list of integers
    #return the two values that totals up targetSum

    #ex: [3, -1, -3, 0, 2], 0 => [3, -3]

    #create a nested loop
    #the inner j will search to see if any of the other values match
    #if target is found, return the values
    #else return empty array

    for i in range(len(array) - 1):
        for j in range(i+1, (len(array))):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []

def twoNumberSum(array, targetSum):
    #create a dictionary
    #store the value
    #find the difference
    #if difference found, return the difference and the current value
    #else store the different in the dict

    dict = {}

    for num in array:
        difference = targetSum - num
        if difference in dict:
            return [difference, num]
        else:
            dict[num] = num
    return []
    
    def next_item(xs, item):
    # receive a list of numbers or strings, item we are looking for
    #return the next item after item
    #if not found, return None
    
    #ex: [1,2,3,5,8], 9 => None
    #ex: [1,2,3,5,8], 3 => 5
    
    #iterate through the list
    #if found the item
    #return the next item afterwards
    #else return None
    
    it = iter(xs)
    for ele in it:
        if ele == item:
            return next(it, None)
    return None

    def double(list):
    #receive a list of integers
    #return a new list where the value are doubled

    #ex: [1,2] => [2, 4]
    #ex: [-3, 0, 3] => [-6, 0, 6]

    #initialize a new array
    #iterate through each value in the list
    #multiply the value by 2
    #add to the list
    #return the new list

    doubleList = []
    for ele in list:
        doubleNumber = ele *2
        doubleList.append(doubleNumber)
    return doubleList

    #list comprehension
    return [ele*2 for ele in list]

result = double([1,2])
print(result)

def each_cons(lst, n):
    #receive a list of integers and an integer
    #return the list separated into n
    
    #ex: [12,3,4,5,2,3,3], 7 => [[12,3,4,5,2,3,3]]
    
    #brute force
    #create a new list
    #iterate up to n+1 amount
    #add it to the new end of the list
    #return the new list
    
    #list comprehension
    #return n for ele in lst if len(n)
   #return [lst[ele: ele + n] for ele in range(len(lst) - n + 1)]

    newList = []
    for i in range(len(lst) - n + 1):
        newList.append(lst[i: i + n])
    return newList

    from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    #receive a linked list
    #return the node at the index
    
    #ex: 1 -> 2 -> 3 -> null, 2 => node 2
    
    #create a current pointer starting at the head
    #move until node == index
    #return current
    
    if not node or index < 0:
        raise IndexErorr("Index must be non-negative")
    
    current = node
    for i in range(index):
        current = current.next
        if current is None:
            raise IndexError("Index out of range")
    return current
  
  def twoNumberSum(array, targetSum):
    #create a dictionary
    #store the value
    #find the difference
    #if difference found, return the difference and the current value
    #else store the different in the dict

    dict = {}

    for num in array:
        difference = targetSum - num
        if difference in dict:
            return [difference, num]
        else:
            dict[num] = num
    return []
        
    def isValidSubsequence(array, sequence):
    # receive a list of integers and a list of integers
    #return true if sequence exists in list

    #e: array: [3,4,2,5,2,5]
    #ex: sequence: [4, 2, 5]
    #=> true

    #create pointers for both arrays
    #if found value in sequence list
    #increment pointer
    #else keep incrementing poitner in array
    #return true if pointer reached end of sequence's length

    seqIdx = 0

    for arrIdx in range(len(array)):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx +=1
        if seqIdx == len(sequence):
            break
    return seqIdx == len(sequence)

    def sortedSquaredArray(array):
    #receive a list of sorted integers
    #return a list of sorted integers

    #ex: [2,3,5,7] => [4, 9, 25,49]

    #brute force:
    #create an empty list
    #iterate through the list
    #add to the new list
    #return the new list sorted

    squaredList = []
    for ele in array:
        squaredNum = ele * ele
        squaredList.append(squaredNum)
        squaredList.sort()
    return squaredList

def sortedSquaredArray(array):
    result = [0] * len(array)
    left, right = 0, len(array) -1
    for i in range(len(array)-1, -1, -1):
        #if absolute value of element at left is > than abs value of right
        #the square of the left element is placed in result[i]
        if abs(array[left]) > abs(array[right]):
            result[i] = array[left] **2
            left += 1
        else:
            result[i] = array[right] **2
            right -= 1
    return result

#time: O(n)
#space: O(n)


def tournamentWinner(competitions, results):
    scores = {}
    currentBestTeam = ""
    maxScore = 0

    for i in range(len(competitions)):
        homeTeam, awayTeam = competitions[i]
        result = results[i]

        winner = homeTeam if result == 1 else awayTeam

        if winner not in scores:
            scores[winner] = 0
        scores[winner] +=1

        if scores[winner] > maxScore:
            maxScore = scores[winner]
            currentBestTeam = winner
    return currentBestTeam

def greet_developers(lst): 
    # receive a list of objects
    #return list of objects adding an additional greeting
    
    #ex: 
    
    #for every item in the list
    #add the greeting 
    #add the name and add what do you like most about "programming langue"
    #use string literals
    
    for developer in lst:
        developer['greeting'] = f"Hi {developer['firstName']}, what do you like the most about {developer['language']}?"
    return lst    

    def greet(s):
  #receive a string of lowercase letters
  #return a greeting with string passed in 

  #ex:greet('my') => 'hey my'

  return f"hey {s}"
def max_value(nums):
  #receive a list of numbers
  #return the max value seen

  #ex: [3,4,5,,2,6] => 6

  return max(nums)

  def max_value(nums):
  #receive a list of numbers
  #return the max value seen

  #ex: [3,4,5,,2,6] => 6

  #return max(nums)

  max = float('-inf')

  for num in nums:
    if num > max:
      max = num
  return max

  def make_negative( number ):
    #receive an integer
    #return the negative number
    
    #ex: 4 => -4
    #ex: 0 => 0
    
    #if num is negative, return num, else make it negative, return num
    
    return -number if number > 0 else number
    return -abs(number)

    def positive_sum(arr):
    # receive a list of integers
    #return the sum of all positive numbers
    
    #ex: [3, -3, 5, 2] => 3 + 5 + 2 => 10
    
    #iterate through list
    #check if the num > 0
    #add it to the running total
    #return total
    
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total

    return sum(num for num in arr if num > 0)

    def repeat_str(repeat, string):
    #receive an integer for repeat and a string for astring
    #return the string added up to repeat times
    
    #ex: 4, 'yo' => 'yoyoyoyo'
    
    #intialize an empty string
    #iterate up to repeat times
    #add string to the empty string
    #return the new string
    
#     repeatedString = ''
#     for num in range(repeat):
#         repeatedString += string
#     return repeatedString

    return string * repeat

    def transposeMatrix(matrix):
    # receive 2D matrix
    # retrun the matrix transpose

    #ex: [
    # [ 3, 4]
    # ]

    # => 
    #[
    # [4],
    # [3]
    # ]

    #initialize a new row
    #capture the first row
    #capture the first col in the row
    #add it in the first row
    #return the new row

    result = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        result.append(newRow)
    return result

    def threeNumberSum(array, targetSum):
    #receive a list of int, and an int for targetSum
    #return the list of triplets that add up to targetSum

    #brute force
    #do 3 inner nested loops
    #sort the answer
    #check if the answer already exists in the results
    #if not, add it in
    #if it does exist, move on to to the next
    #return result

    result = []
    for i in range(len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array)):
                if array[i] + array[j] + array[k] == targetSum:
                    answer = sorted([array[i], array[j], array[k]])

                    if answer not in result:
                        result.append(answer)
    return result

    def smallestDifference(arrayOne, arrayTwo):
    # receive two lists of different sizes
    # return one number from both list that is closest to zero

    #ex: [3, - 3, 1]
    #    [7, 8, -3]
    #=> [3, -3]

    #brute force:
    #iterate through both lists with different pointers
    #capture each pair
    #if smallest pair == or close to 0,
    #return the pair

    smallestAmt = float('inf')
    closestPair = []

    for i in arrayOne:
        for j in arrayTwo:
            diff = abs(i - j)
            if diff < smallestAmt:
                smallestAmt = diff
                closestPair = [i,j]
    return closestPair

    #time: O(N xM) = for every element in arrayOne, you're looping through all of arrayTwo elements
    #space: O(1)

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    smallestDiff = float('inf')
    pair = []
    i = 0
    j = 0

    while i < len(arrayOne) and j < len(arrayTwo):
        diff = abs(arrayOne[i] - arrayTwo[j])
        if diff < smallestDiff:
            smallestDiff = diff
            pair = [arrayOne[i], arrayTwo[j]]
                    
        if arrayOne[i] < arrayTwo[j]:
            i +=1
        else:
            j +=1
    return pair

    def threeNumberSum(array, targetSum):
    results = []
    for i in range(len(array) - 2):
        for j in range(i + 1, len(array)-1):
            for k in range(j  + 1, len(array)):
                if array[i]+ array[j]+ array[k] == targetSum:
                    triplet = sorted([array[i], array[j], array[k]])
                    
                    if triplet not in results:
                        results.append(triplet)
    return results


    def greet(name):
    #receive a string of name - one word
    #return hello (name), how are you doing today
    
    #ex: greet('my') => 'Hello, my how are you doing today?'
    #ex: greet('') => 'Hello,   how are you doing today?'
    
    #brute force
    return f'Hello, {name} how are you doing today?'

    class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #initial: use a hashmap
        #iterate through one string and save; key = letter; value = how many times seen
        #iterate through second string
        #if total gets to 0, return true

        #put both strings into hashmap
        #verify if both strings in hashmap are equal to each other

        #sorting both strings and comparing them

        #edge case: uppercase and lowercase letters, symbols
        #edge case: if one of the string is empty
        #edge case: if both strings are empty, return true b/c they are anagram

        #ex: 'car', 'card' => automatically return false

        #brute force: #ex: 'rat', 'car' => 'art' == 'acr' => false ; O(n log n) time
        #return sorted(s) == sorted(t)

        #optimized - use a hashmap:
        #print(Counter(s))
        return Counter(s) == Counter(t)
        #time: O(n + m) - worst case
        #space: O(n + m)

        def lovefunc( flower1, flower2 ):
    # receive an integer for flower1, flower2
    #return True if one of the lower has an odd and even number, else False (even & even; odd & odd)
    
    #ex: (3, 2) => True
    #ex: (2, 2) => False
    
    #brute force: 
    #if flower1 is even and flower 2 is odd, return true
    #if flower2 is odd and flower1 is even, return true
    #else return False
    
    #    flower1 = 0         1 % 2 => 
#     if flower1 % 2 == 0 and flower2 % 2 != 0:
#         return True
#     elif flower2 % 2 == 0 and flower1 % 2 != 0:
#         return True
#     else:
#         return False

    return flower1 % 2 != flower2 % 2
def hero(bullets, dragons):
    #receive an integer for bullets, integer for the dragons
    #return True if enough bullets to kill dragons, else False
    
    #ex: hero(4, 3) => False; 3 * 2 = 6
    
    #brute force:
    #if dragons * 2 < bullets, return False, else return true
    
    return True if bullets >= dragons * 2 else False

    def better_than_average(class_points, your_points):
    #receive a list of integers for class points, an integer for my ponts
    #return True if our score is better than the average score, else False
    
    #ex: [30, 50, 15], 20
    # 30 + 50 + 15/ 3
    # 95 /3 => ~31
    # 20 > 31 => False
    
    #brute force:
    #iterate through the class Point to get an average score
    #compare our points to the average score
    #return true if our poitns is > than average, else return False
    
    lengthOfClass = len(class_points)
    
    output = 0
    averageScore = 0
    for score in class_points:
        averageScore += score
    
    output = averageScore // lengthOfClass
    
    return your_points > output

    def square_sum(numbers):
    #receive a list of numbers (neg and pos)
    #return the total sum of every number squared
    
    #ex: [2, 2, 4] => 4 + 4 + 8 => 16
    
    #for every num in numbers: square it and add it to the total
    
    return sum(num**2 for num in numbers)

    def sum_array(a):
    #receive a lis tof integers
    #return the total sum
    
    #ex: [3, 5, 2] => 10
    
    return sum(a)

    def find_needle(haystack):
    # receive a list of words and strings
    #return the index position of where 'needle' is
    
    for idx, word in enumerate(haystack):
        if word == 'needle':
            return f"found the needle at position {idx}"
        
    def moveElementToEnd(array, toMove):
    # receive a list of nums, and an integer to move to the end of nums
    #return a new list where the toMove integer are all at the end

    #ex: [3,3, 2, 5,5 ],2 => [3,3,5,5,2]

    #iterate through the array
    #if num == toMove
    #push to the end

    newArray = [num for num in array if num != toMove]
    toMoveArray = [num for num in array if num == toMove]

    return newArray + toMoveArray
    #time:O(2n) => O(N)
    #spaace: O(n)

    def points(games):
    #recieve a list of string of integers
    #return total for team points which is x and not y
    
    #ex: ["3:1", "2:4"] => 3points, 0 => 3 points
    
    #initialize a total sum
    #iterate through each game
    #convert the string into num
    #if x is > y: add 3 points to sum
    #if x < y: add no points
    #if x = y, add 1 point
    #return total sum
    
    totalSum = 0
    
    for game in games:
        x,y = map(int, game.split(":"))
        if x > y:
            totalSum += 3
        elif x==y:
            totalSum += 1
    return totalSum

    def array_plus_array(arr1,arr2):
    #receive two lists
    #return the sum of two lists
    
    #ex:[2,3], [3, 4] => [5] + [7]
    
    #return sum of both lists added together
    
    return sum(arr1) + sum (arr2)
    return sum(arr1 + arr2)

    def two_sort(array):
    # receive a list of strings
    #return the first value from the sorted strings where it has 3*** between each letters
    
    #brute force:
    #sort the array 
    #grab the first word in array
    #join the word together with ***
    
    array.sort()
    firstWord = array[0]
    return '***'.join(firstWord)

    return '***'.join(min(array))

def smallestDifference(arrayOne, arrayTwo):
    # receive two lists of integers
    #return a pair of integers that are closest to 0

    #ex: [4,3], [3] => [3,3]

    #brute force
    #iterate through each element in arrayOne and arrayTwo
    #if the difference is smaller than what the currentDiff
    #update currentDiff
    #capture current pair
    #else move pointers

    smallDiff = float('inf')
    pair = []

    for num in arrayOne:
        for num2 in arrayTwo:
            diff = abs(num - num2)
            if diff < smallDiff:
                smallDiff = diff
                pair = [num, num2]
    return pair

    def smallestDifference(arrayOne, arrayTwo):
    # optimized
    #using a while loop for both
    #sort both arrays
    #move i pointer if value is greater than j
    #return pair

    arrayOne.sort()
    arrayTwo.sort()
    i = 0
    j = 0
    smallestDiff = float('inf')
    pair = []

    while i < len(arrayOne) and j < len(arrayTwo):
        diff = abs(arrayOne[i] - arrayTwo[j])
        if diff < smallestDiff:
            smallestDiff = diff
            pair = [arrayOne[i], arrayTwo[j]]

        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j+= 1
    return pair

    def mergeOverlappingIntervals(intervals):
    # receive a list of intervals
    #return a list of lists back where overlapping intervals are merged in

    #ex: [[1,2], [2, 5], [8,9]] => [[1, 5], [8,9]]

    #create a new list and add in the first interval into the list
    #iterate through each interval
    #check if the end time is < start time of second
    #else merge in list to the intervals
    #return intervals

    intervals.sort(key = lambda x: x[0])

    newInterval = [intervals[0]]

    for interval in intervals[1:]:
        start, end = newInterval[-1]
        start2, end2 = interval

        if start2 <= end:
            newInterval[-1][-1] = max(end, end2)
        else:
            newInterval.append(interval)
    return newInterval
        
def remove_char(s):
    #receive a lowercase string word
    #return a string back of first letter and last letter removed
    #ex: 'happy' => 'app'
    
    #brute force:
    #intiialize a new string
    #skip first letter
    #add each letter until the last letter
    #return new string
    
#     newString = ''
    
#     for idx, letter in enumerate(s):
#         if idx != 0 and idx != len(s) - 1:
#             newString += letter
#     return newString

    return s[1:-1]

    def basic_op(operator, value1, value2):
    #receive an operator, two integer values
    #return the sum, product, of the two values based on operator
    #ex: '*', 3, 4 => 3 * 4 => 12
    
    #brute force:
    #check if the operator is '+'
    #add the two values together
    #if '-', subtract two values
    #if '*', multiply two values
    #if '/', divide the two values
    
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    else:
        return value1 /value2

#can use the eval function
    return eval(str(value1) + operator + str(value2))

    def are_you_playing_banjo(name):
    #receive a name - lowercase and uppercase one word
    #return "{name} plays banjo" if lowercase or uppercase R, else, "{name} does not play banjo"
    
    #ex: 'robby' => 'robby plays banjo'
    #ex: 'santa' => 'santa does not play banjo'
    
    #lowercase the name
    #check if first letter of name starts with 'r'
    #return does play banjo
    #else does not play banjo
    
    lowerText = name.lower()
    
    if lowerText[0] == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

    if name[0].lower() == 'r':
        return name + "plays banjo"
    else:
        return name + " does not play banjo"
    
    def simple_multiplication(number) :
    # receive an integer (pos or neg)
    # return the product - if even, multiply by 8, else multiply by 9
    
    #ex:4 => even, multiply by 8 => 8 * 4 = 32
    #ex: -3 => odd, multiply by 9 => -3 * 9 = -27
    
    #brute force: 
    #if number is mod by 2 with no reminder, multiply number by 8
    #else, multiply number by 9
    
#     if number % 2 == 0:
#         return number * 8
#     else:
#         return number * 9

    return number * 8 if number % 2 == 0 else number * 9

    def invert(lst):
    #receivev a list of integers
    #return a list of integers back with their values inverse
    #ex: [3, 0, 4, 2] => [-3, 0, -4, -2]
    
    #brute force
    #iterate through each of the element
    #flip the signs on them
    #return them back in the list
    
    return [-ele for ele in lst]

    def smash(words):
    #receive a list of words
    #return one string with the list of words
    
    #ex: ['hello', 'its', 'Thursday'] => 'hello its Thursday"
    
    return " ".join(words)
    
    class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #receive a list of words
        #return similar anagrams in a list

        #ex: ['har','arh','hi'] => [['hi],['har','arh]]

        #iterate through the words in the list
        #sort the strings
        #add the similar words together
        #return the list back together

        anagrams = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if (sortedWord not in anagrams):
                anagrams[sortedWord] = []
            anagrams[sortedWord].append(word)
        return list(anagrams.values())

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #receive a list of integers and k for an integer
        #return a list back of the top k elements

        #keep a counter of how many elements seen
        #sort by frequency
        #return top k elements

        #bucket sort

        countNums = Counter(nums)
        return [item[0] for item in countNums.most_common(k)]

        la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

def greet(language):
    #receive a list of tuples of (language, greeting)
    #return the greeting based on the language provided
    
    #ex: 'dutch' => 'Welkom'
    
    greets = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }
    return greets[language] if language in greets

    def spiralTraverse(array):
    # receive a 2D array
    # return a list of elements going in a spiral traverse method

    #ex: [
    # [1,2,3],
    # [4,5,6]
    # ]

    # => [1,2,3,6,5,4]

    #initialize a list to empty
    #iterate through the first row on top 
    # while row has not reach the bottom and col has not reach the end
    #push in the value 
    #then incrmeent to the next row
    #then iterate far right col, go down
    #add value
    #return the list

    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startRow, endCol + 1):
            result.append(array[startRow][col])
        startRow += 1

        for row in range(startRow, endRow +1 ):
            result.append(array[row][endCol])
        endCol -= 1

        if startRow <= endRow:
            for col in range(endCol, startCol - 1, -1):
                result.append(array[endRow][col])
            endRow -= 1
            
        if startCol <= endCol:
           for row in range(endRow, startRow - 1, -1):
               result.append(array[row][startCol])
            startCol += 1
            
    return result

def get_average(marks):
    #receive a list of scores and the students average,
    #return the students average
    
    #ex: [3, 4,5, 2] / 4 => 17 /4 => 4
    
    return sum(marks) // len(marks)

def multi_table(number):
    # Receive an integer and return its multiplication table as a string
    
    output = ''
    for ele in range(1, 10 + 1):
        product = ele * number
        output += f'{ele} * {number} = {product}\n'
    return output.strip()  # Use .strip() to remove the trailing newline

def multi_table(number):
    #receive a string of an integer
    #return the multiplication table for integer
    
    #ex: 4 => 
    
    #for every number 1 - 10
    #create a n * number, then add in \n
    #return the string afterwards
    
    output = ''
    for ele in range(1, 10 + 1):
        product = ele * number
        output += f'{ele} * {number} = {product}\n'
    return output.strip()

    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))

    class Ball(object):
    #receive a ball type
    #return a class Ball with an argument type
    
    #ex:Ball() => 'regular'
    
    #if ball_object is empty, return "regular"
    #else return "the object passed in"
    
#     if not object:
#         return "regular"
#     else:
#         return "{object}"

    def __init__(self, ball_type = 'regular'):
        self.ball_type = ball_type

        def to_binary(n):
    #receive a non-negative integer
    #return an integer such that binary representation of b is same as decimal 
    
    #can convert number into bytes
    return int(bin(n)[2:])

    return int(f'{n:b}')

    def anagrams(s1, s2):
  #receive two strings
  #return true if anagrams, else false

  #ex: 'happy', 'hap' => false

  if len(s1) != len(s2):
    return False

  return sorted(s1) == sorted(s2)

  def pair_sum(numbers, target_sum):
  #receive a list of nums, and integer
  #return a tuple of index that sums up to target_sum

  #ex: [3, 2, 5, 2, 4, 1], 3 => (1, 5)

  #brute force:
  #nested loops
  #check if the value at both index = target_sum
  #return it in a tuple

  for i in range(0, len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == target_sum:
        return (i, j)

#Time: O(N ^2)
#space: O(1)

def pair_sum(numbers, target_sum):
  #receive a list of nums, and integer
  #return a tuple of index that sums up to target_sum

  #ex: [3, 2, 5, 2, 4, 1], 3 => (1, 5)

  #brute force:
  #nested loops
  #check if the value at both index = target_sum
  #return it in a tuple

  previous_nums = {}

  for idx, num in enumerate(numbers):
    difference = target_sum - num

    if difference in previous_nums:
      return (previous_nums[difference], idx)
    else:
      previous_nums[num] = idx

      def pair_product(numbers, target_product):
  #receive a list of numbers, and product sum
  #return the index of the two indices that multiplies to get product sum
  #ex: [3,2,5,1], 10 => (1,2)

  #brute force:
  #nested loops
  #check if inner value * outervalue = product sum
  #if so return the indexes in tuple

  # for i in range(0, len(numbers)):
  #   for j in range(i + 1, len(numbers)):
  #     if numbers[i] * numbers[j] == target_product:
  #       return (i,j)
  # #time: O(n^2)
  # #space:O(1)

#optimized: using a dictionary
#initialize a dictionary
#iterate through numbers
#check to find the divisor (target/ numbers)
#return index if ele exists

    previous_nums = {}
  
    for idx, ele in enumerate(numbers):
      complement = target_product / ele
  
      if complement in previous_nums:
        return (previous_nums[complement], idx)
      
      previous_nums[complement] = idx
  
  def grow(arr):
    #receive a list of integers
    #return the product of all values in the list
    #ex: [3,4, 2] => 3 * 4 * 2 => 24
    
    #brute force:
    #initialize sum to 0
    #iterate through element in the arr
    #multiply the value to sum
    #return sum
    
    
    productsum = 1
    for ele in arr:
        productsum *= ele
    return productsum

    return math.prod(arr)

    return reduce(lamda x, y:)

    def count_positives_sum_negatives(arr):
    #receive a list of integers (pos and neg)
    #return [count of pos, sum of negatives]
    
    #brute force:
    #initialize a count and sum 
    #iterate through each element in the list
    #check if it is a pos or neg
    #if pos, increment count
    #if neg, add to sum
    #return count and sum in a list
    
    if len(arr) == 0:
        return []

    if not arr: return []
    
    count = 0
    sum = 0
    for num in arr:
        if num < 0:
            sum += num
        elif num > 0:
            count += 1
    return [count, sum]

    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

    def uncompress(s):
  #receive a string of number followed by char
  #return the uncompressed version of string
  #ex: '2c' => 'cc'

  #brute force:
  #initailize an empty string
  #iterate through i and j
  #while j < string's length
  #check to see if it is in numbers
  #if so, keep moving
  #else, add on the char's amount

  i = 0
  j = 0
  num = '0123456789'
  result = ''

  while j < len(s):
    if s[j] in num:
      j += 1
    else:
      nu = int(s[i:j])
      result += s[j] * nu
      j += 1
      i = j
  return result

def uncompress(s):
  #receive a string of number followed by char
  #return the uncompressed version of string
  #ex: '2c' => 'cc'

  #brute force:
  #initailize an empty string
  #iterate through i and j
  #while j < string's length
  #check to see if it is in numbers
  #if so, keep moving
  #else, add on the char's amount

  i = 0
  j = 0
  num = '0123456789'
  result = []

  while j < len(s):
    if s[j] in num:
      j += 1
    else:
      nu = int(s[i:j])
      result.append(nu * s[j])
      j += 1
      i = j
  return ''.join(result)

  def compress(s):
  #receive a string
  #return the compressed of string

  #ex: 'aaabb' => '3a2b'

  #sort the letters
  #initalize count
  #increment count for letters seen

  sortS = sorted(s)
  count = 0
  result = ''
  i = 0
  j = 0

  while j < len(s):
    if s[i] == s[j]:
      count += 1
      j += 1
    else:
      result += f"{count}{s[i]}"
      count = 0
      i = j
  result += f"{count}{s[i]}"
  return result

  def update_light(current):
    #receive a string for a color
    #return the next color afterwards
    #'red' => 'green'
    
    #brute force:
    #3 if loops
    
    #create a list
    #if found the color, return the next color
    colorList = ['green', 'yellow', 'red']
    
#     for color in colorList:
#         if color == current:
#             return color + 1

    currentIdx = colorList.index(current)
    nextIdx = (currentIdx + 1) % len(colorList)
    return colorList[nextIdx]

    transitions = {
        'green': 'yellow',
        'yellow': 'red',
        'red': 'green'
    }

    return transitions[current]

    def double_char(s):
    #receive a string of upper, lower, chars, and spaces
    #return the string double
    #ex: 'strin ' => 'ssttrriinn. '
    
    #create a new string
    #iterate through the string
    #multiply it by 2 and add it to the string
    #then return the string
    
#     doubleCharString = ''
    
#     for char in s:
#         doubleCharString += char * 2
    
#     return doubleCharString

    doubleCharList = []
    
    for char in s:
        doubleCharList.append(char * 2)
        
    return ''.join(doubleCharList)

    return ''.join(c * 2 for c in s)
    
  