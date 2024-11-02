# CRUD Operations Documentation

## Create Operation
Command:
python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

Expected Output: The book instance will be created in the database.

## Retrieve Operation
Command:
python
book = Book.objects.get(title="1984")
print(book)

Expected Output : <QuerySet [<Book: 1984>]>

# Update Operation

Command:
python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

Expected Output: The book title will be updated in the database.

# Delete Operation

Command:
python
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

Expected Output: <QuerySet []>
