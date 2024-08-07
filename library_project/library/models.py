
from django.db import models

class UserProfile(models.Model):
    user = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    available_copies = models.IntegerField()

    def __str__(self):
        return self.book_name

