from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()
    publisher = models.CharField(max_length=255, null=True, blank=True)
    image_path = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title
