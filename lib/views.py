from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from .models import BookInstance, Book, User


def main_page(request):
    books = Book.objects.order_by('title')
    return render(request, 'lib/main.html', {'books': books})


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'lib/borrowed_books.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    permission_required = 'lib.change_book'
    template_name = 'lib/all_borrowed_books.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    permission_required = 'lib.change_book'


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    permission_required = 'lib.change_book'


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    template_name = 'lib/book_delete.html'
    permission_required = 'lib.change_book'


class BookInstanceCreate(PermissionRequiredMixin, CreateView):
    model = BookInstance
    fields = '__all__'
    template_name = 'lib/bookinst_form.html'
    permission_required = 'lib.change_book'


class BookInstanceUpdate(PermissionRequiredMixin, UpdateView):
    model = BookInstance
    fields = '__all__'
    template_name = 'lib/bookinst_form.html'
    permission_required = 'lib.change_book'


class BookInstanceDelete(PermissionRequiredMixin, DeleteView):
    model = BookInstance
    fields = '__all__'
    success_url = reverse_lazy('books')
    template_name = 'lib/bookinst_delete.html'
    permission_required = 'lib.change_book'


class UserCreate(PermissionRequiredMixin, CreateView):
    model = User
    fields = ['password', 'username', 'first_name', 'last_name']
    template_name = 'lib/book_form.html'
    permission_required = 'lib.change_book'
    success_url = '/'
