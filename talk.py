#recursion:

#base case (function will exit):
#empty lists, 
#recursive case: (calls itself): call the function with a different argument


def countdown(n): 
    #receive an integer
    #return the integers printed out

    #ex: 5, output: 5, 4, 3, 2, 1

    #print out the integer
    #call the function on the number before it

    #base case: if n == 0: return 

    if n == 0:
        return 
    print(n) #5, 4
    return countdown(n - 1) # 5- 1 = 4, # 4-1 3
# countdown(5)
#time: O(n), space: O(n)

def sumlist(lst):
    #receive a list of integers
    #return the total sum of integers
    #ex: [2, 3, -3, 5,7] => 14
    #sum: 2 + [3, -3, 5, 7]
    #sum: 2+ 3 + [-3, 5, 7]

    #base case: if length of array is empty: return 
    #add each number to the total from each function call

    if len(lst) == 0:
        return 0
    return lst[0] + sumlist(lst[1:])
    
print(sumlist([2, 3, -3, 5,7]))

#time: O(n^2) ; space: O(n)