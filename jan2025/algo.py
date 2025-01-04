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
