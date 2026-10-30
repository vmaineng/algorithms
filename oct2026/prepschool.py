# track population growth of small towns
#write function that is take in initial population
#percent by what it grows each year
#the augmentation (number of inhabitant comes each year on top of growth)
#population you're trying to get to
#return n -> years from initial to expected goal

#receive an integer for initial population (whole) and goal number (whole)
#receive percent of growth (whole or float ex: 2 or 2.5,13.25/100), the augementation (whole/year)
#4 inputs - growth (positive numbers only)
#return an integer for the years to get from initial to expected

#ex: (initial, percent, augmentation, target)
#ex:  (100,      10  , 50      ,     200)   

#while our target has not been reached
#calculate first year's goal => (100 * .10) + 50 => 110 + 50 => 160.2 (round down)
#increment a count for the year
#second: (160 *.10 ) + 50 => (160 + 16) + 50 => 176 + 50 =. 226
#return 2

#calculate first year's goal => (100 * .025) + 50 => 175

import math

def trackPopulation(initial, percent, augmentation, target):
    year = 0
    while initial < target: #100 < 200, 160 < 200, 226 
        initial = math.floor((initial * percent) + augmentation) #(100 * .10) + 50 => 160, #226
        year += 1 # year = 2
    return year

print(trackPopulation(100, 1.1, 50, 200))

