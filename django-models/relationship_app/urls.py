from django.urls import path
from .views import register_view, login_view, logout_view, admin_view, librarian_view, member_view, add_book_view, change_book_view, delete_book_view
from django.contrib.auth.views import LoginView, LogoutView
from .views import BookListView, LibraryDetailView

urlpatterns = [
    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    # Book and Library URLs
    path('books/', BookListView.as_view(), name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Role-based views
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

    # Book management URLs
    path('add_book/', add_book_view, name='add_book'),
    path('change_book/<int:pk>/', change_book_view, name='change_book'),
    path('delete_book/<int:pk>/', delete_book_view, name='delete_book'),
]

["views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]
["edit_book/"]
