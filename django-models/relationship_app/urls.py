from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),
]

from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

["views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]

from .views import admin_view, librarian_view, member_view

urlpatterns += [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]

urlpatterns += [
    path('add_book/', add_book_view, name='add_book'),
    path('change_book/<int:pk>/', change_book_view, name='change_book'),
    path('delete_book/<int:pk>/', delete_book_view, name='delete_book'),
]

["edit_book/"]
