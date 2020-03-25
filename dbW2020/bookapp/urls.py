from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as authviews

urlpatterns = [
	path('', views.book_list, name='book_list'),
	path('book/new/', views.book_new, name='book_new'),
	path('author/new', views.author_new, name='author_new'),
	path('transaction/new', views.transaction_new, name='transaction_new'),
	path('transaction/list/', views.transaction_list, name='transaction_list'),
	path('accounts/login/', authviews.LoginView.as_view(), name='login'),
	path('accounts/logout/', authviews.LogoutView.as_view(next_page='/'), name='logout'),
]
