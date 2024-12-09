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
    
    output = []
    for friend in x:
        if (len(friend)) == 4:
            output.append(friend)
    return output