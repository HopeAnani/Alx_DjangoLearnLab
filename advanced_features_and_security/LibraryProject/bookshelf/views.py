from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404

from .models import Book

@permission_required('your_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Process form submission for editing the book
    return render(request, 'edit_book.html', {'book': book})
