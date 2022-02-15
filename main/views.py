from django.shortcuts import render

# Create your views here.
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'main/index.html', {'books': books})