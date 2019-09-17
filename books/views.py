from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=True)
            return redirect("home")
    else:
        form = BookForm()
    return render(request, "book_form.html", {"form": form})

def edit_book(request, pk):
    instance = Book.objects.get(id=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            book = form.save(commit=True)
            return redirect("home")
    else:
        form = BookForm(instance=instance)

    return render(request, "book_form.html", {"form": form, "is_edit": True})
