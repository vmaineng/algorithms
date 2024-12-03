fhand = open('dec2024/algo.py')
try:
    count = 0
    for line in fhand:
        count = count +1
        print('Line count:', count)
finally:
    fhand.close()