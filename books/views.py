from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

# Create your views here.
def home(request):
    return render(request, "index.html")

def add_book(request):
    form = BookForm()
    return render(request, "book_form.html", {"form": form})
