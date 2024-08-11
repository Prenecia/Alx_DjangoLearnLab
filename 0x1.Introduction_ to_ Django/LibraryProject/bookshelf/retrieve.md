# Retrieve Operation
["Book.objects.get", "1984"]
Command:
```python
from myapp.models import Book

# Retrieve all books
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
