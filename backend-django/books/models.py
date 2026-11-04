from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()
    publisher = models.CharField(max_length=255, null=True, blank=True)
    image_path = models.CharField(max_length=255, null=True, blank=True)
    # 追加機能専用（いいね・いいね数順）。基本機能では使わず、列だけ先に用意する。
    like_count = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title
