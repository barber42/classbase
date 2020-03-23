from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.last_name + ', ' + self.first_name

class Genre(models.Model):
	genre = models.CharField(max_length=50)
	
	def __str__(self):
		return self.genre

class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.ManyToManyField(Author)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE)	
	price = models.DecimalField(max_digits=6, decimal_places=2)
	copies = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.title
 
class Transaction(models.Model):
	books = models.ManyToManyField(Book)
	userid = models.ForeignKey(User, on_delete=models.CASCADE) 
	total = models.DecimalField(max_digits=6, decimal_places=2)
	date = models.DateField(auto_now_add=True)
