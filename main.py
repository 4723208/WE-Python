import sys
import json

books = [
    {
        "title" : "Java基礎",
        "author": "佐藤花子",
        "year": 2023,
        "isbn": "978-4-987654-32-1",
        "price": 2800
    },
    {
        "title" : "Web開発",
        "author": "山田次郎",
        "year": 2023,
        "isbn": "978-4-11111-11-1",
        "price": 3200
    },
]

print(sys.argv)

new_book = sys.argv[1]
new_data = json.loads(new_book)
books.append(new_data)

print(books)