def charAccum(str):
    #receive a string of chars
    #return the chars
    #ex: 
    result = []
    for idx, char in enumerate(str):
        
        result.append(char * (idx + 1))
        
    return '-'.join(result)

# print(charAccum('abc'))


def weighsMore(str1,str2):
    #take the first num // second num
    #see which one out weighs the other
    #ex: ('1:3','1:2')

    totalOne = int(str1[0]) // int(str1[2])
    totalTwo = int(str2[0]) // int(str2[2])

    return True if totalOne > totalTwo else False
print(weighsMore('1:3','1:2'))