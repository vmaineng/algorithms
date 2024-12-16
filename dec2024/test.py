def each_const(lst, n):
    result = []
    for i in range(len(lst) - n + 1):
        result.append(lst[i:i+n])
    return result

print(each_const([12,3,4,5,6], 2))