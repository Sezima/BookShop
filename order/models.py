from django.db import models

# Create your models here.
from main.models import Book


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orders')
    phone = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.phone}'

