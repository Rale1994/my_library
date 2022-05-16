from django.urls import path
from . import views
from .views import BookCreateView, MyBookView, BookDetailView, BookUpdateView, BookDeleteView, AuthorBookView

urlpatterns = [
    path("", views.home, name="book-home"),
    path("about", views.about, name="book-about"),
    path("book/new/", BookCreateView.as_view(), name="book-add"),
    path("user/<str:username>", MyBookView.as_view(), name="user-book"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("book/<int:pk>/update", BookUpdateView.as_view(), name="book-update"),
    path("book/<int:pk>/delete", BookDeleteView.as_view(), name="book-delete"),
    path("book/<str:username>/<str:book_author>", AuthorBookView.as_view(), name="book-author")
]
