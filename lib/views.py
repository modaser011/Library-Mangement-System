from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Book, Category, Author
from .forms import BookForm
from django.db.models import Count, Q


class BookList(ListView):
    model = Book

    def get_queryset(self):
        object_list = Book.objects.filter(borrowed=False)
        return object_list


class BookDetail(DetailView):
    model = Book

    def get_queryset(self):
        book = Book.objects.filter(borrowed=False)
        return book


def add_book(request):
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("lib:book_list")
        else:
            form = BookForm()

        context = {
            "form": form
        }

        return render(request, 'lib/book_add.html', context)
    else:
        return redirect('login')


def edit_book(request, book_id):
    if request.user.is_authenticated and request.user.is_staff:
        book = get_object_or_404(Book, pk=book_id)
        if request.method == 'POST':
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect("lib:book_list")
        else:
            form = BookForm(instance=book)

        context = {
            "form": form
        }

        return render(request, 'lib/book_add.html', context)
    else:
        return redirect('login')


def delete_book(request, book_id):
    if request.user.is_authenticated and request.user.is_staff:
        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return redirect("lib:book_list")
    else:
        return redirect('login')
