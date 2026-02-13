actor_list = ["Fangs of Fortune", "story of a pearl girl", "Love and Redemption", "Love in the Clouds"]

# print(actor_list[0]) #"Fangs of Fortune"

# for movie in actor_list:
#     print(movie)

# Fangs of Fortune
# story of a pearl girl
# Love and Redemption
# Love in the Clouds

# Our list of user objects (dictionaries in Python)
users = [
    {
        "id": 1,
        "name": "Alice Chen",
        "email": "alice@example.com",
        "age": 28,
        "is_active": True,
        "skills": ["Python", "JavaScript", "SQL"]
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "email": "bob@example.com", 
        "age": 35,
        "is_active": False,
        "skills": ["Java", "C++", "AWS"]
    },
    {
        "id": 3,
        "name": "Carol Davis",
        "email": "carol@example.com",
        "age": 42,
        "is_active": True,
        "skills": ["Python", "Data Analysis", "Machine Learning"]
    },
    {
        "id": 4,
        "name": "David Wilson",
        "email": "david@example.com",
        "age": 31,
        "is_active": True,
        "skills": ["React", "Node.js", "MongoDB"]
    }
]

def get_names(list):
    output = []
    for user in users:
        # print("user", user)
        output.append(user["name"])
    return output
# print(get_names(users))

def get_active_emails(list):
    output = []
    for user in users:
        if user["is_active"] == True:
            output.append(user["email"])
    return output

def users_over_30(list):
    output = []
    for user in users:
        if user["age"] > 30:
            output.append(user)
    return output

def get_unique_skills(list):
    skills_list = []
    for user in users:
        skills_list.extend(user["skills"])
    return skills_list
print(get_unique_skills(users))

def create_dict(list):
    #no idea
    id_to_name={}
    for user in users:
        id_to_name[user["id"]] = user["name"]
    return id_to_name

def get_average(list):
    score = 0
    active_count = 0
    for user in users:
        if user["is_active"] == True:
            score += user['age']
            active_count += 1

    if active_count == 0:
        return 0
    return score/active_count


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    #receive a list of integers (pos or neg)
    #return a list back where integers are reversed
    #ex: [-1, 3, 6, 2] => [2, 6, 3, -1]
    
    # return a[::-1]
    
    #initialize an empty list
    #iterate starting from the end , and go up to the front
    #add each value into the list
    #return the list
    
    result = []
    for i in range(len(a)-1, -1, -1):
        result.append(a[i])
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
  max_count = float('-inf')
    
    for row in range(4):
        for col in range(4):
            total = (arr[row][col] + arr[row][col+1] + arr[row ][col+2]
            + arr[row+1][col+1]
            + arr[row+2][col] + arr[row+2][col+ 1] + arr[row+2][col+2])
            
            if total > max_count:
                max_count = total
                
    return max_count