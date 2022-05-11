from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    book_author = models.CharField(max_length=100)
    genres = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
