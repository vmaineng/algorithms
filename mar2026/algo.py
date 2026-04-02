def array_madness(a,b):
    #receive two list of integers
    #return boolean if squared list of a > squares list of b
    
    #find the sum squares of a
    #find the sum squared of b
    #return if  a > b
    
    squared_a = sum([num ** 2 for num in a])
    squared_b = sum([num ** 3 for num in b])
    
    print(squared_a, squared_b)
    
    return squared_a > squared_b

def fizzbuzz(n):
    #receive an integer
    #return a list back
    #ex: 
    
    
    #initialize an empty list
    #iterate up to n
    #check if % 3 and 5 => FizzBuzz
    #check if 3 => Fizz
    #if 5, buzz
    #else add in num 
    
    result = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            result.append('FizzBuzz')
        elif num % 5 == 0:
            result.append('Buzz')
        elif num % 3 == 0: 
            result.append('Fizz')
        else:
            result.append(num)
    return result