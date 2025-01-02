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
        