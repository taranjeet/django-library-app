from django.db import models


class Book(models.Model):

    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name

    def get_authors(self):
        return ', '.join(self.authors.all().values_list('name', flat=True))


class Author(models.Model):

    name = models.CharField(max_length=255)
    book = models.ForeignKey(
        Book,
        related_name='authors', on_delete=models.SET_NULL,
        null=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.name
