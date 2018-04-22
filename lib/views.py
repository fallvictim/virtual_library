from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import BookInstance, Book


def main_page(request):
    books = Book.objects.order_by('title')
    return render(request, 'lib/main.html', {'books': books})


class BookListView(generic.ListView):
    model = Book


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'lib/book_detail.html', {'book': book})


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'lib/borrowed_books.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')