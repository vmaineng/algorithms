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

print(get_all_authors(library))