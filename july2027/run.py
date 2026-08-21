def findNums(array):
    #receive a list of non-negative int and strings
    #return int only

    return [num for num in array if isinstance(num, int)]

# print(findNums([2, "2"]))


def pantagram(string):
    seen = set()

    for char in string.lower():
        if char not in seen:
            seen.add(char)

        if len(seen) == 26:
            return True
    return False

# print(pantagram("The quick brown fox jumps over the lazy dog"))


#check if string has same amount of x's and o's
#P: string a of x's and o's (upper and lower and could contain other alpha characters)
#r: true if equal amount of x's and o's, else False
#ex: 'AxOdXo' => x: 2, o: 2 => 2 == 2 => True
#ex: 'xOo' => x: 1, o:2 => False

#iterate through the string
#keep track of the count of x and o
#compare our totals to see if they == each other, return True, else False

def countXO(str):
    x = 0
    o = 0

    for char in str.lower(): #x = 1, o = 2
        if char == 'x':
            x += 1
        elif char == "o":
            o +=1

    return x == o #1 == 2 => False

print(countXO('AxOdXo')) 
print(countXO('xOo'))