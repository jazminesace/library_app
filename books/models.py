from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    GENRE_CHOICES = [
        ("Adventure", 'Adventure'),
        ("Drama", 'Drama'),
        ("Fantasy", 'Fantasy'),
        ("History", 'History'),
        ("Graphic Novel", 'Graphic Novel'),
        ("Horror", 'Horror'),
        ("Mystery", 'Mystery'),
        ("Romance", 'Romance'),
        ("Science Fiction", 'Science Fiction'),
        ("Thriller", 'Thriller'),
        ("Young adult", 'Young Adult'),
    ]
 
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year_published = models.PositiveSmallIntegerField()
    plot_summary = models.TextField()
    cover = models.ImageField(upload_to="book_covers/")
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)
    is_deleted = models.BooleanField(default=False)

    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.title} ({self.author}, {self.year_published}) {self.is_deleted}"