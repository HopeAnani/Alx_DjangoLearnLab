# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"No author found with the name '{author_name}'"

def list_books_in_library(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Access related books via ManyToManyField
        return books
    except Library.DoesNotExist:
        return f"No library found with the name '{library_name}'"

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library without using Librarian.objects.get(library=...)."""
    try:
        library = Library.objects.get(name=library_name)  # Get the Library instance first
        librarian = library.librarian  # Access the related Librarian directly via OneToOneField reverse relationship
        return librarian
    except Library.DoesNotExist:
        return f"No library found with the name '{library_name}'"
    except AttributeError:
        return f"No librarian assigned to the library '{library_name}'"
