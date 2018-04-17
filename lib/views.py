from django.shortcuts import render, get_object_or_404
from .models import Book


def main_page(request):
    books = Book.objects.order_by('title')
    return render(request, 'lib/main.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'lib/book_detail.html', {'book': book})