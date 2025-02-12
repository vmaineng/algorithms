def compress(s):
    # receive a string of lower and upper letters
    # return the compressed vversion of a string
    # ex: 'aaabba' => '4a2b'

    # create a list
    # push in count of letters seen
    # else start new and refresh count

    #brute force:
 
    if not s:
        return ""

    # result = []
    # count = 1

    # for i in range(len(s) - 1):

    #     if s[i] == s[i + 1]:
    #         count += 1
    #     else:
    #         result.append(f"{count}{s[i]}")
    #         count = 1
    # result.append(f"{count}{s[-1]}")

    # return "".join(result)

    s += '!'
    result = []
    i = 0
    j = 0

    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            if num == 1:
                result.append(s[i])
            else:
                result.append(str(num))
                result.append(s[i])
            i = j
    return ''.join(result)


print(compress('aaabb'))
