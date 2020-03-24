from django import forms

from .models import Book, Author, Transaction

class BookForm(forms.ModelForm):

	class Meta:
		model = Book
		fields = ('title', 'author', 'genre', 'price', 'copies',)

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ('first_name', 'last_name')

class TransactionForm(forms.ModelForm):
	class Meta:
		model = Transaction
		fields = ('books',)
