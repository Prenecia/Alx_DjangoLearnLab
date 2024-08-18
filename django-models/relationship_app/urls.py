from django.urls import path
from .views import register_view, login_view, logout_view
from .views import admin_view, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Role-based access URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    
    # Book management URLs
    path('add_book/', add_book_view, name='add_book'),
    path('change_book/<int:pk>/', change_book_view, name='change_book'),
    path('delete_book/<int:pk>/', delete_book_view, name='delete_book'),
]
