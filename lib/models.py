from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from datetime import date


class Book(models.Model):
    author = models.CharField(max_length=200, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    cipher = models.CharField(max_length=50, verbose_name="Библиотечный шифр")
    volume = models.PositiveSmallIntegerField(verbose_name="Объем")
    publishing_info = models.TextField(verbose_name="Издание")

    def __str__(self):
        return self.title + ' ' + self.author

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])



class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library",
                          verbose_name='Идентификатор')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True, verbose_name="Книга")
    imprint = models.CharField(max_length=200, blank=True, verbose_name="Информация")
    due_back = models.DateField(null=True, blank=True, verbose_name="Срок возврата")

    LOAN_STATUS = (
        ('m', 'На складе'),
        ('o', 'Выдана'),
        ('a', 'Доступна'),
        ('r', 'Зарезервирована'),
    )

    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Подписчик")

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', verbose_name='Статус')

    class Meta:
        ordering = ["due_back"]

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title)


    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.book.id)])