from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.PositiveIntegerField()
    author = models.ForeignKey(
        'Author', related_name='author_book', on_delete=models.CASCADE)
    category = models.ForeignKey(
        'Category', related_name='category_book', on_delete=models.CASCADE)
    borrowed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.isbn}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
