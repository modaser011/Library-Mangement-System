from django.shortcuts import render, redirect, get_object_or_404
from .models import Borrow
from .forms import BorrowForm
from django.contrib.auth.decorators import login_required


@login_required
def borrowing_list(request):
    borrow = Borrow.objects.filter(user=request.user)
    context = {
        'borrow': borrow,
    }
    return render(request, 'borrowing/book_list.html', context)


@login_required
def borrowing_detail(request, borrow_id):
    borrow = get_object_or_404(Borrow, pk=borrow_id)
    context = {
        'borrow': borrow,
    }
    return render(request, 'borrowing/book_detail.html', context)


@login_required
def add_borrow(request):
    user = request.user
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            borrow.user = user
            borrow.save()
            return redirect("borrowing:borrowing_list")
    else:
        form = BorrowForm()

    context = {
        "form": form
    }

    return render(request, 'borrowing/book_add.html', context)


@login_required
def edit_borrow(request, borrow_id):
    bor = get_object_or_404(Borrow, pk=borrow_id)
    user = request.user
    if request.method == 'POST':
        form = BorrowForm(request.POST, instance=bor)
        if form.is_valid():
            borrow = form.save(commit=False)
            borrow.user = user
            borrow.save()
            return redirect("borrowing:borrowing_list")
    else:
        form = BorrowForm(instance=bor)

    context = {
        "form": form
    }

    return render(request, 'borrowing/book_add.html', context)


@login_required
def delete_borrow(request, borrow_id):
    bor = get_object_or_404(Borrow, pk=borrow_id)
    bor.delete()
    return redirect("borrowing:borrowing_list")
