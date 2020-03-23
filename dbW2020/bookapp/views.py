from django.shortcuts import render
from .models import Book, Author, Genre, Transaction
# Create your views here.

def book_list(request):
	books = Book.objects.all()
	return render(request, 'bookapp/book_list.html', {'books' : books})
