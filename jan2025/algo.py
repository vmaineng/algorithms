class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #receive a list of integers
        #return a list of integers multipled by everything except itself

        #ex: [3,4] => [4, 3]

        #brute force:
        #nested loops
        #if i == j, i ++
        #else keep track of the product sum
        #add it to the array integer

        result = []
        for i in range(len(nums)):
            multiplier = 1
            for j in range(len(nums)):
                if i != j:
                    multiplier *= nums[j]
            result.append(multiplier)

        return result
        
        def check_for_factor(base, factor):
    # receive two integers (whole numbers && pos) for base and factor
    # return a boolean - True if the factor is a factor of the base, else False
    
    #ex: (25, 8) => 25 % 8 => 3 => 1
    # => 8 * 3 => 24 => False

    #ex: (25, 5) => 5 * 5 => 25 => 0 => True
    
    #brute force:
    #if base % factor = 0, return true, else return false
    
#     if base % factor == 0:
#         return True
#     else:
#         return False
    return True if base % factor == 0 else False

    return base % factor == 0

    def hoop_count(n):
    # receive an integer
    #return a string of "Great, now move on to tricks", else "Keep at it until you get it"
    
    #ex: 4 => "Keep at it until you get it"
    
    #brute force:
    #if n >= 10, "Great, now move on to tricks", else "Keep at it until you get it"
    
#     if n >= 10:
#         return "Great, now move on to tricks"
#     else:
#         return "Keep at it until you get it"

    return "Great, now move on to tricks" if n >= 10 else "Keep at it until you get it"
    
    def disemvowel(string_):
    #receive a string of lowercase and uppercase and characters and spaces
    #return a string back of lowercase and uppercase and space with no vowels
    
    #ex: 'happy new year!' => 'hppy nw yr!'
    
    #brute force
    #intialize an empty string
    #iterate through each char in the string
    #check to see if it is not a vowel
    #add it to the empty string
    #else, we'll skip it if it a vowel
    #return the string
    
#     noVowelString = ''
#     vowels = 'aeiouAEIOU'
    
#     for char in string_:
#         if char not in vowels:
#             noVowelString += char
    
#     return noVowelString
    
    #time: O(N)
    #space: O(N) - noVowelString 
    
#     noVowels = string_.lower().replace(/[aeiou]/g,'')
#     print(noVowels) #javascript regex
    import re
    noVowels = re.sub(r'[aeiouAEIOU]', '', string_)
    return noVowels

    def square_digits(num):
    # receive an integer
    #return an integer - consist of the squared number of each num from the input
    
    #ex: 345 => 3^2 = 9, 4 ^2 = 16, 5^2 = 25
    #output: 91625
    
    #brute force:
    #convert num into a list
    #iterate through each num in the list
    #square each num
    #add the squared number to the list
    
    listNum = str(num)  #['9119']
    
    squaredNums = ''
    for num in listNum:
        product = int(num) * int(num)
        squaredNums += str(product)
    return int(squaredNums)
        
        class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #receive a list of integers
        #return a list of integers
        
        #ex: [3,4] => [4, 3]
          #     i
          #  j

        #brute force:
        #initialize an empty result list
        #iterate through each num in nums
        #if i != j
        #multiply to get product sum of each value at j
        #add it the list

        #ex: [1,2,3,4]
           #. i
           #.     j
        
        # result = []

        # for i in range(len(nums)):
        #     multiplier = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             multiplier *= nums[j] #2, 3 * 2 = 6
        #     result.append(multiplier) #[2, 6]
        
        # return result

        #time: O(n ^ 2)
        #space: O(1)

        #optimized method: time: O(N)
        #run one loop at a time to grab all the productSum from the left side => O(N) + O(N) => O(2n) => O(n)
        #run another loop to grab all the productSum from the right side

        #initialize an empty result
        #multiplier set to 1
        #iterate through the nums
        #multiply by the multiplier
        #then add in the products in the result list

        #create a rightmultiplier and set it to 1
        #iterate through the right side of th eproduct
        #multiply each num in the result list
        #return the result list

        #initialize a list of the same length of nums list, and set it one
        result = [1] * len(nums)

        leftMultipler = 1
        for i in range(len(nums)):
            result[i] *= leftMultipler
            leftMultipler *= nums[i]

        rightMultiplier = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= rightMultiplier
            rightMultiplier *= nums[i]

        return result

        #time: O(n)
        #space:O(n)

         anagrams = {}

        for word in strs:
            sortedWord = "".join(sorted(word))
            if (sortedWord not in anagrams):
                anagrams[sortedWord] = []
            anagrams[sortedWord].append(word)
        return list(anagrams.values())

        class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += f"{len(s)}:{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != ':':
                j += 1
            length = int(str[i:j])
            i = j + 1
            decoded.append(str[i: i+length])
            i += length
        return decoded

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #receive a string of words that contains uppercase, lowercase,
        #return True if palindrome, else False

        #ex: 'race a car' => 'racecar' => true

        #brute force:
        #modify string to all lowercase and remove the all non-alphanumeric chars
        #create another string - reverse it
        #check if the letter is the same
        #else erturn false immediately

        #optimized: using two pointer
        #filter string to no space and lowercase it
        #start one pointer at the start, and one at the end
        #while the two pointers do not overlap
        #check if they are the same letter
        #if not, then return False immediately
        #else increment both pointers
        #return true after checking

        s = ''.join(c.lower() for c in s if c.isalnum())

        left, right = 0, len(s) -1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1
                
        return True

        class Solution:
    def isPalindrome(self, s: str) -> bool:
        sLower = ''.join(c.lower() for c in s if c.isalnum())

        return sLower == sLower[::-1]
        #compares original sLower which is filtered
        #to reverse and filtered sLower

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sLower = ''.join(c.lower() for c in s if c.isalnum())

        return sLower == sLower[::-1]
        #compares original sLower which is filtered
        #to reverse and filtered sLower

        sLower = ''.join(c.lower() for c in s if c.isalnum())

        for i in range(len(sLower)):
            if sLower != sLower[::-1]:
                return False
        return True
        
        class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #receive a list of integers in non-decreasing order
        #remove duplicates in-place

        #ex: [3,4,4,4,5] => [3,4,5,_,_,_]

        #brute force:
        #iterate through nums
        #if i and j are not the same
        #move i and j pointer
        #if i an j are the same, then move the value of pointer j
        #move i to j 
        #return the nums array again

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] !== nums[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    i =j
        return nums + 1
        
    class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #receive a list of integers in sorted order
        #return a list back of unique elements in the array

        #ex: [3,4,5,5,5,6] => [3,4,5,6, _, _]

        #brute force:
        #iterate through the nums list
        #check to see if the numbers are the same at i and j
        #if they are not the same
        #keep moving, else replace i with j

        i = 0 #tracks the last unique element in the array
        for j in range(1, len(nums)): #j traverses to find the next unique element
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j] #the pointer i will overwrite the previous values
        return i + 1 #bc i is 0-indexed

        class Solution:
    def reverseVowels(self, s: str) -> str:
        #receive a string of uppercase and lowercase string
        #return the vowels reversed

        #ex: 'apple' => 'eppla'

        #brute force:
        #nested loop
        #check to see if there is a vowel


        #optimized: use two pointers
        #one starting at left and one starting at far right
        #check to see if it is a vowel
        #if so, swap them
        #else keep looking
        #return string

        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left =0 
        right = len(s) -1

        while left < right:
            if s_list[left] not in vowels and s_list[right] now in vowels:
                left += 1
                right += 1
            else:
                left += 1
                right += 1
            return s
class Solution:
    def reverseVowels(self, s: str) -> str:
        #receive a string of integers
        #return a string back with the reversed reversed

        #brute force
        #for each letter in the strings
        #if they match a vowel
        #reverse them
        
        vowels = 'aeiouAEIOU'
        vowel_list = [char for char in s if char in vowels]
        reverseVowels = vowel_list[::-1]

        result = []
        vowel_index = 0
        for char in s:
            if char in vowels:
                result.append(reverseVowels[vowel_index])
                vowel_index += 1
            else:
                result.append(char)
        return ''.join(result)

        #create a list of vowels
        #check to see if it is a vowel
        #grab a vowel from the list reversed
        #keep track of the index of it
        #then increment index of vowels used
        #return back in a string

        #time: O(n)
        #space: O(v) => v # of vowels in string

        #optimized:
        #two pointers; one at start, one at beginning
        #if it is a vowel
        #swap them
        #else, increment them

        vowels = set('aeiouAEIOU')
        chars = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] not in vowels:
                left +=1
            elif s[right] not in vowels:
                right -=1
            else:
                s[left], s[right] = s[right], s[left]
                left +=1
                right +=1
        return ''.join(chars)

        class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #receive two lists of uneven lengths
        #return a list of where they intersected

        #ex: [3,4,5,2] and [2,3,4] => [3]

        #brute force
        #create two pointers
        #check if they are the same value
        #return the value as the list
        result = set()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    result.add(nums1[i])
        return list(result)

        class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2) #using & helps find common elements
        #using & in python with sets, it performs an intersection operation
        #using & is shorthand for .intersection()
        #set1.intersection(set2)

        #time: O(m x n)
        #space: O(m x n)

        #sort both arrays
        #then iterate through each arrays
        #add it to the result set

        result = set()
        nums1.sort()
        nums2.sort()
        i,j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.add(nums[1])
                i +=1
                j +=1
            elif nums1[i] < nums2[j]:
                i +=1
            else:
                j +=1
        return list(result)
        


def high_and_low(numbers):
    # receive a string of ints
    #return max and min int in strings
    #ex: '3 5 3 3' => '5 3'
    
    #brute force:
    #turn numbers into a list
    #turn nums into ints
    #find min and max
    #return as string
    
#     minNum = float('inf')
#     maxNum = float('-inf')
    
    listNums = list(map(int,numbers.split()))
#     for num in listNums:
#         print(listNums)

    maxNum = max(listNums)
    minNum = min(listNums)
    return f"{maxNum} {minNum}"

    def high_and_low(numbers):
    numList = [int(num) for num in numbers.split(" ")]
    maxNum = max(numList)
    minNum = min(numList)
    
    return f"{maxNum} {minNum}"

     numList = [int(num) for num in numbers.split(" ")]
    
    return f"{max(numList)} {min(numList)}"

def filter_list(l):
    #receive a list of strings and nums
    #return a list of nums only
    
    return [num for num in l if isinstance(num,int)]

    # return masked string
def maskify(cc):
    #receive a string of integers
    #return the string of integers back with the first couple of nums in # with last 4 shown
    #ex: '2342342' => '###2342'
    
    #find the length of the string
    #turn it all into # and slice out -4
    
    #edge case:
    #if length of cc <4, return the card as is
    
    return (len(cc) - 4) * '#' + cc[-4:]
    def min_max(lst):
    #receive a list of integers
    #return the min and max in a list back
    
    #ex: [3,2,5,6] => [2, 6]
    
    #brute force:
    #look for min num and max num using min and math functions
    #return a list of min and max
    
    minNum = min(lst)
    maxNum = max(lst)
    return [minNum, maxNum]

    return [min(lst), max(lst)]

    def threeNumberSum(array, targetSum):
    #receive a list of integers, and a targetSUm integer
    #return the triplets that matches up to the total

    #brute force:
    #iterate through array with 3 pointers
    #add triplet to result array
    #return result array

    result = []
    for i in range(0, len(array) -2):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array)):
                if array[i] + array[j] + array[k] == targetSum:
                    triplet = sorted([array[i], array[j], array[k]])
                    if triplet not in result:
                       result.append(triplet)
    return result

#time: O(N^3)
#space: O(n) n for number of triplets stored

def threeNumberSum(array, targetSum):
    # iterate through the array with 2 pointers
    #sort teh array first
    #have a pointer start atfirst index
    #i and j moves in between
    #if they are the same, addto the result array
    #else increment i or decrement j
    #return result

    result = []
    array.sort()
    
    for i in range(0, len(array) - 2):
        j = i + 1
        k = len(array) - 1

        while j < k:
             if array[i] + array[j] + array[k] == targetSum:
                 result.append([array[i], array[j], array[k]])
                 j += 1
                 k -= 1
             elif array[i] + array[j] + array[k] < targetSum:
                 j += 1
             else:
                 k -= 1
    return result
       #time: O(n^2)
       #space:O(N)
        def findClosestValueInBst(tree, target):
    # receive a BST and a node value
    #return the node value's that is closest to target

    #ex:

    #brute force: 
    #if tree has no root node, return None
    #check if the target's value < or > than root node, so we can see if we go left or right
    #return the smallest difference
    #return the node associated with it

    if tree is None:
        return None

    min_diff = abs(target- tree.value)
    closeset_value = tree.value

    if target < tree.value:
        left_closest = findClosestValueInBst(tree.left, target)
        if left_closest is not None:
            left_diff = abs(target - left_closest)
            if left_diff < min_diff:
                closest_value = left_closest
                min_diff = left_diff
    elif target > tree.value:
        right_closest = findClosestValueInBst(tree.right, target)
        if right_closest is not None:
            right_diff = abs(target - right_closest)
            if right_diff < min_diff:
                closet_value = right_closest
                min_diff = right_diff
    return closest_value

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class Solution:
    def validPalindrome(self, s: str) -> bool:
        #receive a string of lowercase letters
        #return True if can delete at most one char from it, else False

        #ex: 'helpeh' => True

        #brute force:
        #create a new string
        #add

        #optimize:
        #iterate thorugh the strings iwwth left and right pointer
        #start at 0 and one at the end
        #if they are equal to each other, move both pointers
        #else, move one of the pointers to check if the the other letters are the same
        #increment count
        #false if more than 2 counts
        #else return true after searching all

        count = 0
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left +=1
                right -=1
            elif if s[left] != s[right]:
                count += 1
                left += 1
                right -= 1
                if count > 1:
                    return False
        return True

        class Solution:
    def validPalindrome(self, s: str) -> bool:
        #receive a string of lowercase letters with no spaces
        #return True if palindrome if removing one letter, else False

        #ex: 'abca' => True

        #brute force
        #create a new string
        #check if the reverse string is equal to the other one
        #return False if they don't
        #else, checking everything, return True

        def checkPali(string):
            return string == string[::-1]

        #check all possible single-char removals
        for i in range(len(s)):
            modifiedString = s[:i] + s[i + 1:]
            if checkPali(modifiedString):
                return True
        return checkPali(s)

        class Solution:
    def validPalindrome(self, s: str) -> bool:
        #receive a string of lowercase letters with no spaces
        #return True if palindrome if removing one letter, else False

        #ex: 'abca' => True

        #brute force
        #create a new string
        #check if the reverse string is equal to the other one
        #return False if they don't
        #else, checking everything, return True

        # def checkPali(string):
        #     return string == string[::-1]

        # #check all possible single-char removals
        # for i in range(len(s)):
        #     modifiedString = s[:i] + s[i + 1:]
        #     if checkPali(modifiedString):
        #         return True
        # return checkPali(s)

        #optimized: leeft and right

        def isPali(left, right, string):
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -=1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPali(left + 1, right, s) or isPali(left, right - 1, s)
        return True

        
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #receive the head of a SLL
        #return True if palindrome
        #else False

        #brute force: 
        #create a track of the values in a list
        #check if the reversed one is equal to it

        lst_vals = []
        current = head
        while current != None:
            lst_vals.append(current.val)
            current = current.next
        
        left, right = 0, len(lst_vals) - 1

        while left < right:
            if lst_vals[left] != lst_vals[right]:
                return False
            left += 1
            right -=1
        return True

    #time:O(n)
    #space:O(n)


def reverse_words(text):
    #receive a string of words, spaces, uppercase and lowercase
    #return the string back in reverse
    
    #ex: 'hello world' => 'dlrow olleh'
    
    #brute force:
   #split the words into a list
#iterate through the strings
#reverse them
#add it back to the list
#join together as strings
    splitText = text.split(" ")
    revWords = []
    
    for word in splitText:
        #print(word)
        revWord = word[::-1]
#         print(revWord)
        revWords.append(revWord)
    return ' '.join(revWords)
        
return ''.join([s[::-1] for s in text.split('')])
        class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #receive a list of integers
        #return a list of lists of triplets with no duplicate triplets

        #brute force
        #create a result list
        #iterate through each num in the nums list
        #check if all 3 values are equal to 0, if so,
        #check if all triplets are already in the result lsit
        #if not, add them in
        #return result list

        result = []

        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[k] + nums[j] == 0:
                        triplets = sorted([nums[i], nums[j], nums[k]])
                        if triplets not in result:
                            result.append(triplets)
        return result

        class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #optimized solution:
        #sort the list
             #create a result list
        #have a pointer that iterates through all index
        #left and right pointer
        #if the 3 values at each pointer == 0
        #add them in the result list
        #else if the values is higher than 0
        #move right pointer down, else left pointer up

        nums.sort()
        result = []

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while (left < right):
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left +=1
                    while left < right and nums[right] == nums[right - 1]:
                        right -=1
                        
                        left += 1
                        right -=1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return result

   
from collections import Counter

# write the function is_anagram
def is_anagram(test, original):
    #receive two strings of uppercase and lowercase letters
    #return True if they are anagrams of each other, else False
    
    #ex: 'hi','yo' => false
    #ex: 'alli', 'lila' => True
    
    #sort both of the values
    #compare to each other if they are of same values
    
#     sortTest = sorted(list(test.lower()))
#     sortOriginal = sorted(list(original.lower()))
    
#     return sortTest == sortOriginal
#time: O(n log n)
#space: O(n)

    return Counter(test.lower()) == Counter(original.lower())
#time: O(N)
#space:O(N)
       
       def sequence_sum(begin_number, end_number, step):
    #receive integers for being, end, and step
    #return the sum of begin - end, by the step, else return 0 if begin > end
    
    #ex: 4, 3, 1 => 0
    #ex: 2, 9, 2 => 2 + 4 + 6 + 8 => 20
    
    #if begin # > end #, return 0
    #else inititalize a sum to 0
    #increment starting at begin #, go up to end #, by step
    #add to total
    #return total
    
    if begin_number > end_number:
        return 0
    
    sum = 0
    for val in range(begin_number, end_number + 1, step):
        sum += val
    return sum

   # return [sum(val) for val in range(begin_number, end_number + 1, step)]
    return sum(range(begin_number, end_number + 1, step))
    
    def find_average(numbers):
    return sum(numbers)/len(numbers) if len(numbers) > 0 else 0

    def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    #receive integers for both for x and n
    #return a list back of numbers up 
    #return a list of back of numbers x times by n
    
    #ex: 3, 3 => [3, 6, 9]
    
    #brute force: use list comprehrension
    #add num for each num for x time
    
    return [i*x for i in range(1, n+1)]
    def check(seq, elem):
    #receive a sequence and number
    #return True if elem exists in seq, else False
    
    #ex: [42, 34, 55, 32], 32 => True
    
    #brute force:
    #iterate through to see if elem = seq, return true, else return false
    
    for ele in seq:
        if ele == elem:
            return True
    return False
    
    class Solution:
    def isPalindrome(self, s: str) -> bool:
        #receive a string of words letters and chars
        #return true if string is palidrome, else false

        #ex: 'hello, mary joe' => 'eoj yram ,,olleh' => false

        #brute force:
        #lowercase the words
        #create a reversed string of the words
        #iterate through each char
        #check if each char is not the same letter
        #else return false

        #'hello'
        #'olleh'
        #'racecar'
        #'racecar'

        revString = ''
        for idx in range(len(s)-1, -1, -1):
            revString += s[idx]

        revLower = revString.lower()
        newLower = s.lower()

        for idx in range(len(newLower)):
            
            if newLower[idx] != revLower[idx]:
                print(revLower[idx], newLower[idx])
                return False
        return True
        #optimized
        
        class Solution:
    def isPalindrome(self, s: str) -> bool:
        #brute force:
        #remove all alphanumbers and special chars, and lowercase the letters
        #check if reverse string == string
        
       # filterWord = ''.join(c.lower() for c in s if c.isalnum())
        # print(filterWord)
       # return filterWord == filterWord[::-1]

        #topimized solution:
        #lower and filtered out the word
        #using left and right pointer
        #check if char is the same as each other
        #if they are equal to each other, return false
        #else return True

        filterWord = ''.join(c.lower() for c in s if c.isalnum())

        left, right = 0, len(filterWord) - 1

        while left < right:
            if filterWord[left] != filterWord[right]:
                return False
            left += 1
            right -= 1
        return True
       
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    #receive integers for both for x and n
    #return a list back of numbers up 
    #return a list of back of numbers x times by n
    
    #ex: 3, 3 => [3, 6, 9]
    
    #brute force: use list comprehrension
    #add num for each num for x time
    
    return [i*x for i in range(1, n+1)]

    def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    #receive integers
    #return a list of n amount by x
    
    #ex: x = 2, n =3 => [2, 4, 6]
    
    return [i * x for i in range(1, n + 1)]


    def reverse_seq(n):
    #receive an integer
    #return a list of the intege back in revered
    
    #ex: 3 => [3, 2, 1]
    
    #brute force:
#     result = []
#     for i in range(n, 0, -1):
#         result.append(i)
#     return result
#time: O(N) , space: O(n)

    return [i for i in range(n, 0, -1)]

    class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #remove duplicates in place
        #override it with the next number

        #two index
        #iterate thorugh
        #check if the next value is the same value
        #then rewrite it with j's value
        #move i pointer up

        #[1,1,2]
        # i j


        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
           
        return i + 1

        class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #receive a list of sorted nums
        #return a list of nums where no duplicates
        #ex: [1,2,2,3] => [1,2,3, _]

        #solution:
        #iterate through the list with j
        #if j's value is same as i's value, update i's value to j
        #increment i pointer
        #return the array + 1

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
            nums[i] = nums[j]
        return i + 1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []

        for ele in nums:
            if ele not in result:
                result.append(ele)
                print(result)
        
        for i in range(len(result)):
            nums[i] = result[i]
        return (len(result))

   def remove_exclamation_marks(s):
    #receive a string of words
    #return a new string with no '!'
    
    #ex: 'H!i!'=> 'Hi'
    
    #brute force:
    #create a new string
    #check each char to see if it is not a !
    #add to string
    
    #list comprehension
    #join back
    
    noMarks = [char for char in s if char != '!']
    return ''.join(noMarks)

    return s.replace('!', '')     
    
    def quarter_of(month):
    #receive a month
    #return what quarter the month is in
    
    #ex: 3 => 1st
    #ex: 6 => 2
    
    #brute force:
    # 1 - 3 = 1
    # 4 - 6 = 2
    #7 - 9 = 3
    #10 - 12 = 4

    #if statements

    if month < 4:
        return 1
    elif month >= 4 and month < 7:
        return 2
    elif month >= 7 and month < 10:
        return 3
    else:
        return 4

from math import ceil

    return ceil(month /3)
    
    
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        #receive a string of lowercase chars
        #return total of good substrings in length of 3

        #ex: 'hello' => 'hel' => 1

        #solution:
        #start left and right pointer at the beginning of string
        #tell right to up to 3
        #check if it's been seen before in a set
        #add to set, else keep moving 

        count = 0

        for i in range(len(s) - 2):
            substring = s[i:i + 3]
            if (len(set(substring)) == 3):
                count += 1
        return count

        class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #receive an array of integers
        #return the max average
        #ex:

        #kadane's algo
        #slice up to k amount + 1

        maxAverage = float(-inf)

        for i in range(len(nums) - k + 1):
            subAmt = nums[i: i + k] #[1, 12, -5, -6]
            subAvg = sum(subAmt)/k
            if subAvg > maxAverage:
                maxAverage = subAvg
        return maxAverage

        #optimized solution
        currentSum = sum(nums[:k])
        maxSum = currentSum

        for i in range(k, len(nums)):
            currentSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currentSum)
        return maxSum/k
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #receive a string of chars
        #return max # vowels seen in s with k size

        #ex: 'hello', 2 => 1 'he', 'lo'

        #brute force:
        #keep count
        #iterate through strings
        #check if strings contains vowels
        #increment vowel count
        #if vowel count exceeds max count, max count = vowel Count
        #return maxCount

        maxCount = 0
        vowelCount = 0
        vowels = ['a','e','i','o','u']

        for i in range(len(s) - k + 1): 
            subStr = s[i:i+k]
            vowelCount = 0
            for char in subStr:
                if char in vowels:
                    vowelCount += 1
            maxCount = max(maxCount, vowelCount)
        return maxCount

        #time:O(n x k)
        #space:O(1)
        
        #optimized: 
        vowels = {'a', 'e', 'i','o','u'} #set
        maxCount = 0
        currentCount = 0

        for i in range(k):
            if s[i] in vowels:
                currentCount += 1

        maxCount = currentCount

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                currentCount -=1
            if s[i] in vowels:
                currentCount += 1
        maxCount = max(maxCount, currentCount)

        return maxCount

        class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #receive a list of integers
        #return min size array whose sum = target
        #ex: [3,4,5,11, 3], 9 => [4,5]

        #keep track of size
        #iterate through the array
        #if total > target, reduce window size, else expand window size
        #return min size window seen

        minWindow = 0
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    minWindow = [nums[i], nums[j]]
                elif nums[i] + nums[j] < target:
                    j += 1
                else:
                    i +=1
        return len(minWindow)

        minWindow = float('inf')
        current = 0
        currentSum = 0 

        for end in range(len(nums)):
            currentSum += nums[end]

            while currentSum >= target:
                minWindow = min(minWindow, end - current + 1)
                currentSum -= nums[current]
                current += 1
        return minWindow if minWindow != float('inf') else 0

def get_grade(s1, s2, s3):
    #receive 3 integers
    #return the letter grade of the average of the 3 integers
    
    #ex: (100,100,100) => 100
    
    # calc average
    #dictate where average exists
    #then return the letter grade
    
    total = s1 + s2 + s3
    
    avg = total/3
    print(avg)

    avg = sum([s1,s2,s3])/3
    
    if avg >=90 and avg <= 100:
        return 'A'
    elif avg >= 80 and avg < 90:
        return 'B'
    elif avg >= 70 and avg <80:
        return 'C'
    elif avg >= 60 and avg < 70:
        return 'D'
    else:
        return 'F'
    
    def sum_mix(arr):
    #receive a list of nums and strings
    #return the sum as nums and strings
    
    return sum([int(num) for num in arr])
    return sum(map(int, num))

    def set_alarm(employed, vacation):
    #receive booleans
    #return True if both inputs do not match each other
    
    #if employed is True and vacation is True, return false
    #if employed is False and vacation is True, return False
    
    if employed == True and vacation == False:
        return True
    else:
        return False

return employed and not vacation
#return True and opposite of what vacation is

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #receive a list of integers
        #return a list back of integers that occurs most frequent

        numsFreq = Counter(nums)

        return [item for item,count in numsFreq.most_common(k)]

#Time: O(n + logk)
#space: O(N)

def greet(language):
    #receive a language
    #return the 'welcome' of that specific language
    #ex: 'english' => 'Welcome'
    #ex: 'polish' => 'Witamy'
    
    #ex: 'EngliSH' => 
    
    languageLower = str(language).lower()
    
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
        'welsh': 'Croeso',
    }
    
    return greets[languageLower] if languageLower in greets else 'Welcome'
   
    #time: O(1)
    #space: O(1)

    return  {
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
        'welsh': 'Croeso',
    }.get(language, 'Welcome')

    def get_char(c):
    #input: ascII number
    #return the corresponding letter with it
  # {65, 'A'}
    return chr(c)
    #will return the letter back from integers

    class Solution:
    def isPalindrome(self, s: str) -> bool:
        #palindrome => 'racecar'
        #receive a string of uppercase, lowercase, spaces, and special chars
        #return True if valid palindrome, else False

        #ex: 'apples are Fall1ng' => 'applesarefall1ng' => False
        #ex: 'rumpp mur' => 'rumppmur' = True

        #brute force:
        #remove all white spaces and non-alphnumeric characters
        #joinit all together into one big word
        #check if the reversed word = the same word

        # reversedString = ''.join([char.lower() for char in s if char.isalnum()])
        # return reversedString == reversedString[::-1]

        #time: O(n)
        #space: O(n)

        #optimized: using left and right pointers
        #modified input string
        #left and right pointers (left starts at beginning, right starts at the end)
        #check to see if the letters are the same, 
        #if they are, move pointers down
        #else return false
        #after checking everything, return True

        modifiedString = ''.join([char.lower() for char in s if char.isalnum()])
        left, right = 0, len(modifiedString) - 1

        while left < right:
            if modifiedString[left] == modifiedString[right]:
                left += 1
                right-=1
            else: 
                return False
        return True

        #time:O(n)
        #space:O(n)

        class Solution:
    def validPalindrome(self, s: str) -> bool:
        #receive a string of lowercase letters with no spaces
        #return True if palindrome if removing one letter, else False

        #ex: 'abca' => True

        #brute force
        #create a new string
        #check if the reverse string is equal to the other one
        #return False if they don't
        #else, checking everything, return True

        # def checkPali(string):
        #     return string == string[::-1]

        # #check all possible single-char removals
        # for i in range(len(s)):
        #     modifiedString = s[:i] + s[i + 1:]
        #     if checkPali(modifiedString):
        #         return True
        # return checkPali(s)

        #optimized: leeft and right

        def isPali(left, right, string):
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -=1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPali(left + 1, right, s) or isPali(left, right - 1, s)
        return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        #receive a string of lowercase English characters
        #return true if valid palidrome after deleting at monst one character
        #else return False

        #ex: 'abca' => True

        #edge cases: '' => True
        #'a' => True

        #brute force:
        #look at the reversed string

        #optimized method:
        #left and right pointer
        #skip the characters
        #do the rest of the check

        def isValid(self, left: int, right: int, string:str) -> bool:
            while left < right:
                if string[left] == string[right]:
                    left+= 1
                    right -=1
                else:
                    return False
            return True
#'abc'
#l. r
        left, right = 0, len(s) -1

        while left < right: 
            if s[left] == s[right]:
                left += 1
                right -=1
            else: 
                return isValid(self, left + 1, right, s) or isValid(self, left, right - 1, s)
        return True

def declare_winner(fighter1, fighter2, first_attacker):
    # fighter 1 and fighter 2 are objects, who attacks first
    #within the fighter objects, "name", int (health), int(damage)
    
    #return: string of the winner
    
    #ex: Lew 10.    Harry 5
        #1st             -2
        #                 3
        #2nd -4
        #.    6
        #3rd             -2
        #                 1
        #4th  -4
        #     2
        #5th              -2
        #                  -1
        #Lew is still alive
        
        #let's figure out who goes first
        #deduct damage_per_attack from other person's health
        #the other fighter attacks, deducts attack from their person's health
        #check if the health <=0, return the other fighter's name
        
        if first_attacker == fighter1.name:
            while fighter1.health > 0 and fighter2.health >0:
                fighter2.health -= fighter1.damage_per_attack
                fighter1.health -= fighter2.damage_per_attack

                return fighter1.name if fighter1.health >0 else fighter2.name

        else: #fighter2's turn
            while fighter1.health > 0 and fighter2.health >0:
                fighter1.health -= fighter2.damage_per_attack
                fighter2.health -= fighter1.damage_per_attack
                
                return fighter2.name if fighter2.health >0 else fighter1.name
    

        def mystery():
    results = {'sanity': 'Hello'}
    return results

    def two_decimal_places(n):
#     raise NotImplementedError("TODO: two_decimal_places")
    #receive an floating number
    #return the number rounded to decimal places
    
    #ex: 3.2349723987 => 3.23
    #ex: -38427.9827 => -38427.99
    
    return round(n, 2)