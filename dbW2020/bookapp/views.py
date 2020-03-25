from django.shortcuts import render
from .models import Book, Author, Genre, Transaction
from .forms import BookForm, AuthorForm, TransactionForm
from django.shortcuts import redirect
from decimal import Decimal
from django.contrib.auth.decorators import login_required

# Create your views here.

def book_list(request):
	books = Book.objects.all()
	return render(request, 'bookapp/book_list.html', {'books' : books})

@login_required
def transaction_list(request):
	transactions = Transaction.objects.all()
	return render(request, 'bookapp/transaction_list.html', {'transactions' : transactions})

@login_required
def book_new(request):
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			book = form.save(commit=False)
			book.save()
			form.save_m2m()
			return redirect('/')	
	else:
		form = BookForm()			
	return render(request, 'bookapp/book_edit.html', {'form': form})

def author_new(request):
	if request.method == "POST":
		form = AuthorForm(request.POST)
		if form.is_valid():
			author = form.save(commit=False)
			author.save()
			return redirect('book_new')	
	else:
		form = AuthorForm()			
	return render(request, 'bookapp/author_edit.html', {'form': form})

@login_required
def transaction_new(request):
	if request.method == "POST":
		form =TransactionForm(request.POST)
		if form.is_valid():
			transaction = form.save(commit=False)
			
			total = Decimal.from_float(0.00)
			uname = request.user
			transaction.total = total
			transaction.userid = uname 	
			
			transaction.save()
			form.save_m2m()
				
			for book in transaction.books.all():
				total = total + book.price
				book.copies -= 1
				book.save()				
			
			transaction.total = total
			transaction.save()
			
			return redirect('/')	
	else:
		form = TransactionForm()			
	return render(request, 'bookapp/transaction_edit.html', {'form': form})
