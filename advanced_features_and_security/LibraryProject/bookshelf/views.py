from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import Book
from django.http import HttpResponse
from .forms import ExampleForm

@permission_required('yourapp.can_view', raise_exception=True)
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

@permission_required('yourapp.can_create', raise_exception=True)
def book_create_view(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'book_form.html')

@permission_required('yourapp.can_edit', raise_exception=True)
def book_edit_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'book_form.html', {'book': book})

@permission_required('yourapp.can_delete', raise_exception=True)
def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})

books

def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'book_list.html', {'books': books})

def my_view(request):
    response = HttpResponse('Hello, world!')
    response['Content-Security-Policy'] = "default-src 'self';"
    return response
