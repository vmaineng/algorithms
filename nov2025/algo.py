def to_csv_text(array):
    #receive a list of list
    #return a string back
    
    #splitlines the list
    #and add together
    
    #add it into one list
    #for each row, convert number to a string and join with a comma
    #join back with a string and a \n
    
    csv_rows=[]
    for row in array:
        csv_rows.append(','.join(map(str,row)))
    return '\n'.join(csv_rows)

def to_csv_text(array):
    #receive an array
    #return a string back of new items
    
    #create a new empty list
    #iterate through the rows in array
    #convert them into a string
    #return it joined back with csv
    
    csv_rows = []
    for row in array:
        csv_rows.append(','.join(map(str, row)))
    return '\n'.join(csv_rows)

    def contamination(text, char):
    #receive a string of lowercase letters, numbers, and a string char
    #replace the text with chars
    
    #ex: 'hello', 'z' => 'zzzzz'
    
    #initialize an empty list
    #iterate through each char
    #replace each text with char
    #return new string
    
    new_word = []
    for letter in text:
        new_word.append(char)
    return ''.join(new_word)

def calculator(x, y, op):
    #receive two numbers and a string of operations
    #return the output from x & y based off of operations
    
    #ex: 4, 2, '+' => 4 + 2 => 6
    #ex 8,4, '/' => "unknown vaue"
    
    if x == str(x) or y == str(y):
        return "unknown value"
    
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x /y
    else:
        return "unknown value"
    

    def rain_amount(mm):
    if (mm < 40):
         return f"You need to give your plant {abs(mm - 40)}mm of water"
    else:
         return "Your plant has had more than enough water for today!"
    

    def sakura_fall(v):
    #receive an integer, ensure it is positive
    #return total time for petal to reach ground
    #ex: travels 5 cm/s, and it is 80 secs
    #ex: 10cm/s, now it's 40 secs
    
    new_cm = v /5
    return 80 / new_cm if v > 0 else 0
    
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #receive an array of integers and an integer number target
        #return the position of two numbers

        #ex: [4,3, 1, 0], 1 => [2, 3]

        #iterate through the numbers for one loop
        #continue a second iteration while having first pointer stay one value
        #check to see if two values at index positions are equal to target
        #return the index position
        #else, return [-1, -1] and not found

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [ -1, -1]
        

        #time: O(n^2) due to using two inner for loops
        #space: O(n) for n in nums

        obj = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in obj:
                return [obj[difference], i]
            else:
                obj[nums[i]] = i
        return [ -1, -1]