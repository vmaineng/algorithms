library = [
    {
        "book_id": 101,
        "title": "Python Fundamentals",
        "author": {
            "name": "Jane Smith",
            "country": "USA",
            "birth_year": 1980
        },
        "genres": ["Programming", "Education", "Technology"],
        "copies": 5,
        "available": 3,
        "ratings": [4.5, 4.8, 4.2, 5.0, 4.3]
    },
    {
        "book_id": 102,
        "title": "The Silent Patient",
        "author": {
            "name": "Alex Michaelides",
            "country": "Cyprus",
            "birth_year": 1977
        },
        "genres": ["Thriller", "Mystery", "Fiction"],
        "copies": 8,
        "available": 2,
        "ratings": [4.2, 4.0, 4.5, 4.1, 3.9, 4.6]
    },
    {
        "book_id": 103,
        "title": "Becoming",
        "author": {
            "name": "Michelle Obama",
            "country": "USA",
            "birth_year": 1964
        },
        "genres": ["Memoir", "Biography", "Inspirational"],
        "copies": 12,
        "available": 4,
        "ratings": [4.9, 4.8, 5.0, 4.9, 4.7, 4.8, 4.9]
    },
    {
        "book_id": 104,
        "title": "The Code Book",
        "author": {
            "name": "Simon Singh",
            "country": "UK",
            "birth_year": 1964
        },
        "genres": ["Science", "History", "Cryptography"],
        "copies": 3,
        "available": 1,
        "ratings": [4.3, 4.1, 4.4, 4.0]
    }
]


def get_all_books(list):
    output = []
    for book in library:
        output.append(book["title"])
    return output

# print(get_all_books(library))


def get_all_authors(list):
    output = []
    for book in library:
        output.append(book['author']['name'])
    return output

# print(get_all_authors(library))

def get_all_books(list):
    for book in library:
        return book if book['available'] > 0 else book #check
    
def get_unique(list):
    output = []
    for book in library:
        output.append(book['genres'])

    return list(set(output)) #check again

# print(get_unique(library))

def get_average_rating(list):
    #for every book, calc their own average
    total = 0
    for book in library:
        total =sum([book["ratings"]])
        avg = total /len(book["ratings"])
        return book[id], avg
    
    averages = {}
    for book in library:
        ratings = book["ratings"]
        avg = sum(ratings) /len(ratings)
        averages[book["book_id"]] = round(avg,2)
    return averages
      
    
def get_list_authors_book_count(list):
    author_counts = {}
    for book in library:
        author = book["author"]["name"]
        if author in author_counts:
            author_counts[author] += 1
        else:
            author_counts[author] = 1
    result = []
    for author, count in author_counts.items():
        result.append({"name": author, "book_count": count})
    return result


def get_thriller_books(list):
    for book in library:
        for genre in book['genres']:
            if genre == 'Thriller':
                return book["title"]
            
def get_total_copies(list):
    total = 0
    available = 0

    for book in library:
        total += book["copies"]
        avaiable += book["available"]
    # return f"{"total_copies:" total, "total_available:"available"}"
              
# def get_highest_rating(list):
    
# person = {"name": "Alice", "age": 30, "city": "New York"}
# print(person["name"])

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# names = []
# for person in people:
#     names.append(person["name"])
# print(names)

# ages = []
# for person in people:
#     ages.append(person["age"])
# (print(ages))

old_names=[]
for person in people:
    if person["age"] > 30:
        old_names.append(person["name"])
# print(old_names)

students = [
    {"name": "Emma", "grade": 85, "subjects": ["math", "science"]},
    {"name": "Liam", "grade": 92, "subjects": ["history", "art"]},
    {"name": "Sophia", "grade": 78, "subjects": ["math", "english"]}
]

names=[]
for person in students:
    names.append(person['name'])

grades=[]
for person in students:
    grades.append(person["grade"])

good_students =[]
for person in students:
    if person["grade"] > 90:
        good_students.append(person["name"])

all_subjects = []
for subject in students:
    all_subjects.extend(subject["subjects"])
return list(set(all_subjects))


import { useState } from 'react';

const App = () => {
  const [count, setCount] = useState(0)

  const handleUpClick= () => {
    setCount(count + 1)
  }

  const handleDownClick= () => {
    setCount(count -1)
  }
  return <div className="flex justify-center h-screen items-center ">
    <button className="m-2 px-4 py-2 border border-2 bg-red-100" onClick={handleDownClick}>-</button>
    <div>{count}</div>
     <button className="m-2 px-4 py-2 border border-2 bg-green-100" onClick={handleUpClick}>+</button>
  </div>;
};

export default App;

def is_vow(inp):
    #receive a list of integers
    #return a list back filled with integers and lowercase chars if the nubmers matches lowercase vowels
    #ex: [100, 97] => [100, 'a']
    
    #intialize an empty list
    #iterate through each number
    #check if the number is chr == any of the lowercase vowels
    #return the lowercase chars
    #else, return the integer
    
    result = []
    vowels = ['a', 'e','i','o','u']
    
    for num in inp:
        if chr(num) in vowels:
            result.append(chr(num))
        else:
            result.append(num)
    return result