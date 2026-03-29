
#receive a string
#return middle char
#ex: 'hello' => 'l'

#iterate with two pointers
#first one starts at beginning
#second pointer starts at end
#keep decrementing down until pointers match each other


def findMiddle(str):
    i = 0
    j = len(str) - 1

    while i <= j:
        i += 1
        j -= 1
        if len(str) % 2 == 0:
            return str[i] + str[j]
        else:
            return str[i]


    # mid = len(str) // 2

    # if len(str) % 2 == 0:
    #     return str[mid -1] +str[mid]
    # else:
    #     return str[mid]


# print(findMiddle('hello'))
# print(findMiddle('race'))




#summation
#find the summation of every number from 1 to number given
#number is postive and > 0


#receive a postive whole integer > 0
#return the sum of every number up to number
#ex: 1 => 1
#ex: 5 => 5 + 4 + 3 + 2 +1 => 15

#iniitalize a total set to 0
#iterate up to number given
#add it all up total
#return the total

def summation(num):
    total = 0 # 0 
    for number in range(0, num + 1): #(0, 1)
        total += number #0, #1
    return total #1

print(summation(1))
print(summation(5))

def duck_duck_goose(players, goose):
    #receive a list of strings, and an integer
    #return the name of the player where goose lands on
    #ex: [3, 4, 2], 6 => 2
    
    #take len of players
    #return name 
    
    name = (goose- 1) % len(players) 
    return players[name].name

def if_chuck_says_so():
    return 'apple' == 'orange'
def min_value(digits):
    #receive a list of integers
    #return smallest number that can be formed from these digits
    #ex: [3, 25, 1] => 1253
    
    #could iterate through every possbilities
    #that'd take O(n) time with O(n) space
    
    #use a set for the digits to get unique numbers and remove duplicates
    #iterate through every number, 
    #check if the number is less than the next one
    #if they aren't, swap them, 
    #return the number back together
    
    unique = set(digits)
    sortUnique = sorted(unique)
    total = ''
    
    for num in sortUnique:
        total += str(num)
    return int(total)
        
    def min_value(digits):
    #receive a list of integers
    #return smallest number to be formed with the digits
    #ex: [3, 5, 2] => 235
    
    #create a set of digits
    #sort them from smallest to biggest
    #add them back together as a string
    #return an integer
    
    uniqueDigits = sorted(set(digits))
    total = ''
    for num in uniqueDigits:
        total += str(num)
    return int(total)
            
    
    
    