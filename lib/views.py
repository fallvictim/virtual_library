from django.shortcuts import render
from .models import Book


def main_page(request):
    books = Book.objects.order_by('title')
    return render(request, 'lib/main.html', {'books': books})
