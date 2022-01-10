from django.urls import path
from . import views


app_name = 'borrowing'


urlpatterns = [
    path('', views.borrowing_list, name='borrowing_list'),
    path('add/', views.add_borrow, name='add_borrow'),
    path('<borrow_id>/', views.borrowing_detail, name='borrowing_detail'),
    path('<borrow_id>/edit/', views.edit_borrow, name='edit_borrow'),
    path('<borrow_id>/delete/', views.delete_borrow, name='delete_borrow'),
]
