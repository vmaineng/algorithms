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