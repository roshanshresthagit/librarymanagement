from django.db import models
from accounts.models import User
# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=32, unique=True)
    published_date = models.DateField()
    genre = models.CharField(max_length=50)

class BookDetails(models.Model):
    details_id = models.AutoField(primary_key=True)
    book_id = models.OneToOneField(Book, on_delete=models.CASCADE)
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    language = models.CharField(max_length=50)

class BorrowedBooks(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True,blank=True)


