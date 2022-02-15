from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=80, blank=True)
    date_of_birth = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to='authors')

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Genre(models.Model):
    slug = models.SlugField(max_length=55, primary_key=True)
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    CHOICES = (
        ('in stock', 'в наличии'),
        ('out of stock', 'нет в наличии')
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='books')
    status = models.CharField(choices=CHOICES, max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

    genre = models.ManyToManyField(Genre)







