#friend or foe
#filters a list of strings

#if name has 4 letters == friend, else foe

#input = a list of strings
#output = a list of strings that are friends that has a length of 4
#ex: ['Mai', 'Kyle', 'Eric', 'Amanda'] => [ 'Kyle', 'Eric' ]

#[] => []
#[34, ] => always be strings only
#['Mai']
#with names longer than 4=> []

#initalize an empty list
#iterate through the input string
#check the length of name == 4
#add it to our empty list
#return the result list of names == 4

def friendOrFoe(array):
    result = []
    for name in array:
        if len(name) == 4:
            result.append(name)
    return result

# print(friendOrFoe(['Mai', 'Kyle', 'Eric', 'Amanda']))
# print(friendOrFoe(['Mai', 'Kye', 'Ric', 'Amanda']))

def sheepCount(array):
    # count = 0
    # for sheep in array:
    #     if sheep == True:
    #         count += 1
    # return count 
    return sum(sheep is True for sheep in array)

print(sheepCount([True, False, False]))


