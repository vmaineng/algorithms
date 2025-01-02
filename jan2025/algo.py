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
    