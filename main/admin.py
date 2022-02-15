from django.contrib import admin

# Register your models here.
from main.models import Author, Book, Genre

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)




