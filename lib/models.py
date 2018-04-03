from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    cipher = models.CharField(max_length=50)
    volume = models.PositiveSmallIntegerField()
    publishing_info = models.TextField()
    on_loan = models.BooleanField('On loan')
    subscriber = models.ForeignKey(
        'Subscriber',
        models.SET_NULL,
        blank=True,
        null=True
    )

#    def lend(self):
#        self.on_loan = True
#        self.save()

    def __str__(self):
        return self.title + ' ' + self.author


class Subscriber(models.Model):
    lib_card = models.CharField(max_length=50)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
