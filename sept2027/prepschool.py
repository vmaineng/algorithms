#splits a string into strings of two chars into array
#if string contains odd, missing second char will have an underscore it

#parameter:can be lowercase or uppercase characters, no spaces
#return: a list of two chars, but if it's odd, then the second char will have underscore
#ex: 'hello' => ['he', 'll', 'o_']
#ex: 'star' => ['st', 'ar']
#ex: ''=> []

#at least one character

#iterate word
#calc even or odd for the string,
#concat '_' at the end of the last digit if odd
#create an empty string; slice up to two characters at the same time
#add in two characters at a time
#push in the pair in the final result

# if len(word) % 2 == 0
#'a'

def splitPairs(word): 
    result = []

    if len(word) % 2 != 0:
        word = word + '_'

    for idx in range(0, len(word), 2): #hello_
        pair = word[idx: idx+2] #'he', 'll', 'o_'
        result.append(pair) #['he', 'll', 'o_']

    return result

# print(splitPairs('hello'))
# print(splitPairs('star'))
        
#check to see if string has same amount of x's and o's
#return boolean
#

def checkXO(word):
    word = word.lower()
    return word.count('x') == word.count('o')

print(checkXO('xoo1bco'))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def valid(self, node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        
        return self.valid(node.val, left, right) and self.valid(left, node.val, right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #receive the root node of a tree
        #return boolean

        return self.valid(root, float("-inf"), float("inf"))

        