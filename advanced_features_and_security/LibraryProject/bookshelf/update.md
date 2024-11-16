# Update Operation

Command:
python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

Expected Output: The book title will be updated in the database.