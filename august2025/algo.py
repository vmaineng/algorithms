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