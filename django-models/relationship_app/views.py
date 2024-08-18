from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import user_passes_test, permission_required
from .models import Book, Library, UserProfile

# Authentication Views
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')

# Role-based Views
def user_role_check(role):
    return user_passes_test(lambda u: UserProfile.objects.get(user=u).role == role)

@user_role_check('Admin')
def admin_view(request):
    return render(request, 'admin_view.html')

@user_role_check('Librarian')
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_role_check('Member')
def member_view(request):
    return render(request, 'member_view.html')

# Book Management Views
@permission_required('relationship_app.can_add_book')
def add_book_view(request):
    # Implementation for adding a book
    pass

@permission_required('relationship_app.can_change_book')
def change_book_view(request, pk):
    # Implementation for changing a book
    pass

@permission_required('relationship_app.can_delete_book')
def delete_book_view(request, pk):
    # Implementation for deleting a book
    pass

# Book and Library Views
from django.views.generic import ListView, DetailView

class BookListView(ListView):
    model = Book
    template_name = 'list_books.html'
    context_object_name = 'books'

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

["relationship_app/list_books.html"]
["relationship_app/library_detail.html"]
["from django.views.generic.detail import DetailView"]
