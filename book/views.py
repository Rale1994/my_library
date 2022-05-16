from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Book
from django.contrib.auth.models import User
from django.views.generic import (CreateView, ListView, DetailView, UpdateView, DeleteView)

# Create your views here.

books = [
    {
        "author": "Tolkien",
        "title": "The lord of the rings",
        "genres": "Epic fantasy",

    },
    {
        "author": "Donato Karizi",
        "title": "Whisper",
        "genres": "Crime",

    }
]


class BookCreateView(CreateView):
    model = Book
    fields = ["title", "book_author", "content", "genres"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('book-home')


class MyBookView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book/my_book.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        user1 = get_object_or_404(User, username=self.kwargs.get('username'))
        return Book.objects.filter(user=user1)


class AuthorBookView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book/author_book.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        user1 = get_object_or_404(User, username=self.kwargs.get('username'))
        print(user1)
        book_of_author = get_list_or_404(Book, book_author=self.kwargs.get('book_author'))
        for book in book_of_author:
            return Book.objects.filter(user=user1).filter(book_author=book.book_author)
        # for book in book_of_author:
        #     print(book.book_author)
        # return book_of_author


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    fields = ["title", "content", "book_author", "genres"]


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ["title", "content", "book_author", "genres"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.user:
            return True
        else:
            return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = "/"

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.user:
            return True
        else:
            return False


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, "book/home.html", context)


def about(request):
    return render(request, "book/about.html")
