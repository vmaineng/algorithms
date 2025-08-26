import math

def nearest_sq(n):
    #receive an integer - pos or negative
    #return the next closest perfect square
    #ex: 44 => 49
    
    #take the square root of n
    #round the square root
    #**2 to find the perfect square
    
    squareRoot = math.sqrt(n)
    roundNum = round(squareRoot)
    return roundNum**2

#time: O(1) => computing one number
#space: O(1) => returning a number
    
    def get_drink_by_profession(param):
    #receive a string of letters
    #return the corresponding output from the input
    
    #ex: 'schOOL counsElor' => 'Anything with Alcohol'
    
    #brute force with if-else statement
    #check the params.toLowerCase == 'jabroni' => return 'Patron Tequila'
    #repeat for the rest of the items
    
    
    #optimized way => capture the following inputs and outputs in an object
    
    drinks = { 
    'jabroni': 'Patron Tequila',
        'school counselor': "Anything with Alcohol",
        'programmer': "Hipster Craft Beer",
        'bike gang member': "Moonshine",
        'politician': "Your tax dollars",
        'rapper': 'Cristal',
    }
    
#     return drinks[param.lower()] if drinks[param.lower()] else "Beer"
    return drinks.get(param.lower(), "Beer")

class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        count = 0
        left = t - 3000

        for request in self.requests:
            if request >= left:
                count += 1
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

#receive recent requests
#intiailize a counter with 0 recent requests
#

from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)

        while self.requests[0] < t-3000:
            self.requests.popleft()
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

#receive recent requests
#intiailize a counter with 0 recent requests
#

def seats_in_theater(tot_cols, tot_rows, col, row):
    #receive positive integers
    #return the amount of seats available behind you and in your col or the left
    
    #ex:
    #sitting in col 5 and row 3
    #total cols =16-5 + 1 = 12 - inclusive of the cols
    #total rows = 11 -3 = 8 - exclusive
    
    # 12 * 8 = 96
    
    remainingCols = tot_cols - col + 1
    remainingRows = tot_rows - row
    
    return remainingCols * remainingRows

def check_exam(arr1,arr2):
    #receive two list of same equal length and not empty of lowercase string letters
    #return the score, integer, of each student's answer
    
    #first list = answer
    #second list = student's answer
    
    #iterate through each student's answer, 
    #compare it to the answer list
    #if same letter, +4 b/c it's correct
    #if not the same letter, -1,
    #if it is blank, +0
    #check the final score, if it is less than 0, return 0
    
    score = 0
    firstIdx = 0
    
    for idx,char in enumerate(arr2):
        if arr1[firstIdx] == char:
            score += 4
        elif char == "":
            score += 0
        elif arr1[firstIdx] != char:
            score -= 1
#         print(score, firstIdx, idx)
        firstIdx += 1
    return 0 if score < 0 else score

#time: O(n)
#space: O(1)
  

    
    def check_exam(arr1,arr2):
    #receive two list of same equal length and not empty of lowercase string letters
    #return the score, integer, of each student's answer
    
    #first list = answer
    #second list = student's answer
    
    #iterate through each student's answer, 
    #compare it to the answer list
    #if same letter, +4 b/c it's correct
    #if not the same letter, -1,
    #if it is blank, +0
    #check the final score, if it is less than 0, return 0
    
    score = 0
    firstIdx = 0
    
    for char in arr2:
        if arr1[firstIdx] == char:
            score += 4
        elif char == "":
            score += 0
        elif arr1[firstIdx] != char:
            score -= 1
#         print(score, firstIdx, idx)
        firstIdx += 1
    return 0 if score < 0 else score

#time: O(n)
#space: O(1)
  

  def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def mod(a, b):
    return a % b

def exponent(a, b):
    return a**b

def subt(a, b):
    return a - b

    def solve(s):
    #receive a string of characters - lower and upper
    #return the word either lowercase or uppercase back
    #ex: 'COde' => 'code'
    #ex: 'CODe' => 'CODE'
    
    #keep track of uppercase and lowercase letters in the string
    #if uppercase > lowercase,
    #return the word as upppercase
    #else if uppercase < lowercase,
    #return the word as lowercase
    #else ==, return the word as lowercase
    
    lowercaseChars = 0
    uppercaseChars = 0
    
    for char in s:
        if char == char.upper():
            uppercaseChars += 1
        else:
            lowercaseChars += 1
    return s.upper() if uppercaseChars > lowercaseChars else s.lower()
    
    # Create the combine_names function here
def combine_names(firstName, lastName):
    return f"{firstName} {lastName}"

    return ' '.join(args)

def max_multiple(divisor, bound):
    #receive two positive integers > 0
    #return the largest N that is divided by the divisor and <= bound
    #ex: 2, 24 => 24/2 => 12 => 24
    
    #check if bound % divisor has no remainder, return bound, 
    #floor it down, and multiply it by the divisor
    
    if bound % divisor == 0:
        return bound
    else:
        #print((bound // divisor) )
        return (bound // divisor) * divisor
    
    return bound - (bound % divisor)
    
    def sort_array(source_array):
    #receive a list of integers - pos and neg
    #return the list with only odds sorted
    #ex: [3,2,8,9,5] => [2, 3,5, 8,9]
    
    #brute force: 
    #initialize an empty list
    #do two pointers with a nested loop
    #check to see if the integer is an odd,
    #if so, check the integer before if it is odd 
    #if it is, check to see if their order is correct
    #else, it is even, then we can leave in place
    #return the list back
    
#     sortedOddList = []
    
#     for i in range(len(source_array)):
#         for j in range(1, len(source_array)):
#             if source_array[j] % 2 != 0:
#                 if source_array[i] % 2 != 0:
#                     if source_array[j] < source_array[i]:
#                         sortedOddList.append(source_array[j])
#             else:
#                 sortedOddList.append(source_array[i])
#     return sortedOddList

    #optimized with two pointers
    #intiialize a left pointer at the beginning, and a right pointer at the end of the list
    #while the two pointers do not meet
    #check if they are odd nums
    #if they are odd, check if they are in the right order
    #if not, swap them, else we can leave as-is
    #return the list back
    
#     left = 0
#     right = len(source_array) -1
    
#     while left < right:
#         if source_array[left] % 2 != 0 and source_array[right] % 2 != 0:
#                 if source_array[right] < source_array[left]:
#                     source_array[left], source_array[right] = source_array[right], source_array[left]
#                     left += 1
#                     right -=1
# #         left += 1
# #         right -=1
#     return source_array
    odds = sorted([x for x in source_array if x % 2 != 0])
    
    odd_idx = 0
    result = []
    
    for num in source_array:
        if num % 2 != 0:
            result.append(odds[odd_idx])
            odd_idx += 1
        else:
            result.append(num)
    return result
            
            class Sleigh(object):
    def authenticate(self, name, password):
        #receive a name and a password, 
        #return true if 'Santa Claus', else false
        #ex: 'San, 'Ho Ho Ho!' => False
        
        if name == 'Santa Claus' and password == "Ho Ho Ho!":
            return True
        else:
            return False
    return name == 'Santa Claus' and password == 'Ho Ho Ho!'

def digits(n):
    # your code here
    #receive a n integer
    #return total number in integer
    
    return len(str(n))

from collections import Counter

def comp(array1, array2):
    #receive two list of integers
    #return True if b elements are squared products of a
    
    #edge case: if length of two lists are different, return False
    
    #iterate through list1
    #check if squared product does not exist, return False
    #else, increment to the next one
    #return True after checking everything
    
    if array1 is None or array2 is None:
        return False
    if len(array1) != len(array2):
        return False

    
#     return sorted([x**2 for x in array1]) == sorted(array2)

#     return Counter([x**2 for x in array1]) == Counter(array2)
    
#     i = 0
    
#     for num in array2:
#         if array1[i]**array[
#     for num in array1:
#         print(num)
#         squaredNum = num * num
#         if squaredNum not in array2:
#             return False
#     return True

def converter(mpg):
    #receive an integer that is postive in mile /imperial gallon
    #return the km/ liters
    
    #ex: 10
    #miles / imperigal gallon => 10 miles / 
    
    #ex: 1 mpg => 1.609344/4.54609188
    
    kilo = 1.609344 
    litres = 4.54609188
    return round((kilo/litres) * mpg,2)

def in_asc_order(arr):
    # random_ is not allowed 
    #(True or false)
    #receive a list of postive integers - could start at 0 or 1
    #return boolean if it is sorted from smallest to biggest
    
    #ex: [1,4,5] => [1,4, 5] => True
    #brute force:
    #compare the list to a sorted version of it
#     print(arr, sorted(arr))
    return arr == sorted(arr)

    #time: O(n log n)
    #space: O(n)
    
    #optimized: 
    #ex: [8, 1,6,3] => 
    #first round: [3, 1,6,8]
    
    def tower_builder(n_floors):
    #receive an integer
    #return a list of strings of stars down by the odd level
    #ex: 4:
    #[ '*',
    # '***',
    # '*****',
    # '*******'
    #]
    
    #edge cases: if the integer for floors is negative or even 0, return an empty list
    
    if n_floors < 1:
        return []
    
    #initialize an empty list
    #initialize an empty string to hold stars to the length of n_floors * 2 -1
    
    #iterate up to n_floors
    #if num == 0, add in *, append into the list
    #else, add in two extra stars, append into the list
    #return the list
    
    towerList = []
    starStrLen = n_floors * 2 - 1
    
    for num in range(n_floors):
        countStars = (num * 2) + 1
        num_spaces = (starStrLen - countStars) // 2
        print(num_spaces)
        current_floor = " " * num_spaces + "*" * countStars + ' ' * num_spaces
        towerList.append(current_floor)
    return towerList


            
    
    
    
    
    
    #initialize an empty list
    #initialize an empty string
    #iterate up to n_floors,
    #add two stars to the list
    
#     towerStars = []
#     stringStars = ''
    
#     for num in range(1, n_floors):
#         if num == 1:
#             stringStars = '*'
#             towerStars.append(stringStars)
#         elif num > 1:
#             stringStars += '**'
#             towerStars.append(stringStars)
#     return towerStars
    
    """Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(min_in_oven):
    """Calculate the bake time remaining.

    :param min_in_oven: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).
    """
    return EXPECTED_BAKE_TIME - min_in_oven
 

#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the number of minutes making each layer remaining.

    :param number_of_layers: 2* number_of_layers to make
    :return: 2 * number of layers 

    Function that takes in the layers needed for the lasagna as
    an argument and returns how many minutes to make the layers for the entire lasagna
    based on the `number_of_layers`.
    """

    MINS_PREPARATION = PREPARATION_TIME * number_of_layers
    return MINS_PREPARATION


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    
    """Calculate the total number of minutes cooking in the kitchen

    :param number_of_layers, elapsed_bake_time:
    :return: elapsed_bake_time - (number of Layers * 2)

    Function that takes in the layers needed for the lasagna and the number of minutes spent cooking already as
    an argument and returns total minutes spent layering and baking in the oven
    based on the `number_of_layers` and `elapsed_bake_time`.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

import re

def validate_usr(username):
    #receive a string of characters => lowercase and uppercase
    #return boolean if lowercase numbers and underscore and between len of 4-16
    pattern = r"^[a-z0-9_]{4,16}$"
    
    if re.fullmatch(pattern,username):
        return True
    else:
        return False