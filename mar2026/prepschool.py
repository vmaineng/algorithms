#function that filters out string, returns list of friends name in it
#if name has 4 letters, name is friend otherwise they are not

#receive a list of strings
#return back a list of our friends whose length is only 4
#'Mark'
#receive only alphabetical letters
#array will never be empty

#ex: ['Mai', 'Mark', 'Amanda'] => ['Mark]

#initialize an empty array that will hold the answer
#iterate through all of names
#check the length == 4, add the name to the list
#return result

#time: O(n) #n 
#space: O(n)

def findFriends(array):
    result = []
    for name in array:
        if len(name) == 4 or len(name) == 6:
            result.append(name)
    return result

# print(findFriends(['Mai', 'Mark', 'Amanda']))

def addList(array): 
    result = []
    for idx, item in enumerate(array):
        result.append(f"{idx + 1}")
        result.append(":" + item)
    return result
print(addList(['a','b','d']))
