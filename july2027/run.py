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

print(pantagram("The quick brown fox jumps over the lazy dog"))