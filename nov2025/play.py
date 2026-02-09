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


