
### Create Operation

**Command:**

```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(book)
Output:

yaml
Copy code
1984
go
Copy code

**`retrieve.md`:**

```markdown
### Retrieve Operation

**Command:**

```python
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
Output:

yaml
Copy code
1984 George Orwell 1949
go
Copy code

**`update.md`:**

```markdown
### Update Operation

**Command:**

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
Output:

Copy code
Nineteen Eighty-Four
go
Copy code

**`delete.md`:**

```markdown
### Delete Operation

**Command:**

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
books = Book.objects.all()
print(books)
Output:

css
Copy code
[]
python
Copy code

### Task 2: Utilizing the Django Admin Interface

#### 1. Register the Book Model with the Django Admin

Edit `bookshelf/admin.py` to register the `Book` model:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
