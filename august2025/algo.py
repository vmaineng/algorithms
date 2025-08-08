import math

def nearest_sq(n):
    #receive an integer - pos or negative
    #return the next closest perfect square
    #ex: 44 => 49
    
    #take the square root of n
    #round the square root
    #**2 to find the perfect square
    
    squareRoot = math.sqrt(n)
    roundNum = round(squareRoot)
    return roundNum**2

#time: O(1) => computing one number
#space: O(1) => returning a number
    
    def get_drink_by_profession(param):
    #receive a string of letters
    #return the corresponding output from the input
    
    #ex: 'schOOL counsElor' => 'Anything with Alcohol'
    
    #brute force with if-else statement
    #check the params.toLowerCase == 'jabroni' => return 'Patron Tequila'
    #repeat for the rest of the items
    
    
    #optimized way => capture the following inputs and outputs in an object
    
    drinks = { 
    'jabroni': 'Patron Tequila',
        'school counselor': "Anything with Alcohol",
        'programmer': "Hipster Craft Beer",
        'bike gang member': "Moonshine",
        'politician': "Your tax dollars",
        'rapper': 'Cristal',
    }
    
#     return drinks[param.lower()] if drinks[param.lower()] else "Beer"
    return drinks.get(param.lower(), "Beer")