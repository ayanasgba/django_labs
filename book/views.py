from django.shortcuts import render
from . import models
# Create your views here.

def books_view(request):
    book_value = models.Book.objects.all()
    return render(request, "books.html",{"book_key":book_value})

