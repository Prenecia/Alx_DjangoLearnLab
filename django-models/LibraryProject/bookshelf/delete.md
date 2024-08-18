# Delete Operation
["from bookshelf.models import Book"]
Command:
```python
from myapp.models import Book

# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion
books = Book.objects.all()
for book in books:
    print(book.title)
