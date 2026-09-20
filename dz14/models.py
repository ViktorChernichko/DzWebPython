from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, blank=True)
    published_year = models.PositiveIntegerField(null=True, blank=True)
    copies_available = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Reader(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
