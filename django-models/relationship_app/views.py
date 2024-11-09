from django.shortcuts import render, redirect
from relationship_app.models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

def list_books(request):
    """Function-based view to list all books."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """Class-based view to display a specific library's details."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'




# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Use Django's built-in LoginView
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Use Django's built-in LogoutView
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'



# Helper function to check if the user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Helper function to check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Helper function to check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin View - Only Admins can access this view
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View - Only Librarians can access this view
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View - Only Members can access this view
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
