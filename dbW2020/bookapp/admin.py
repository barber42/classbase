from django.contrib import admin
from .models import Book, Author, Genre, Transaction
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Transaction)
