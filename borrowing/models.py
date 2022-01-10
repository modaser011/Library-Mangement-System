from django.db import models
from django.contrib.auth import get_user_model
from lib.models import Book

User = get_user_model()


class Borrow(models.Model):
    user = models.ForeignKey(
        User, related_name='borrow', on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, related_name='borrow', on_delete=models.CASCADE)
    exp = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.book}"
