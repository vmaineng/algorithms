def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

        def get_count(sentence):
    vowels = 'aeiou'
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count
    def number_to_string(num):
    #receive a number
    # Return a string of the number here!
    
    #ex: 42 => '42'
    #ex: -5 => '-5'
    
    return str(num)

    def opposite(number):
  # receive a number
# return the opposite of the number passed in
#ex: 14 => -14
#ex: -280 => 280
    return (-number)

    def solution(string):
    #receive a string of lowercase letters
    #return the string back in reversed
    
    #ex: 'yo' => 'oy'
    #ex: 'apple' => 'elppa'
    
    #create a new string
    #iterate through string starting at the end
    #add on to the new string
    #return new string
    
    revString = ''
    for i in range(len(string)-1, -1, -1):
        revString += string[i]
    return revString

    #range(start, stop, step)
    return str[::-1]

    def bool_to_word(boolean):
    return "Yes" if boolean else "No"