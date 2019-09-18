from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        books = Book.objects.filter(posted_by=request.user).filter(is_deleted=False)
        return render(request, "index.html", {"books": books})
    else:
        return redirect("login")

def add_book(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.posted_by = request.user
            book.save()
            return redirect("home")
    else:
        form = BookForm()
    return render(request, "book_form.html", {"form": form})

def edit_book(request, pk):
    if not request.user.is_authenticated:
        return redirect("login")

    try:        
        instance = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return redirect("home")

    if instance.posted_by != request.user:
        return redirect("home")

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            book = form.save(commit=True)
            return redirect("home")
    else:
        form = BookForm(instance=instance)

    return render(request, "book_form.html", {"form": form, "is_edit": True})

def view_book(request, pk):
    if request.user.is_authenticated:
        book = Book.objects.get(id=pk)
        if book.is_deleted:
            return redirect("home")
        return render(request, "book_details.html", {"book": book})
    else:
        return redirect("login")

def delete_book(request, pk):
    book = Book.objects.get(id=pk)

    if book.posted_by != request.user:
        return redirect("home")

    book.is_deleted = True
    book.save(update_fields=['is_deleted'])

    return redirect("home")