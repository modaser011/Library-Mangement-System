from django.urls import path
from . import views


app_name = 'lib'


urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('add/', views.add_book, name='add_book'),
    path('<book_id>/edit/', views.edit_book, name='edit_book'),
    path('<book_id>/delete/', views.delete_book, name='delete_book'),
]
